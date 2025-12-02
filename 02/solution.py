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
import textwrap

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

def check_split(str_id, wrap_to_num):
    parts = textwrap.wrap(str_id, wrap_to_num)
    sentinal = parts[-1]
    for part in parts:
        logging.debug(f"{part=} {sentinal=}")
        if part != sentinal:
            return False
    return True

def p2_is_invalid(id_to_check):
    logging.debug(f"{id_to_check=}")
    str_id = str(id_to_check)
    wrap_to_nums = []
    for check_if_splits_by in range(2, len(str_id)):
        if len(str_id) % check_if_splits_by == 0:
            if len(str_id) % check_if_splits_by == 0:
                wrap_to_nums.append(int(len(str_id) / check_if_splits_by))
    # Always have split for each character
    wrap_to_nums.append(1)
    logging.debug(f"{wrap_to_nums=}")
    for wrap_to_num in wrap_to_nums:
        logging.debug(f"checking {wrap_to_num=}")
        if check_split(str_id, wrap_to_num):
            logging.debug(f"FOUND ONE: {str_id}")
            return True
    return False

def p2_sum_invalid_ids(id_range):
    this_range_sum = 0
    first_id, last_id = id_range.split("-")
    first_id = int(first_id)
    last_id = int(last_id)
    for id_to_check in range(first_id, last_id + 1):
        if p2_is_invalid(id_to_check):
            logging.debug(f"Adding it {id_to_check=}")
            this_range_sum += id_to_check
    return this_range_sum

def p1_sum_invalid_ids(id_range):
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
            answer += p1_sum_invalid_ids(id_range)
            logging.debug(f"{answer=}")
    return answer


def part_2(input_data):
    input_data = input_data.strip()
    answer = 0
    for line in input_data.split("\n"):
        line = line.strip()
        for id_range in line.split(","):
            logging.info(f"About to check {id_range=}")
            answer += p2_sum_invalid_ids(id_range)
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
        pass
        logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
    main()
