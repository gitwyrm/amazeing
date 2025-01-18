from line import Line
from point import Point
from window import Window


class Cell():
    def __init__(self, x1, y1, x2, y2, window: Window):
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__win = window

    def draw(self):
        if self.has_left_wall:
            self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)))
        if self.has_top_wall:
            self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)))
        if self.has_right_wall:
            self.__win.draw_line(Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)))
        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)))

    def draw_move(self, to_cell, undo=False):
        """
        Draw a move between two cells, a line should go from the center of one cell to the center of the other
        
        If undo is True, the line is drawn gray, otherwise red
        """
        color = "gray" if undo else "red"
        self.__win.draw_line(Line(Point(self.__x1 + 50, self.__y1 + 50), Point(to_cell.__x1 + 50, to_cell.__y1 + 50),), color)
        