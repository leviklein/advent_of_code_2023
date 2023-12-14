import re
from pathlib import Path
from itertools import groupby
from dataclasses import dataclass
from enum import IntEnum, auto
from itertools import product, combinations
from functools import cached_property, reduce
from typing import Iterator
import sys
import time

from multiprocessing import Pool


# sys.path.append(Path(__file__, "/../../lib"))
# sys.path.append(Path('/home/leviklein/repo/advent_of_code_2023/'))
# import levi_aoc_common

# from .levi_aoc_common import all_equal

def all_equal(iterable, value=None):
    g = groupby(iterable)
    if (value):
        return next(g, True) and not next(g, False) and iterable[0] == value

    return next(g, True) and not next(g, False)


class Kind(IntEnum):
    NONE = 0
    STAR = auto()

@dataclass(frozen=True)
class Coordinate:
    index: int
    row: int
    column: int
    kind: Kind = Kind.NONE


@dataclass(frozen=True)
class Sky:
    coordinates: tuple[Coordinate, ...]

    # @classmethod
    # def load(cls, path: Path) -> "Sky":
    #     return Sky(tuple(load_coordinates(path)))

    def __post_init__(self) -> None:
        validate_indices(self)
        validate_rows_columns(self)
        # validate_entrance(self)
        # validate_exit(self)

    def __iter__(self) -> Iterator[Coordinate]:
        return iter(self.coordinates)

    def __getitem__(self, index: int) -> Coordinate:
        return self.coordinates[index]

    @cached_property
    def width(self):
        return max(coord.column for coord in self) + 1

    @cached_property
    def height(self):
        return max(coord.row for coord in self) + 1

    # @cached_property
    # def entrance(self) -> Coordinate:
    #     return next(sq for sq in self if sq.role == Role.ENTRANCE)

    # @cached_property
    # def exit(self) -> Coordinate:
    #     return next(sq for sq in self if sq.role == Role.EXIT)

    # def dump(self, path: Path) -> None:
    #     dump_coordinates(self.width, self.height, self.coordinates, path)

    @cached_property
    def star_pairs(self) -> set[Coordinate]:
        return combinations([coord for coord in self.coordinates if coord.kind == Kind.STAR], 2)

def validate_indices(sky: Sky) -> None:
    assert [coord.index for coord in sky] == list(
        range(len(sky.coordinates))
    ), "Wrong coord.index"


def validate_rows_columns(sky: Sky) -> None:
    for y in range(sky.height):
        for x in range(sky.width):
            coord = sky[y * sky.width + x]
            assert coord.row == y, "Wrong coord.row"
            assert coord.column == x, "Wrong coord.column"


def validate_stars(sky: Sky) -> None:
    assert 0 < sum(
        1 for coord in sky if coord.kind == Kind.STAR
    ), "Must have at least 1 star"


# def validate_entrance(sky: Sky) -> None:
#     assert 1 == sum(
#         1 for coord in sky if coord.role == Role.ENTRANCE
#     ), "Must be exactly one entrance"


# def validate_exit(sky: Sky) -> None:
#     assert 1 == sum(
#         1 for coord in sky if coord.role == Role.EXIT
#     ), "Must be exactly one exit"

import math
from typing import NamedTuple, TypeAlias

import networkx as nx
Node: TypeAlias = Coordinate


class Edge(NamedTuple):
    node1: Node
    node2: Node

    @property
    def flip(self) -> "Edge":
        return Edge(self.node2, self.node1)

    @property
    def distance(self) -> float:
        return math.dist(
            (self.node1.row, self.node1.column),
            (self.node2.row, self.node2.column),
        )

    # def weight(self, bonus=1, penalty=2) -> float:
    #     match self.node2.role:
    #         case Role.REWARD:
    #             return self.distance - bonus
    #         case Role.ENEMY:
    #             return self.distance + penalty
    #         case _:
    #             return self.distance

def make_graph(sky: Sky) -> nx.Graph:
    return nx.Graph(
        (edge.node1, edge.node2, {"weight": edge.distance})
        for edge in get_edges(sky, get_nodes(sky))
    )

