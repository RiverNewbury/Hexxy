description = """{-
Module      : Board
Description : Defines the board and all access that needs to be done on it; it 
                enforces the physical invariants of the board (i.e. can't have
                2 pieces on same place on board)
Maintainer  : River
-}"""

#-------- Imports ---------------------------------------------------------------

import numpy as np

#-------- Classes ---------------------------------------------------------------

class Board:
    def __init__(self, boardSize: int):
        self.boardSize = boardSize
        self.board = np.zeros(shape=(self.boardSize, self.boardSize), dtype=np.int8)
        
        # Players
        self.BLUE_PLAYER = 1
        self.RED_PLAYER = 2
    
    # Returns whatever's in board(i)(j) - so i is the row and j is the col TODO : ?
    # PRE : isValid(i,j)
    def get(self, cords) -> int:
        i,j = cords
        return self.board[i][j];

    # Updates board[i][j] to be l
    def update(self, cords: tuple[int, int], l:int) -> None:
        i,j = cords
        self.board[i][j] = l

    # Returns if board[i][j] == 0
    # PRE : isValid(i,j)
    def canPlay(self, cords: tuple[int, int]) -> bool:
        return self.get(cords) == 0;



    # Plays a piece in i,j and updates turn
    # PRE : isValid(i,j)
    #    && canPlay(i,j)
    def play(self, cords: tuple[int, int], player: int):
        assert(self.canPlay(cords))

        # Play Move
        if player == self.BLUE_PLAYER:
            self.update(cords, self.BLUE_PLAYER)
        elif player == self.RED_PLAYER:
            self.update(cords, self.RED_PLAYER)

    # Returns all possitions (i,j) s.t. canPlay(i,j)
    def getPossibleMoves(self):
        x, y = np.where(self.board == 0)
        free_coordinates = [(i, j) for i, j in zip(x, y)]

        return free_coordinates


    # Returns all neighbouring hexes to i,j
    # PRE : isValid(i,j)
    def getNeighbours(self, cords: tuple[int, int]):
        i,j = cords
        neighbours = []
        for row in range(-1, 2):
            for col in range(-1, 2):
                if row != col:
                    if self.isValid((i + row, j + col)):
                        neighbours.append((i + row, j + col))

        return neighbours

    # Returns if i,j is a valid board possition
    def isValid(self, cords: tuple[int, int]):
        return all(0 <= _ < self.boardSize for _ in cords) 

    def isBorder(self, cords: tuple[int, int], player: int) -> bool:
        x, y = cords
        if player == self.BLUE_PLAYER:
            if y == self.boardSize - 1:
                return True
        elif player == self.RED_PLAYER:
            if x == self.boardSize - 1:
                return True
        return False;

    def updateWinningPath(self, cordss: list[tuple[int, int]], player: int):
        for cords in cordss:
            self.update(cords, player+2)

#-------- Datatypes -------------------------------------------------------------

#-------- Destructors -----------------------------------------------------------

#-------- Helper Functions ------------------------------------------------------

#-------- Main Functions --------------------------------------------------------

if __name__ == "__main__":
    print(description)

