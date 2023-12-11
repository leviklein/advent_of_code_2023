import re
import pathlib
from pathlib import Path
from enum import Enum
from source_code_final.src.maze_solver.models.border import Border
from source_code_final.src.maze_solver.models.square import Square
from source_code_final.src.maze_solver.models.maze import Maze
from source_code_final.src.maze_solver.models.role import Role
from source_code_final.src.maze_solver.view.renderer import SVGRenderer
from source_code_final.src.maze_solver.graphs.converter import make_graph
import networkx as nx


class InputBorder(Enum):
    P = Border.LEFT | Border.RIGHT # | now P for pipe
    D = Border.TOP | Border.BOTTOM # - now D for Dash
    L = Border.LEFT | Border.BOTTOM
    J = Border.BOTTOM | Border.RIGHT
    V = Border.TOP | Border.RIGHT # 7 now V for seVen
    F = Border.TOP | Border.LEFT
    G = Border.TOP | Border.LEFT | Border.BOTTOM | Border.RIGHT # . now G for Ground
    S = Border.EMPTY

class InputRole(Enum):
    A = Role.NONE
    G = Role.WALL # . now G for Ground
    S = Role.ENTRANCE
    P = Role.NONE
    D = Role.NONE
    L = Role.NONE
    J = Role.NONE
    V = Role.NONE
    F = Role.NONE

    @classmethod
    def _missing_(cls, value):
        return cls.A

    # @classmethod
    # def __getitem__(self, name):
    #     try:
    #         return super().__getitem__(name)
    #     except (ValueError, KeyError) as error:
    #         return super().__getitem__('A')

def print_list(list):
    for line in list:
        print(line)

def find_max_list(list):
    # return lengths(list)
    # return max(list_len)
    max_length = 0
    max_i = 0
    for i in range(len(list)):
        if len(list[i]) > max_length:
            max_length = len(list[i])
            max_i = i
    return max_length, max_i

def lengths(x):
    if isinstance(x,list):
        yield len(x)
        for y in x:
            yield from lengths(y)

def get_adjacent_square_borders(square, direction, width):
    index = {
        "TOP":    ((square.row-1) * width) + square.column,
        "BOTTOM": ((square.row+1) * width) + square.column,
        "LEFT":   (square.row * width) + (square.column-1),
        "RIGHT":  (square.row * width) + (square.column+1)
    }
    default = Border.TOP | Border.LEFT | Border.BOTTOM | Border.RIGHT
    idx = index[direction]
    if idx < 0:
        return default
    try:
        return MY_SQUARES[idx].border
    except:
        return default

class AdjacentBorder(Enum):
    TOP = Border.BOTTOM
    LEFT = Border.RIGHT
    BOTTOM = Border.TOP
    RIGHT = Border.LEFT

def fix_squares(width):
    for i in MY_SQUARES:
        new_border = i.border
        new_role = i.role
        for dir in ("TOP", "BOTTOM", "LEFT", "RIGHT"):
            if get_adjacent_square_borders(i, dir, width) & AdjacentBorder[dir].value:
                new_border = new_border | Border[dir]
        if new_border.box:
            new_role = Role.WALL

        if(new_border != i.border or new_role != i.role):
            new_square = Square(i.index, i.row, i.column, new_border, new_role)
            MY_SQUARES[i.index] = new_square



def render_maze(maze, solution=None):
    svg = SVGRenderer().render(maze, solution)
    file_loc = write_to_file("maze.svg", svg.xml_content)
    print(f"saved maze svg to: {file_loc}")


def write_to_file(filename, data):
    with Path(filename).open(mode="w", encoding="utf-8") as file:
        file.write(data)
        print(f"saved to: {filename}")
    return filename

if __name__ == "__main__":
    script_path = str(pathlib.Path(__file__).parent.resolve()) + "/"

    f = open(script_path + "input.txt", "r")
    # f = open(script_path + "test_input.txt", "r")
    a = f.readline().strip()

    row = 0
    col = 0
    width = 0
    index = 0
    MY_SQUARES = []
    while a:
        for char in a:
            char = 'P' if char == '|' else char
            char = 'D' if char == '-' else char
            char = 'V' if char == '7' else char
            char = 'G' if char == '.' else char
            # print(char)
            MY_SQUARES.append(Square(index, row, col, InputBorder[char].value, InputRole[char].value))
            index += 1
            col += 1

        width = col
        a = f.readline().strip()
        row += 1
        col = 0
    pass

    fix_squares(width)
    maze = Maze(squares=MY_SQUARES)
    print("maze created")
    render_maze(maze)
    G = make_graph(maze)
    print("graph created")

    H = G.copy()
    # H.remove_edges_from(nx.selfloop_edges(G))
    cycle_basis = nx.cycle_basis(G, root=maze.entrance)
    loops = [x for x in cycle_basis]
    with Path("cycles.txt").open(mode="w", encoding="utf-8") as file:
        for line in loops:
            file.write(str(line))
            file.write('\n')

    # print(maze.entrance)
    final_loops = []
    for loop in loops:
        if maze.entrance in loop:
            final_loops.append(loop)

    max_length, index = find_max_list(final_loops)
    solution = final_loops[index]
    endpoint_index = int((len(solution)+1)/2)
    # solution = solution[:6]
    solution = solution[-1:] + solution
    max_length = nx.path_weight(
                    G,
                    path=solution,
                    weight="weight",
                )

    render_maze(maze, solution)

    print(f"max_length: {max_length}")
    print(f"answer1: {max_length/2}")
    write_to_file("solution.txt", str(solution))



