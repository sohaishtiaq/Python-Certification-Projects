from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]
    
    def make_move(self):
        move = random.choice(self.moves)
        new_position = (self.position[0] + move[0], self.position[1] + move[1])
        self.position = new_position
        self.path.append(self.position)
        return self.position

    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [(1,0), (-1,0), (0,1), (0,-1)]

    def level_up(self):
        new_moves = [(1,1), (1,-1), (-1,1), (-1,-1)]
        self.moves += new_moves
