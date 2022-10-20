description = """{-
Module      : 
Description : 
Maintainer  : River
-}"""


#-------- Imports ---------------------------------------------------------------

import sys

import pygame
from rich.console import Console
from rich.table import Table

from game.ui import UI
from game.board import Board
from player.hexplayer import HexPlayer

#-------- Classes ---------------------------------------------------------------

class Game:
    def __init__(self, boardSize: int, bluePlayer : HexPlayer, redPlayer : HexPlayer, showGui = True, blueToStart: bool = True):

        # Instantiate classes
        self.ui = UI(boardSize) if showGui else None
        self.board = Board(boardSize)

        # Initialize players
        self.bluePlayer = bluePlayer
        self.redPlayer  = redPlayer
        
        if bluePlayer.type == "human" : bluePlayer.gui = self.ui; assert(showGui)
        if redPlayer.type == "human"  : redPlayer.gui  = self.ui; assert(showGui)

        # Initialize variables
        self.node = None
        self.showGui = showGui
        self.winner = 0
        self.turn = {True: self.board.BLUE_PLAYER, False: self.board.RED_PLAYER}

        # BLUE player starts
        self.turn_state = blueToStart

    def get_game_info(self, args):
        console = Console()

        table = Table(title="Hex Game", show_header=True, header_style="bold magenta")
        table.add_column("Parameters", justify="center")
        table.add_column("Value", justify="right")
        table.add_row("Board size", str(args[0]))
        table.add_row("Player 1", str(args[1].type))
        table.add_row("Player 2", str(args[2].type))
        table.add_row("Game", str(args[3]))

        console.print(table)

    def get_winner(self):
        if self.winner:
            print("----------------- Player {} wins! -------------------------------------".format(self.winner))
            return True

    def play(self):
        if self.showGui: self.ui.draw_board()

        if self.turn_state:
            node = self.bluePlayer.getMove(self.board)
        else:
            node = self.redPlayer.getMove(self.board)

        if node != None:
            #print(node)
            self.board.play(cords=node, player=self.turn[self.turn_state])
            if self.showGui: self.ui.color[node[0] * self.board.boardSize + node[1]] = self.ui.blue if self.turn_state else self.ui.red
            self.is_game_over()
            self.get_winner()
            self.turn_state = not self.turn_state

        if self.showGui:
            pygame.display.update()
            self.ui.clock.tick(30)


    def is_game_over(self):
        """
        Sets GAME_OVER to True if there are no more moves to play.
        Returns the winning player.
        """
        player = self.turn[self.turn_state]
        for _ in range(self.board.boardSize):
            if player == self.board.BLUE_PLAYER:
                border = (_, 0)
            if player == self.board.RED_PLAYER:
                border = (0, _)

            path = self.traverse(border, player, {})
            if path:
                self.board.updateWinningPath(path, player)
                return;

    def traverse(self, node: tuple, player: int, visited: dict):
            neighbours = self.board.getNeighbours(node)

            try:
                if visited[node]:
                    pass
            except KeyError:
                if self.board.get(node) == player:
                    visited[node] = 1

                    if self.board.isBorder(node, player):
                        self.winner = player

                    for neighbour in neighbours:
                        self.traverse(neighbour, player, visited)

            if self.winner:
                return visited

#-------- Datatypes -------------------------------------------------------------

#-------- Destructors -----------------------------------------------------------

#-------- Helper Functions ------------------------------------------------------

#-------- Main Functions --------------------------------------------------------

if __name__ == "__main__":
    print(description)