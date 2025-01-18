from line import Line
from point import Point
from window import Window


def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(10, 10), Point(100, 100)))
    win.draw_line(Line(Point(10, 100), Point(100, 10)), "red")
    win.wait_for_close()

if __name__ == "__main__":
    main()