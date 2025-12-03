#!/usr/bin/env python
"""
Usage: solution.py [options]

Options:
  -h --help             Show this help message and exit
  -d --debug            Enable debugging prints.
"""

from collections import defaultdict
import logging
import pprint

import docopt


def part_1(input_data):
    input_data = input_data.strip()
    answer = 0
    for line in input_data.split("\n"):
        line = line.strip()
        line_digits = [int(this_char) for this_char in line]
        logging.debug(f"{line_digits=}")
        max_value = max(line_digits[:-1])
        index_max = line_digits.index(max_value)
        second_max = max(line_digits[index_max + 1:])
        joltage = int(f"{max_value}{second_max}")
        logging.debug(f"{joltage=}")
        answer += joltage
    return answer


def part_2(input_data):
    input_data = input_data.strip()
    answer = None
    for line in input_data.split("\n"):
        line = line.strip()
    return answer


def main():
    with open("input") as input_file:
        input_data = input_file.read()
    print(part_1(input_data))
    print(part_2(input_data))


if __name__ == "__main__":
    options = docopt.docopt(__doc__)
    if options["--debug"]:
        logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
    else:
        logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    main()
