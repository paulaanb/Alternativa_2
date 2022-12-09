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
class Board:
  def __init__(self,board):
    self.board = None
    self.cached_hash = None
    self.empties = []

    self.bit_blocks = []
    self.bit_columns = []
    self.bit_rows = []

    self.invalid = False
    self.solved = False
    self.solved_cell = False

    if isinstance(board,list):
      self.board = copy.deepcopy(board)

      for i in range(9):
        self.bit_blocks.append(0)
        self.bit_columns.append(0)
        self.bit_rows.append(0)

      for y in range(9):
        for x in range(9):
          num = self.board[y][x]

          if num == 0:
            self.empties.append(Cell(x,y))
          else:
            bit_num = 1 << (num - 1)

            self.bit_blocks[self.block_i(x,y)] |= bit_num
            self.bit_columns[x] |= bit_num
            self.bit_rows[y] |= bit_num
    else:
      self.board = copy.deepcopy(board.board)
      self.cached_hash = board.cached_hash
      self.empties = copy.deepcopy(board.empties)

      for i in range(9):
        self.bit_blocks.append(copy.deepcopy(board.bit_blocks[i]))
        self.bit_columns.append(copy.deepcopy(board.bit_columns[i]))
        self.bit_rows.append(copy.deepcopy(board.bit_rows[i]))

  def __eq__(self,other):
    return self.board == other.board

  def __hash__(self):
    if self.cached_hash is None:
      self.cached_hash = hash(tuple(itertools.chain.from_iterable(self.board)))
    return self.cached_hash

# Usado para conjeturas/backtracking.
  def block_empty_count(self,x,y):
    bit_block = self.bit_block(x,y)
    count = 0

    for i in range(9):
      if (bit_block & (1 << i)) == 0:
        count += 1

    return count

  def end_solve(self):
    return self.invalid or self.solved

  # Usado para conjeturas/backtracking.
  def min_empty(self):
    min_cell = None
    min_count = 11
    min_index = -1

    for i,cell in enumerate(self.empties):
      self.sole_candidate(cell)
      count = self.block_empty_count(cell.x,cell.y)

      if count < min_count:
        min_cell = cell
        min_count = count
        min_index = i

    return (min_cell,min_index)

  def sole_candidate(self,cell):
    cell.bit_candidates |= self.bit_block(cell.x,cell.y)
    cell.bit_candidates |= self.bit_columns[cell.x]
    cell.bit_candidates |= self.bit_rows[cell.y]

    return cell.sole_candidate()

  def solve(self):
    while True:
      self.solved_cell = False

      if self.solve_sole_candidates().end_solve(): return
      if self.solve_unique_candidates().end_solve(): return

      if not self.solved_cell: break

  def solve_cell(self,cell,index=None):
    if cell.bit_candidates == Cell.NO_BIT_CANDIDATES:
      self.invalid = True
      self.solved = False
      return False

    candidate = self.sole_candidate(cell)

    if candidate > 0:
      self.set_cell(cell,candidate,index)
      self.solved_cell = True
      return True

    return False

  def solve_sole_candidates(self):
    self.solved = True

    i = 0 # Dentro del bucle, podríamos borrar vacíos
    while i < len(self.empties):
      cell = self.empties[i]

      if self.solve_cell(cell,i): continue
      if self.invalid: return self

      self.solved = False
      i += 1

    return self

  def solve_unique_candidates(self):
    block_uniques = Uniques()
    column_uniques = Uniques()
    row_uniques = Uniques()

    for i in range(Uniques.MAX_UNIQUES):
      block_uniques.init()
      column_uniques.init()
      row_uniques.init()

      for j in range(9):
        block_uniques.init_group(i)
        column_uniques.init_group(i)
        row_uniques.init_group(i)

    for cell in self.empties:
      self.sole_candidate(cell)

      for i in range(Uniques.MAX_UNIQUES):
        block_group = block_uniques.group(i,self.block_i(cell.x,cell.y))
        column_group = column_uniques.group(i,cell.x)
        row_group = row_uniques.group(i,cell.y)

        for combo in itertools.combinations(cell.candidates,i + 1):
          block_group.add_combo(combo,cell)
          column_group.add_combo(combo,cell)
          row_group.add_combo(combo,cell)

    if block_uniques.eliminate_candidates(): self.solved_cell = True
    if column_uniques.eliminate_candidates(): self.solved_cell = True
    if row_uniques.eliminate_candidates(): self.solved_cell = True

    return self

  def set_cell(self,cell,num,index=None):
    bit_num = 1 << (num - 1)

    self.bit_blocks[self.block_i(cell.x,cell.y)] |= bit_num
    self.bit_columns[cell.x] |= bit_num
    self.bit_rows[cell.y] |= bit_num
    self.board[cell.y][cell.x] = num
    self.cached_hash = None

    if index is None:
      try:
        self.empties.remove(cell)
      except ValueError:
        pass
    else:
      try:
        del self.empties[index]
      except IndexError:
        pass

  def bit_block(self,x,y):
    return self.bit_blocks[self.block_i(x,y)]

  def block_i(self,x,y):
    return x // 3 + (y // 3 * 3)

  # Usé esto para depurar candidatos únicos.
  def print_candidates(self,title=None):
    if title is not None: print(title)

    candidates = [['---' for x in range(9)] for y in range(9)]
    max_len = 3 # Debe ser > 0

    for cell in self.empties:
      candidates[cell.y][cell.x] = ''.join(map(str,sorted(cell.candidates)))
      candidates_len = len(cell.candidates)

      if candidates_len > max_len: max_len = candidates_len

    for y in range(9):
      for x in range(9):
        print('{:{}s}'.format(candidates[y][x],max_len),end=' ')
        if ((x + 1) % 3) == 0: print(end=' ')

      print()
      if ((y + 1) % 3) == 0: print()

class UniqueCombo:
  def __init__(self):
    self.cells = []
    self.count = 0
