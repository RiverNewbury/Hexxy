description = """{-
Module      : Random Player
Description : Describes the Hex Player which acts completely randomly
Maintainer  : River
-}"""


#-------- Imports ---------------------------------------------------------------
from random import randint

from player.hexplayer import HexPlayer, Board

#-------- Classes ---------------------------------------------------------------

class RandomPlayer(HexPlayer):
    type = "random"
    
    def getMove(self, board: Board) -> tuple[int, int]:
        poss = board.getPossibleMoves()
        move = randint(0,len(poss) - 1)
        return poss[move]


#-------- Datatypes -------------------------------------------------------------

#-------- Destructors -----------------------------------------------------------

#-------- Helper Functions ------------------------------------------------------

#-------- Main Functions --------------------------------------------------------

if __name__ == "__main__":
    print(description)