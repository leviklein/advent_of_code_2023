from pathlib import Path
from itertools import groupby
from dataclasses import dataclass
from enum import IntEnum, auto
from itertools import product, combinations
from functools import cached_property
from typing import Iterator
import time

from multiprocessing import Pool


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

    def distance(self, other) -> int:
        return (abs(self.row - other.row) + abs(self.column - other.column))


@dataclass(frozen=True)
class Sky:
    coordinates: tuple[Coordinate, ...]

    def __post_init__(self) -> None:
        validate_indices(self)
        validate_rows_columns(self)

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


def get_total_expansion(star_pair):
    expansion = 0

    x_bigger = 1 if star_pair[1].row > star_pair[0].row else 0
    for x in range(star_pair[x_bigger - 1].row + 1, star_pair[x_bigger].row):
        if x in x_to_double:
            expansion += num_to_add

    y_bigger = 1 if star_pair[1].column > star_pair[0].column else 0
    for y in range(star_pair[y_bigger - 1].column + 1, star_pair[y_bigger].column):
        if y in y_to_double:
            expansion += num_to_add
    return expansion


def get_shortest_path_with_just_commonsense(star_pair):
    base = star_pair[0].distance(star_pair[1])
    expansion = get_total_expansion(star_pair)
    return (base + expansion)


import datetime as dt
def print_every_n_seconds(t, seconds, line):
    delta = dt.datetime.now()-t
    if delta.seconds >= seconds:
        print(line)
    return delta.seconds >= seconds
t = dt.datetime.now()


if __name__ == "__main__":
    script_path = Path(__file__).parent
    f = open(script_path/"input.txt", "r")
    # f = open(script_path/"test_input.txt", "r")
    a = [x.strip() for x in f.readlines()]
    width = len(a[0])

    IS_PART2 = True
    num_to_add = 1 if not IS_PART2 else 999999

    x_to_double = [x for x in range(len(a)) if all_equal(a[x], '.')]
    y_to_double = [y for y in range(len(a[0])) if all_equal(list(zip(*a))[y])]

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

    star_pairs = [x for x in sky.star_pairs]
    print(f"found {len(star_pairs)} star_pairs")

    left = len(star_pairs)
    print(f"computing shortest paths. {left} remaining")
    answer1 = 0

    ### with multiprocessing
    start_t = time.perf_counter()
    with Pool() as pool:
        for res in pool.imap_unordered(get_shortest_path_with_just_commonsense, star_pairs, 100):
            answer1 += res
            t = dt.datetime.now() if print_every_n_seconds(t, 5, f" computing shortest path. {left} remaining") else t
            left -= 1
    end_t = time.perf_counter()
    duration = end_t - start_t
    print(f"it took: {duration:.4f}s")
    print(f"answer1: {answer1}")
    pass