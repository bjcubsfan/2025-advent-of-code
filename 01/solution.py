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
import sys

import docopt

def part_1(input_data):
    input_data = input_data.strip()
    index = 50
    answer = 0
    for line in input_data.split("\n"):
        line = line.strip()
        if not line:
            continue
        if line[0] == "R":
            # Positive
            logging.debug("R")
            number = int(line[1:])
            index = (index + number) % 100
        elif line[0] == "L":
            # Negative
            logging.debug("L")
            number = int(line[1:])
            index = (index - number) % 100
        else:
            sys.exit("NO L OR R!?!?")
        logging.debug(f"{index=}")
        if index == 0:
            answer += 1 
    return answer


def part_2(input_data):
    logging.debug("====== PART 2 ========")
    input_data = input_data.strip()
    input_data = input_data.strip()
    index = 50
    answer = 0
    for line in input_data.split("\n"):
        logging.debug(f"{answer=}")
        logging.debug(f"{index=}")
        line = line.strip()
        if not line:
            continue
        logging.debug(f"{line=}")
        number = int(line[1:])
        if line[0] == "R":
            # Positive
            direction = 1
        elif line[0] == "L":
            # Negative
            direction = -1
        else:
            sys.exit("NO L OR R!?!?")
        cross_zero, new_index = divmod(index + direction * number, 100)
        answer += abs(cross_zero)
        index = new_index
    logging.debug(f"{answer=}")
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
    main()
