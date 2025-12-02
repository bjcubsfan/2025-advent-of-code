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

def is_invalid(id_to_check):
    logging.debug(f"{id_to_check=}")
    str_id = str(id_to_check)
    if len(str_id) % 2 != 0:
        return False
    half_id = int(len(str_id) / 2)
    first = str_id[:half_id]
    last = str_id[half_id:]
    if first == last:
        logging.debug(f"FOUND ONE: {str_id}")
        return True
    else:
        return False

def sum_invalid_ids(id_range):
    first_id, last_id = id_range.split("-")
    first_id = int(first_id)
    last_id = int(last_id)
    this_range_sum = 0
    for id_to_check in range(first_id, last_id + 1):
        if is_invalid(id_to_check):
            logging.debug("Adding it")
            this_range_sum += id_to_check
        else:
            continue
    return this_range_sum

def part_1(input_data):
    input_data = input_data.strip()
    answer = 0
    for line in input_data.split("\n"):
        line = line.strip()
        for id_range in line.split(","):
            answer += sum_invalid_ids(id_range)
            logging.debug(f"{answer=}")
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
    main()
