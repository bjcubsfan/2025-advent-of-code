#!/usr/bin/env python
"""
Usage: solution.py [options]

Options:
  -h --help             Show this help message and exit
  -d --debug            Enable debugging prints.
"""

from collections import defaultdict
import itertools
import logging
import pprint
import sys

import docopt

def compact_diagram(helpful_diagram):
    lines = ["\n"]
    for line in helpful_diagram:
        lines.append("".join(line))
    return "\n".join(lines)

def get_spots_to_check(v_index, h_index):
    to_check = []
    raw_check = []
    for add_to_h, add_to_v in itertools.product((-1, 0, 1), repeat=2):
        raw_check.append((add_to_v, add_to_h))
        if add_to_v == 0 and add_to_h == 0:
            continue
        to_check.append((v_index + add_to_v, h_index + add_to_h))
    #logging.debug(f"{v_index=} {h_index=} {to_check=} {len(to_check)=} {raw_check=} {len(raw_check)=}")
    return to_check


def is_accessible(helpful_diagram, v_index, h_index):
    spots_to_check = get_spots_to_check(v_index, h_index)
    max_v = len(helpful_diagram) - 1
    max_h = len(helpful_diagram[0]) - 1
    num_nearby = 0
    for v_spot, h_spot in spots_to_check:
        if num_nearby >= 4:
            logging.debug(f"False {v_index} {h_index} {num_nearby=} {len(spots_to_check)=}")
            return False
        if v_spot < 0 or h_spot < 0 or v_spot > max_v or h_spot > max_h:
            continue
        if helpful_diagram[v_spot][h_spot] == "@":
            #logging.debug(f"{h_spot=} {v_spot} has a roll!")
            num_nearby += 1
    if num_nearby < 4:
        logging.debug(f"True end {v_index} {h_index} {num_nearby=}")
        return True
    else:
        logging.debug(f"False end {v_index} {h_index} {num_nearby=}")
        return False


def num_accessible(helpful_diagram):
    v_size = len(helpful_diagram)
    h_size = len(helpful_diagram[0])
    answer = 0
    accessable = []
    for v_index in range(v_size):
        for h_index in range(h_size):
            if helpful_diagram[v_index][h_index] == "@":
                if is_accessible(helpful_diagram, v_index, h_index):
                    answer += 1
                    accessable.append((v_index, h_index))
    return answer, accessable


def part_1(input_data):
    helpful_diagram = []
    input_data = input_data.strip()
    first_line_length = None
    for line in input_data.split("\n"):
        if not line:
            continue
        line = line.strip()
        if not first_line_length:
            first_line_length = len(line)
        #logging.debug(f"{line=}  -  {len(line)=}  -  {first_line_length=}")
        assert len(line) == first_line_length
        this_diagram_row = []
        for character in line:
            this_diagram_row.append(character)
        helpful_diagram.append(this_diagram_row)
    logging.debug(f"{compact_diagram(helpful_diagram)}")
    answer, accessable = num_accessible(helpful_diagram)
    for v_index, h_index in accessable:
        helpful_diagram[v_index][h_index] = "X"
    logging.debug(f"SHOW_ACCESSIBLE:{compact_diagram(helpful_diagram)}")
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
