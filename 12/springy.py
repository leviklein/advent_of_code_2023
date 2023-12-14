import re
import pathlib
from math import pow
from itertools import groupby, combinations
from functools import reduce
from operator import add
import time
from multiprocessing import Pool


def is_correct(iterable, counts):
    count_iter = [ len(list(g)) for k, g in groupby(iterable) if k == '#']
    return count_iter == counts

# from https://stackoverflow.com/questions/1851134/generate-all-binary-strings-of-length-n-with-k-bits-set
def kbits(n, k):
    for bits in combinations(range(n), k):
        s = ['0'] * n
        for bit in bits:
            s[bit] = '1'
        num = int(''.join(s), 2)
        yield num



def get_answer(inputs):
    sequence = inputs[0]
    counts = inputs[1]
    # 0 == .
    # 1 == #
    qs = sequence.count('?')
    target_counts = reduce(add, counts)
    current_counts = sequence.count('#')

    list_sequence = list(sequence)
    print(f"{sequence}, {counts}")
    qs_idx = [ i.start() for i in re.finditer('\?', sequence) ]

    answer = 0
    for i in kbits(qs, target_counts-current_counts):
        bitfield = i
        combination = list_sequence
        for x in range(qs):
            if bitfield & 1:
                combination[qs_idx[x]] = '#'
            else:
                combination[qs_idx[x]] = '.'
            bitfield = bitfield >> 1

        answer += 1 if is_correct(combination, counts) else 0
    return answer


import datetime as dt
def print_every_n_seconds(t, seconds, line):
    delta = dt.datetime.now()-t
    if delta.seconds >= seconds:
        print(line)
    return delta.seconds >= seconds
t = dt.datetime.now()


if __name__ == "__main__":
    script_path = str(pathlib.Path(__file__).parent.resolve()) + "/"

    f = open(script_path + "input.txt", "r")
    # f = open(script_path + "test_input.txt", "r")
    a = f.readline().strip()

    IS_PART2 = True
    IS_PART2 = False

    row = 1
    answer1 = 0
    input_pairs = []
    while a:
        pass
        sequence, counts = a.split(' ')
        sequence = '.'.join([ x for x in sequence.split('.') if len(x)> 0 ])
        counts = [ int(x) for x in counts.split(',') ]
        if IS_PART2:
            sequence = "?".join([sequence] * 5)
            counts = counts * 5
        input_pairs.append((sequence, counts))
        a = f.readline().strip()
        row += 1

    left = len(input_pairs)
    print(f"computing combinations. {left} remaining")
    answer1 = 0

    start_t = time.perf_counter()
    with Pool() as pool:
        for res in pool.imap_unordered(get_answer, input_pairs):
            answer1 += res
            t = dt.datetime.now() if print_every_n_seconds(t, 1, f" computing combinations path. {left} remaining") else t
            left -= 1
    end_t = time.perf_counter()
    duration = end_t - start_t
    print(f"it took: {duration:.4f}s")

    print(f"answer1 is {answer1}")
    pass