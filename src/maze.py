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
        win,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        for row in range(self.__num_rows):
            cells = []
            for col in range(self.__num_cols):
                x1 = self.__x1 + col * self.__cell_size_x
                y1 = self.__y1 + row * self.__cell_size_y
                x2 = x1 + self.__cell_size_x
                y2 = y1 + self.__cell_size_y
                cells.append(Cell(x1, y1, x2, y2, self.__win))
            self.__cells.append(cells)
        # draw cells
        for i in range(self.__num_rows):
            for j in range(self.__num_cols):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        cell_x = self.__x1 + j * self.__cell_size_x
        cell_y = self.__y1 + i * self.__cell_size_y
        self.__cells[i][j].__x1 = cell_x
        self.__cells[i][j].__y1 = cell_y
        self.__cells[i][j].__x2 = cell_x + self.__cell_size_x
        self.__cells[i][j].__y2 = cell_y + self.__cell_size_y
        self.__cells[i][j].draw()
        self.__animate()

    def __animate(self):
        self.__win.redraw()
        time.sleep(0.05)