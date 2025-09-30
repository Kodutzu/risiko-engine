from risiko import RisikoState, processors
from risiko.core import PlayerBase, ShellBase   

state = RisikoState()


class AIPlayer(PlayerBase): ...


state = processors.add_player_to_game(
    game_state=state, player=AIPlayer(id="test", charges=6)
)

state = processors.load_magazine(
    game_state=state,
    round=[
        ShellBase(shell_type="live", damage=1),
        ShellBase(shell_type="live", damage=1),
        ShellBase(shell_type="blank", damage=0),
        ShellBase(shell_type="blank", damage=0),
    ],
)


state = processors.shuffle_magazine(game_state=state)
state = processors.shotgun_load_shell(game_state=state)
state = processors.unload_shotgun_chamber(game_state=state)
print([shell.shell_type for shell in state.shotgun.magazine.tube])
# fired_shell,state = processors.fire_shell(game_state=state, shooter_id="test")

# print(fired_shell.shell_type)
