from pydantic import BaseModel, Field, PrivateAttr
from ..core.player.player import Player  
from ..core.game.snapshot import GameSnapshot
from .shotgun_handler import ShotgunHandler

class RoundHandler:
    
    @staticmethod
    def get_current_round(snapshot: GameSnapshot) -> int:

        return snapshot.round_number

    @staticmethod
    def advance_round(snapshot: GameSnapshot) -> GameSnapshot:

        snapshot_advance_round = snapshot.model_copy(deep=True)

        players = snapshot_advance_round.players
        gun = snapshot_advance_round.shotgun

        #clearing player's Inventory and Effector
        for player in players:
            player.inventory.items.clear()
            player.effector.effects.clear()

        #clearing shotgun effects
        gun.effector.effects.clear()

        snapshot_advance_round.round_number += 1

        return snapshot_advance_round
    
    @staticmethod
    def is_round(snapshot: GameSnapshot) -> bool:

        return not snapshot.shotgun.magazine
        

    @staticmethod
    def reset_round(snapshot: GameSnapshot) -> GameSnapshot:    

        snapshot_reset_round = snapshot.model_copy(deep=True)

        snapshot_reset_round.round_number = 0

        return snapshot_reset_round
    
    @staticmethod
    def add_player(snapshot: GameSnapshot, player: Player) -> GameSnapshot:

        snapshot_add_player = snapshot.model_copy(deep=True)
        players = snapshot_add_player.players

        for p in players:

            if p.id == player.id:

                raise ValueError("Player already in game")
            
        players.append(player)

        return snapshot_add_player
    @staticmethod
    def remove_player(snapshot: GameSnapshot, player: Player) -> GameSnapshot:

        snapshot_remove_player = snapshot.model_copy(deep=True)
        players = snapshot_remove_player.players

        for p in players:
            if p.id == player.id:
                players.remove(p)

                return snapshot_remove_player
            
        raise ValueError("Player doesn't exist")


    
    @staticmethod
    def total_players(snapshot: GameSnapshot) -> int:

        return len(snapshot.players)





