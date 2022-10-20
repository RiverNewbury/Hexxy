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
        1: HumanPlayer()
    }

    BOARD_SIZE = 7
    ITERMAX = 500
    GAME_COUNT, N_GAMES = 0, 200

    print("What is [bold blue]Player 1[/bold blue]?\n 1. Human\n 2. Random Player", end="\t")
    P1 = PLAYER_DICTIONARY.get(int(input())) #TODO : Add erroring or something

    print("What is [bold blue]Player 2[/bold blue]?\n 1. Human\n 2. Random Player", end="\t")
    P2 = PLAYER_DICTIONARY.get(int(input())) #TODO : Add erroring or something

    
    log = logging.getLogger("rich")

    print("What [bold blue]board size[/bold blue] do you want to play on?", end="\t")
    BOARD_SIZE = int(input())

    print("How [bold blue]many games[/bold blue] do you want to play?", end="\t")
    N_GAMES = int(input())
    #print("How many iterations should MCTS play ([bold red]itermax[/bold red])?", end="\t")
    #ITERMAX = int(input())

    print()
    log.warning("No Pie Rule not implemented yet!")
    print() 


    args = BOARD_SIZE, ITERMAX, P1, P2, GAME_COUNT, N_GAMES
    main(args)
