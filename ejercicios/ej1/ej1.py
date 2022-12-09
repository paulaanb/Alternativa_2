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

class Cell:
  ALL_BIT_CANDIDATES = 0
  NO_BIT_CANDIDATES = 511 # 111111111

  def __init__(self,x,y):
    self.bit_candidates = self.ALL_BIT_CANDIDATES
    self.candidates = set()
    self.x = x
    self.y = y

  def __eq__(self,other):
    return self.x == other.x and self.y == other.y

  def __hash__(self):
    return hash((x,y))

  def sole_candidate(self):
    self.candidates = set()
    result = 0

    for i in range(9):
      if (self.bit_candidates & (1 << i)) == 0:
        self.candidates.add(i + 1)

    if len(self.candidates) == 1:
      for result in self.candidates: break

    return result
