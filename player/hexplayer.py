description = """{-
Module      : HexPlayer
Description : Defines the abstract class of a game player
Maintainer  : River
-}"""

#-------- Imports ---------------------------------------------------------------

from abc import ABC, abstractmethod

from game.board import Board

#-------- Classes ---------------------------------------------------------------

class HexPlayer(ABC):
	@abstractmethod
	def getMove(self, board: Board) -> tuple[int, int]:
		pass;

#-------- Datatypes -------------------------------------------------------------

#-------- Destructors -----------------------------------------------------------

#-------- Helper Functions ------------------------------------------------------

#-------- Main Functions --------------------------------------------------------

if __name__ == "__main__":
	print(description)