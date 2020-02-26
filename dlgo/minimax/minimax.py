import enum
import random
from dlgo.agent import Agent

__all__ = ['MinimaxAgent',]


# tag::gameresult-enum[]
class GameResult(enum.Enum):
    loss = 1
    draw = 2
    win = 3

