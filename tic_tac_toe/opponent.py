from move import BaseDecideMove
import math

from tic_tac_toe import TicTacToe, format_pos
from game import GameException, Player


class DecideMove(BaseDecideMove):

    def __init__(self):
        super().__init__(max_depth=6, max_white_score=1, min_black_score=-1)


    def moves_from(self, game: TicTacToe) -> list[TicTacToe]:
        games = []  # TODO
        return games


    def evaluate(self, game: TicTacToe) -> int:
        pass  # TODO


    def decide_best_move(self, game: TicTacToe):

        # black is the minimizing player
        if game.turn == Player.BLACK:
            best_score: int  = math.inf

            for i in range(9):
                if game.pieces[i] is not None:
                    continue

                # make a copy for minimax
                tmp = game.copy()
                tmp.pieces[i] = Player.BLACK
                tmp.turn = Player.WHITE

                # start up minimax!
                score = self.minimax(tmp)

                #print(f"Move {format_pos(i % 3, i // 3)} has score {score}")
                
                # track the best score!
                if score < best_score:
                    best_score = score
                    self.best_move = format_pos(i % 3, i // 3)

        else:

            best_score: int  = -math.inf
            for i in range(9):
                if game.pieces[i] is not None:
                    continue

                # make a copy for minimax
                tmp = game.copy()
                tmp.pieces[i] = Player.WHITE
                tmp.turn = Player.BLACK
                score = self.minimax(tmp)

                #print(f"Move {format_pos(i % 3, i // 3)} has score {score}")
                
                # track the best score!
                if score > best_score:
                    best_score = score
                    self.best_move = format_pos(i % 3, i // 3)
