import pytest

from risiko.core.shell.base import ShellBase
from risiko.core.shell.interface import ShellInterface


def test_shell_creation():
    """Test that a ShellBase can be instantiated with valid properties."""
    shell = ShellBase(shell_type="live", damage=1)
    assert shell.shell_type == "live"
    assert shell.damage == 1


def test_shell_creation_with_negative_damage_raises_exception():
    """Test that creating a shell with negative damage raises a ValueError."""
    with pytest.raises(ValueError):
        ShellBase(shell_type="live", damage=-1)


def test_shellbase_is_shellinterface():
    """Test that ShellBase is a valid implementation of ShellInterface."""
    shell = ShellBase(shell_type="live", damage=1)
    assert isinstance(shell, ShellInterface)
