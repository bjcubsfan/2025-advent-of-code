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

def compact_diagram(helpful_diagram):
    lines = ["\n"]
    for line in helpful_diagram:
        lines.append("".join(line))
    return "\n".join(lines)


def is_accessible(helpful_diagram, v_index, h_index):



def num_accessible(helpful_diagram):
    v_size = len(helpful_diagram)
    h_size = len(helpful_diagram[0])
    answer = 0
    for v_index, h_index in zip(range(v_size), range(h_size)):
        if is_accessible(helpful_diagram, v_index, h_index):
            answer += 1
    return answer


def part_1(input_data):
    helpful_diagram = []
    input_data = input_data.strip()
    first_line_length = None
    for line in input_data.split("\n"):
        line = line.strip()
        if not first_line_length:
            first_line_length == len(line)
        assert len(line) == first_line_length
        this_diagram_row = []
        for character in line:
            this_diagram_row.append(character)
        helpful_diagram.append(this_diagram_row)
    logging.debug(f"{compact_diagram(helpful_diagram)}")
    return num_accessible(helpful_diagram)


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
