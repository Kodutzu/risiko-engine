from pydantic import BaseModel, Field, PrivateAttr
from ..core.player.player import Player  
from ..core.game.snapshot import GameSnapshot

class RoundHandler:
    

    @staticmethod
    def get_current_round(snapshot: GameSnapshot) -> int:

        return snapshot.round_number

    @staticmethod
    def start_round(snapshot: GameSnapshot) -> GameSnapshot:

        new_snapshot = snapshot.model_copy(deep=True)

        new_snapshot.round_number += 1

        return new_snapshot
    
    @staticmethod
    def end_round(snapshot: GameSnapshot) -> GameSnapshot:

        pass

    @staticmethod
    def reset_round(snapshot: GameSnapshot) -> GameSnapshot:    

        new_snapshot = snapshot.model_copy(deep=True)

        new_snapshot.round_number = 0

        return new_snapshot
    
    @staticmethod
    def remove_player(snapshot: GameSnapshot, player: Player) -> GameSnapshot:

        new_snapshot = snapshot.model_copy(deep=True)
        
        for p in new_snapshot.players:
            if p.id == player.id:
                new_snapshot.players.remove(p)

                return new_snapshot
            
        raise ValueError("Player doesn't exist")

    @staticmethod
    def add_player(snapshot: GameSnapshot, player: Player) -> GameSnapshot:

        new_snapshot = snapshot.model_copy(deep=True)

        for p in new_snapshot.players:

            if p.id == player.id:

                raise ValueError("Player already in game")
            
        new_snapshot.players.append(player)

        return new_snapshot
    
    @staticmethod
    def total_players(snapshot: GameSnapshot) -> int:

        return len(snapshot.players)





