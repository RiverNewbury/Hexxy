description = """{-
Module      : 
Description : 
Maintainer  : River
-}"""


#-------- Imports ---------------------------------------------------------------
import sys

import pygame

from player.hexplayer import HexPlayer, Board


#-------- Classes ---------------------------------------------------------------

class HumanPlayer(HexPlayer):
    type = "human"
    gui = None


    def getMove(self, board: Board) -> tuple[int, int]:
        node = self.gui.get_node_hover()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                return self.check_move(node, board)
                     

    def check_move(self, node, board):
        # Forbid playing on already busy node
        x, y = self.gui.get_true_coordinates(node)
        if board.canPlay((x,y)):
            return (x,y)
        else: return None

#-------- Datatypes -------------------------------------------------------------

#-------- Destructors -----------------------------------------------------------

#-------- Helper Functions ------------------------------------------------------

#-------- Main Functions --------------------------------------------------------

if __name__ == "__main__":
    print(description)