def get_nodes(sky: Sky) -> set[Node]:
    nodes: set[Node] = set()
    for coordinate in sky:
        nodes.add(coordinate)
    return nodes


def get_edges(sky: Sky, nodes: set[Node]) -> set[Edge]:
    edges: set[Edge] = set()
    for source_node in nodes:
        # Follow right:
        node = source_node
        for x in range(node.column + 1, sky.width):
            node = sky.coordinates[node.row * sky.width + x]
            if node in nodes:
                edges.add(Edge(source_node, node))
                break
        # Follow down:
        node = source_node
        for y in range(node.row + 1, sky.height):
            node = sky.coordinates[y * sky.width + node.column]
            if node in nodes:
                edges.add(Edge(source_node, node))
                break
    return edges


import datetime as dt
def print_every_n_seconds(t, seconds, line):
    delta = dt.datetime.now()-t
    if delta.seconds >= seconds:
        print(line)
    return delta.seconds >= seconds
t = dt.datetime.now()

def get_shortest_path_with_copying_g(star_pair):
    return len(nx.shortest_path(G, source=star_pair[0], target=star_pair[1])) - 1

if __name__ == "__main__":
    script_path = Path(__file__).parent
    f = open(script_path/"input.txt", "r")
    f = open(script_path/"test_input.txt", "r")
    a = [x.strip() for x in f.readlines()]
    width = len(a[0])

    IS_PART2 = True
    num_to_add = 1 if not IS_PART2 else 999999

    x_to_double = [x for x in range(len(a)) if all_equal(a[x], '.')]
    y_to_double = [y for y in range(len(a[0])) if all_equal(list(zip(*a))[y])]

    for x in x_to_double:
        for tmp in range(num_to_add):
            a.insert(x + x_to_double.index(x), '.'*width)

    length = len(a)
    for y in y_to_double:
        for x in range(length):
            position = y + y_to_double.index(y)
            line = '{0}{2}{1}'.format(a[x][:position], a[x][position:], '.'*(num_to_add))
            a[x] = line

    grid = a
    length = len(grid)
    width = len(grid[0])

    x = 0
    y = 0
    index = 0
    MY_COORDINATES = []
    for x,y in product(range(length), range(width)):
        char = grid[x][y]
        MY_COORDINATES.append(Coordinate(index, x, y, Kind.STAR if char == '#' else Kind.NONE))
        index += 1

    sky = Sky(MY_COORDINATES)
    print("sky generated")

    G = make_graph(sky)
    print("graph generated")

    paths = []
    star_pairs = [x for x in sky.star_pairs]
    print(f"found {len(star_pairs)} star_pairs")


    left = len(star_pairs)
    print(f"computing shortest paths. {left} remaining")
    answer1 = 0
    # for star_start, star_end in star_pairs:
    #     t = dt.datetime.now() if print_every_n_seconds(t, 5, f" computing shortest path between {star_start.index} and {star_end.index}. {left} remaining") else t

    #     paths.append(nx.shortest_path(G, source=star_start, target=star_end))

    #     left -= 1
    #     answer1 += len(paths[-1]) -1

    # ### with fxn
    # for i in star_pairs:
    #     paths.append(get_shortest_path_with_copying_g(i))

    #     left -= 1
    #     answer1 += len(paths[-1]) -1

    ### with multiprocessing
    start_t = time.perf_counter()
    with Pool() as pool:
        for res in pool.imap_unordered(get_shortest_path_with_copying_g, star_pairs, 100):
            answer1 += res
            t = dt.datetime.now() if print_every_n_seconds(t, 5, f" computing shortest path. {left} remaining") else t
            left -= 1
    end_t = time.perf_counter()
    duration = end_t - start_t
    print(f"it took: {duration:.4f}s")

    # answer1 = reduce(lambda a, b: a + b, [len(x)-1 for x in paths])
    print(f"answer1: {answer1}")
    pass