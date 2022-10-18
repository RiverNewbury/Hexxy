import logging

from rich import print
from rich.logging import RichHandler

FORMAT = "%(message)s"
logging.basicConfig(level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()])

from classes.tournament import Tournament


def main(args):
    arena = Tournament(args)

    if MODE == "cpu_vs_cpu":
        arena.championship()
    if MODE == "man_vs_cpu":
        arena.single_game(blue_starts=True)


if __name__ == "__main__":
    BOARD_SIZE = 7
    ITERMAX = 500
    MODES = {1:"man_vs_man", 2:"man_vs_cpu",3:"cpu_vs_cpu"}
    GAME_COUNT, N_GAMES = 0, 200

    print("What Mode do you want to play?\n 1. Man vs Man\n 2. Man vs CPU\n 3. CPU vs CPU\t", end="\t")
    MODE = MODES.get(int(input())) #TODO : Add erroring or something

    if MODE == "man_vs_man":
        raise Exception("Man vs man not implemented") 
    
    elif MODE == "man_vs_cpu":
        log = logging.getLogger("rich")

        print("What [bold blue]board size[/bold blue] do you want to play on?", end="\t")
        BOARD_SIZE = int(input())
        #print("How many iterations should MCTS play ([bold red]itermax[/bold red])?", end="\t")
        #ITERMAX = int(input())

        print()
        log.info("You will be playing as the BLUE player!")
        log.warning("No Pie Rule not implemented yet!")
        print() 


    args = BOARD_SIZE, ITERMAX, MODE, GAME_COUNT, N_GAMES
    main(args)
