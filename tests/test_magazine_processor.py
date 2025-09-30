from collections import deque

import pytest
from attrs import evolve

from risiko.core.magazine.base import MagazineBase
from risiko.core.magazine.exception import MagazineEmptyException
from risiko.core.shell import InvalidShell, ShellNotFoundException
from risiko.core.shell.base import ShellBase
from risiko.core.shotgun.base import ShotgunBase
from risiko.service.processors import magazine as magazine_processor
from risiko.service.risiko_state import RisikoState


@pytest.fixture
def live_shell():
    return ShellBase(shell_type="live", damage=1)


@pytest.fixture
def blank_shell():
    return ShellBase(shell_type="blank", damage=0)


@pytest.fixture
def initial_game_state():
    return RisikoState()


@pytest.fixture
def magazine_with_one_shell(live_shell):
    return MagazineBase(tube=deque([live_shell]))


@pytest.fixture
def magazine_with_shells(live_shell, blank_shell):
    return MagazineBase(tube=deque([live_shell, blank_shell, live_shell]))


# --- Test cases for load_magazine ---
def test_load_magazine_success_empty_magazine(initial_game_state, live_shell):
    new_state = magazine_processor.load_magazine(initial_game_state, [live_shell])
    assert len(new_state.shotgun.magazine.tube) == 1
    assert new_state.shotgun.magazine.tube[0] == ShellBase(shell_type="live", damage=1)


def test_load_magazine_success_non_empty_magazine(
    initial_game_state, live_shell, blank_shell, magazine_with_one_shell
):
    state_with_one_shell = evolve(
        initial_game_state, shotgun=ShotgunBase(magazine=magazine_with_one_shell)
    )

    new_state = magazine_processor.load_magazine(
        state_with_one_shell, [blank_shell]
    )
    assert len(new_state.shotgun.magazine.tube) == 2
    assert new_state.shotgun.magazine.tube[0] == ShellBase(shell_type="live", damage=1)
    assert new_state.shotgun.magazine.tube[1] == ShellBase(shell_type="blank", damage=0)


def test_load_magazine_invalid_shell_raises_exception(initial_game_state):
    with pytest.raises(InvalidShell):
        magazine_processor.load_magazine(initial_game_state, ["not_a_shell"])


# --- Test cases for eject_magazine_shell ---
def test_eject_magazine_shell_success(
    initial_game_state, live_shell, magazine_with_one_shell
):
    state_with_shell = evolve(
        initial_game_state, shotgun=ShotgunBase(magazine=magazine_with_one_shell)
    )

    ejected_shell, new_state = magazine_processor.eject_magazine_shell(state_with_shell)
    assert ejected_shell == live_shell
    assert len(new_state.shotgun.magazine.tube) == 0


def test_eject_magazine_shell_empty_magazine_raises_exception(initial_game_state):
    with pytest.raises(MagazineEmptyException):
        magazine_processor.eject_magazine_shell(initial_game_state)


# --- Test cases for insert_shell_to_magazine ---
def test_insert_shell_to_magazine_success(initial_game_state, live_shell):
    new_state = magazine_processor.insert_shell_to_magazine(
        initial_game_state, live_shell
    )
    assert len(new_state.shotgun.magazine.tube) == 1
    assert new_state.shotgun.magazine.tube[0] == ShellBase(shell_type="live", damage=1)


def test_insert_shell_to_magazine_invalid_shell_raises_exception(
    initial_game_state,
):
    with pytest.raises(InvalidShell):
        magazine_processor.insert_shell_to_magazine(
            initial_game_state, "not_a_shell"
        )


# --- Test cases for remove_shell_from_magazine ---
def test_remove_shell_from_magazine_success(
    initial_game_state, live_shell, magazine_with_one_shell
):
    state_with_shell = evolve(
        initial_game_state, shotgun=ShotgunBase(magazine=magazine_with_one_shell)
    )

    new_state = magazine_processor.remove_shell_from_magazine(
        state_with_shell, live_shell
    )
    assert len(new_state.shotgun.magazine.tube) == 0


def test_remove_shell_from_magazine_non_existent_raises_exception(
    initial_game_state, blank_shell, magazine_with_one_shell
):
    state_with_shell = evolve(
        initial_game_state, shotgun=ShotgunBase(magazine=magazine_with_one_shell)
    )

    with pytest.raises(ShellNotFoundException):
        magazine_processor.remove_shell_from_magazine(
            state_with_shell, blank_shell
        )


def test_remove_shell_from_magazine_invalid_shell_raises_exception(
    initial_game_state,
):
    with pytest.raises(InvalidShell):
        magazine_processor.remove_shell_from_magazine(
            initial_game_state, "not_a_shell"
        )


# --- Test cases for shuffle_magazine ---
def test_shuffle_magazine_non_empty(
    initial_game_state, magazine_with_shells
):
    state_with_shells = evolve(
        initial_game_state, shotgun=ShotgunBase(magazine=magazine_with_shells)
    )

    new_state = magazine_processor.shuffle_magazine(state_with_shells)
    # Check that the contents are the same, but order might be different
    assert sorted(
        new_state.shotgun.magazine.tube, key=lambda s: s.shell_type
    ) == sorted(state_with_shells.shotgun.magazine.tube, key=lambda s: s.shell_type)
    # It's possible but unlikely for the order to be the same after shuffle, so we don't assert inequality
    assert (
        new_state.shotgun.magazine.tube is not state_with_shells.shotgun.magazine.tube
    )  # Should be a new instance of the tube


def test_shuffle_magazine_empty(initial_game_state):
    new_state = magazine_processor.shuffle_magazine(initial_game_state)
    assert len(new_state.shotgun.magazine.tube) == 0
    assert new_state == initial_game_state  # Should be identical if no change


# --- Test cases for clear_magazine ---
def test_clear_magazine_success(
    initial_game_state, magazine_with_one_shell
):
    state_with_shell = evolve(
        initial_game_state, shotgun=ShotgunBase(magazine=magazine_with_one_shell)
    )

    new_state = magazine_processor.clear_magazine(state_with_shell)
    assert len(new_state.shotgun.magazine.tube) == 0


def test_clear_magazine_empty_raises_exception(initial_game_state):
    with pytest.raises(MagazineEmptyException):
        magazine_processor.clear_magazine(initial_game_state)