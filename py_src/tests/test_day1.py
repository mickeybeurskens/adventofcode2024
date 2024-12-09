from aoc_24.day1 import part1, part2

INPUT = """\
3   4
4   3
2   5
1   3
3   9
3   3
"""
OUTPUT_1 = "11"
OUTPUT_2 = "31"


def test_part1():
    assert part1(INPUT) == OUTPUT_1


def test_part2():
    assert part2(INPUT) == OUTPUT_2
