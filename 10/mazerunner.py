import re
import pathlib
from pathlib import Path
from enum import Enum
from source_code_final.src.maze_solver.models.border import Border
from source_code_final.src.maze_solver.models.square import Square
from source_code_final.src.maze_solver.models.maze import Maze
from source_code_final.src.maze_solver.view.renderer import SVGRenderer


class InputSymbol(Enum):
    P = Border.LEFT | Border.RIGHT # | now P for pipe
    D = Border.TOP | Border.BOTTOM # - now D for Dash
    L = Border.LEFT | Border.BOTTOM
    J = Border.BOTTOM | Border.RIGHT
    V = Border.TOP | Border.RIGHT # 7 now V for seVen
    F = Border.TOP | Border.LEFT
    Z = Border.EMPTY                # . now Z for zero
    # S =


if __name__ == "__main__":
    script_path = str(pathlib.Path(__file__).parent.resolve()) + "/"

    f = open(script_path + "input.txt", "r")
    f = open(script_path + "test_input.txt", "r")
    a = f.readline().strip()

    row = 0
    col = 0
    index = 0
    SQUARES = []
    while a:
        for char in a:
            char = 'P' if char == '|' else char
            char = 'D' if char == '-' else char
            char = 'V' if char == '7' else char
            char = 'Z' if char == '.' else char
            # print(char)
            SQUARES.append(Square(index, row, col, InputSymbol[char].value))
            index += 1
            col += 1

        a = f.readline().strip()
        row += 1
        col = 0
    pass

    maze = Maze(SQUARES)
    renderer = SVGRenderer()
    svg = renderer.render(maze)
    with Path("maze.svg").open(mode="w", encoding="utf-8") as file:
        file.write(svg.xml_content)