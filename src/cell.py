from line import Line
from point import Point
from window import Window


class Cell():
    def __init__(self, window: Window=None):
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = window
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        line = Line(Point(x1, y1), Point(x1, y2))
        if self.has_left_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, "white")
        line = Line(Point(x1, y1), Point(x2, y1))
        if self.has_top_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, "white")
        line = Line(Point(x2, y1), Point(x2, y2))
        if self.has_right_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, "white")
        line = Line(Point(x1, y2), Point(x2, y2))
        if self.has_bottom_wall:
            self._win.draw_line(line)
        else:
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        """
        Draw a move between two cells, a line should go from the center of one cell to the center of the other
        
        If undo is True, the line is drawn red, otherwise green
        """
        if self._win is None:
            return
        color = "red" if undo else "green"
        cell_size_x = self._x2 - self._x1
        cell_size_y = self._y2 - self._y1
        self._win.draw_line(Line(Point(self._x1 + cell_size_x/2, self._y1 + cell_size_y/2), Point(to_cell._x1 + cell_size_x/2, to_cell._y1 + cell_size_y/2)), color)