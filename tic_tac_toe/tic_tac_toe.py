from __future__ import annotations

from typing import Optional
from enum import Enum
import re

from game import Game, State, Player, GameException


# Change to False if you use a light terminal
TERMINAL_DARK = True

MAX_COORD = 2

def parse_pos(pos: str) -> tuple[int, int]:
    """Convert from a string representation to (x, y)"""
    x = ord(pos[0]) - ord("a")
    y = ord(pos[1]) - ord("1")
    if x < 0 or x > MAX_COORD or y < 0 or y > MAX_COORD:
        raise GameException(f"Invalid position {pos}.")
    return x, y


def format_pos(pos_x: int, pos_y: int) -> str:
    """Convert from (x, y) to the chess coordinate system."""
    x = chr(pos_x + ord("a"))
    y = chr(pos_y + ord("1"))
    return f"{x}{y}"


def piece_str(player: Player):
    """Get the unicode piece"""
    match player:
        case Player.WHITE:
            return "●" if TERMINAL_DARK else "○"
        case Player.BLACK:
            return "○" if TERMINAL_DARK else "●"
        case None:
            return " "

        
class TicTacToe(Game):
    """An implementation of Tic tac toe."""
    
    def __init__(self):
        self.pieces: list[Optional[Player]] = [None] * 9
        self.turn = Player.WHITE
        self.state : State = State.IN_PROGRESS

        
    def __str__(self):
        return f"turn={self.turn} board=[{''.join(map(str, self.pieces))}]"

    def print(self):
        if self.turn == Player.BLACK: 
            black_token = "○" if TERMINAL_DARK else "●"
            white_token = " "
        else:
            white_token = "●" if TERMINAL_DARK else "○"
            black_token = " "

        print(f"  ╔═══════════╗ {black_token}")
        print(f"3 ║ {piece_str(self.pieces[6])} │ {piece_str(self.pieces[7])} │ {piece_str(self.pieces[8])} ║")
        print(f"  ║───┼───┼───║")
        print(f"2 ║ {piece_str(self.pieces[3])} │ {piece_str(self.pieces[4])} │ {piece_str(self.pieces[5])} ║")
        print(f"  ║───┼───┼───║")
        print(f"1 ║ {piece_str(self.pieces[0])} │ {piece_str(self.pieces[1])} │ {piece_str(self.pieces[2])} ║")
        print(f"  ╚═══════════╝ {white_token}")
        print(f"    a   b   c")

        
    def is_over(self) -> bool:
        """Determine if a game is over."""

        if self.state == State.IN_PROGRESS:

            winner = None
            if self.pieces[0] is not None and self.pieces[0] == self.pieces[1] and self.pieces[1] == self.pieces[2]:
                winner = self.pieces[0]
            if self.pieces[3] is not None and self.pieces[3] == self.pieces[4] and self.pieces[4] == self.pieces[5]:
                winner = self.pieces[3]
            if self.pieces[6] is not None and self.pieces[6] == self.pieces[7] and self.pieces[7] == self.pieces[8]:
                winner = self.pieces[6]
            if self.pieces[0] is not None and self.pieces[0] == self.pieces[3] and self.pieces[3] == self.pieces[6]:
                winner = self.pieces[0]
            if self.pieces[1] is not None and self.pieces[1] == self.pieces[4] and self.pieces[4] == self.pieces[7]:
                winner = self.pieces[1]
            if self.pieces[2] is not None and self.pieces[2] == self.pieces[5] and self.pieces[5] == self.pieces[8]:
                winner = self.pieces[2]
            if self.pieces[0] is not None and self.pieces[0] == self.pieces[4] and self.pieces[4] == self.pieces[8]:
                winner = self.pieces[0]
            if self.pieces[2] is not None and self.pieces[2] == self.pieces[4] and self.pieces[4] == self.pieces[6]:
                winner = self.pieces[2]

            if winner and winner == Player.WHITE:
                self.state = State.WHITE_WIN
            if winner and winner == Player.BLACK:
                self.state = State.BLACK_WIN

            if all(p is not None for p in self.pieces):
                self.state = State.DRAW

        return not self.state


    def move(self, move_str: str):

        if not self.state:
            raise GameException("The game is over.")

        x, y = parse_pos(move_str)
        index = y * 3 + x
        
        if self.pieces[index]:
            raise GameException(f"There is a piece at position {move_str}")

        self.pieces[index] = self.turn

        # progress to next player's turn
        if self.state:
            self.turn = Player.BLACK if self.turn == Player.WHITE else Player.WHITE


    def copy(self) -> TicTacToe:
        tmp: TicTacToe = TicTacToe()
        tmp.pieces = self.pieces.copy()
        tmp.turn = self.turn
        tmp.state = self.state
        return tmp


