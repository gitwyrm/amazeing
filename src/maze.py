import random
import time
from cell import Cell


class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed = None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed is not None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        """
        Recursive function to break walls between cells
        """
        self._cells[i][j].visited = True
        self._draw_cell(i, j)
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            new_i = i + dx
            new_j = j + dy
            if new_i < 0 or new_i >= self._num_cols or new_j < 0 or new_j >= self._num_rows:
                continue
            if self._cells[new_i][new_j].visited:
                continue
            if dx == 1:
                self._cells[i][j].has_right_wall = False
                self._cells[new_i][new_j].has_left_wall = False
            elif dx == -1:
                self._cells[i][j].has_left_wall = False
                self._cells[new_i][new_j].has_right_wall = False
            elif dy == 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[new_i][new_j].has_top_wall = False
            elif dy == -1:
                self._cells[i][j].has_top_wall = False
                self._cells[new_i][new_j].has_bottom_wall = False
            self._draw_cell(i, j)
            self._draw_cell(new_i, new_j)
            self._animate()
            self._break_walls_r(new_i, new_j)

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        """
        Solve the maze using a depth-first search algorithm
        """
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        """
        Recursive function to solve the maze
        """
        self._cells[i][j].visited = True
        self._draw_cell(i, j)
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            new_i = i + dx
            new_j = j + dy
            if new_i < 0 or new_i >= self._num_cols or new_j < 0 or new_j >= self._num_rows:
                continue
            if self._cells[new_i][new_j].visited:
                continue
            if dx == 1 and not self._cells[i][j].has_right_wall:
                if self._solve_r(new_i, new_j):
                    self._cells[i][j].draw_move(self._cells[new_i][new_j])
                    self._animate()
                    return True
            elif dx == -1 and not self._cells[i][j].has_left_wall:
                if self._solve_r(new_i, new_j):
                    self._cells[i][j].draw_move(self._cells[new_i][new_j])
                    self._animate()
                    return True
            elif dy == 1 and not self._cells[i][j].has_bottom_wall:
                if self._solve_r(new_i, new_j):
                    self._cells[i][j].draw_move(self._cells[new_i][new_j])
                    self._animate()
                    return True
            elif dy == -1 and not self._cells[i][j].has_top_wall:
                if self._solve_r(new_i, new_j):
                    self._cells[i][j].draw_move(self._cells[new_i][new_j])
                    self._animate()
                    return True
        return False