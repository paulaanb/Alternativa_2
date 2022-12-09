import copy
import itertools
import re
import sys


def solve(board):
  if isinstance(board,list):
    board = Board(board)

  board.solve()

  if board.invalid: return None
  if board.solved: return board.board

  empty,empty_i = board.min_empty()

  for candidate in empty.candidates:
    guess = Board(board)
    guess.set_cell(empty,candidate,empty_i)

    solution = solve(guess)
    if solution is not None: return solution

  return None

# 1 = no candidato; 0 = candidato.
# El lugar del binario es el número, así que hay 9 lugares.
#
# Por ejemplo: 101 010 101
# 987 654 321
# Esto significa que [2,4,6,8] son candidatos para esta celda.