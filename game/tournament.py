import os
import pickle

# Hide Pygame welcome message
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

from game.game import Game

import pandas as pd
from trueskill import Rating, rate_1vs1


class Tournament:
    def __init__(self, args):
        self.args = args

        self.BOARD_SIZE = args[0]
        self.ITERMAX = args[1]
        self.P1 = args[2]
        self.P2 = args[3]
        self.GAME_COUNT = args[4]
        self.N_GAMES = args[5]
        self.GUI = args[6]

    def single_game(self, blue_starts: bool = True) -> int:
        pygame.init()
        pygame.display.set_caption("Hex")

        game = Game(boardSize=self.BOARD_SIZE, bluePlayer = self.P1, redPlayer = self.P2, 
                    showGui=self.GUI)
        game.get_game_info([self.BOARD_SIZE, self.P1, self.P2, self.GAME_COUNT])
        while not game.winner:
            game.play()
        return game.winner

    def championship(self):
        # r1 (BLUE) r2 (RED)
        r1, r2 = Rating(), Rating()

        blue_mu, red_mu = [], []
        blue_sigma, red_sigma = [], []

        for _ in range(self.N_GAMES):
            self.GAME_COUNT = _

            # First half of the tournament played by one player
            # Remaining half played by other player (see "no pie rule")
            if self.GAME_COUNT < self.N_GAMES / 2:
                blue_starts = True
            if self.GAME_COUNT >= self.N_GAMES / 2:
                blue_starts = False
            winner = self.single_game(blue_starts=blue_starts)

            if winner == 1:
                r1, r2 = rate_1vs1(r1, r2)
            if winner == 2:
                r2, r1 = rate_1vs1(r2, r1)

            blue_mu.append(r1.mu)
            blue_sigma.append(r1.sigma)
            red_mu.append(r2.mu)
            red_sigma.append(r2.sigma)

            print("Blue Rating" + str(r1))
            print("Red Rating " + str(r2))

        df = pd.DataFrame.from_dict({"blue_mu": blue_mu, "red_mu": red_mu,
                                     "blue_sigma": blue_sigma, "red_sigma": red_sigma})

        print("Final Blue Rating" + str(r1))
        print("Final Red Rating " + str(r2))


        data_path = "data"
        if not os.path.exists(data_path):
            os.makedirs(data_path)

        with open(data_path + "\s{}-i{}-g{}.pkl".format(self.args[0], self.args[1], self.args[4]), "wb") as file:
            pickle.dump(df, file)
