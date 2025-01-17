import logging

from rich import print
from rich.logging import RichHandler

FORMAT = "%(message)s"
logging.basicConfig(level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()])

from game.tournament import Tournament
from player.allplayers import *


def main(args):
    arena = Tournament(args)
    if N_GAMES== 1:
        arena.single_game(blue_starts=True)
    else:
        arena.championship()
        

if __name__ == "__main__":
    PLAYER_DICTIONARY = {
        1: HumanPlayer(),
        2: RandomPlayer(),
    }
    PLAYERS_STR = """What is [bold blue]Player {}[/bold blue]?
     1. Human
     2. Random Player"""

    BOARD_SIZE = 7
    ITERMAX = 500
    GAME_COUNT, N_GAMES = 0, 200
    GUI = False

    print(PLAYERS_STR.format(1), end="\t")
    P1 = PLAYER_DICTIONARY.get(int(input())) #TODO : Add erroring or something

    print(PLAYERS_STR.format(2), end="\t")
    P2 = PLAYER_DICTIONARY.get(int(input())) #TODO : Add erroring or something

    
    log = logging.getLogger("rich")

    print("What [bold blue]board size[/bold blue] do you want to play on?", end="\t")
    BOARD_SIZE = int(input())

    print("How [bold blue]many games[/bold blue] do you want to play?", end="\t")
    N_GAMES = int(input())
    #print("How many iterations should MCTS play ([bold red]itermax[/bold red])?", end="\t")
    #ITERMAX = int(input())

    print("Do you want a [bold blue]GUI[/bold blue]?", end="\t")
    GUI = True if input() == "yes" else False

    print()
    log.warning("No Pie Rule not implemented yet!")
    print() 


    args = BOARD_SIZE, ITERMAX, P1, P2, GAME_COUNT, N_GAMES, GUI
    main(args)
