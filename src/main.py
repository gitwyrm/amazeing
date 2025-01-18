from line import Line
from point import Point
from window import Window
from cell import Cell


def main():
    win = Window(800, 600)
    cells = [
        Cell(0, 0, 100, 100, win),
        Cell(100, 0, 200, 100, win),
        Cell(200, 0, 300, 100, win),
        Cell(300, 0, 400, 100, win),
    ]
    cells[2].has_bottom_wall = False

    for cell in cells:
        cell.draw()

    win.wait_for_close()

if __name__ == "__main__":
    main()