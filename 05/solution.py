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

def num_is_fresh(range_tuples, num):
    for start, stop in range_tuples:
        if num >= start and num <= stop:
            return True
    return False

def part_1(input_data):
    input_data = input_data.strip()
    part = "building_ranges"
    ranges_evaluated = 0
    fresh_ingredients = set()
    fresh_on_hand = 0
    range_tuples = []
    for line in input_data.split("\n"):
        line = line.strip()
        if not line and ranges_evaluated > 0:
            # Blank line signals switch
            part = "evaluating_ingredients"
            logging.info("Moving to evaluating_ingredients")
        # Build tuples
        elif part == "building_ranges":
            ranges_evaluated += 1
            logging.info(f"Evaluating range #{ranges_evaluated}: {line}")
            start, end = line.split("-")
            start = int(start)
            end = int(end)
            range_tuples.append((start, end))
        elif part == "evaluating_ingredients":
            logging.debug(f"evaluating_ingredients line: '{line}'")
            num = int(line)
            if num_is_fresh(range_tuples, num):
                fresh_on_hand += 1
    return fresh_on_hand

def reduce_tuple_overlap(refined_tuples):
    original_tuples = refined_tuples
    logging.debug(f"{original_tuples=}")
    for eval_tuple in original_tuples:
        logging.debug(f"{eval_tuple=}")
        start, end = eval_tuple
        other_tuples = [this_tuple for this_tuple in original_tuples if this_tuple != eval_tuple]
        logging.debug(f"{other_tuples=}")
        for other_tuple in other_tuples:
            o_start, o_end = other_tuple
            if start >= o_start and start <= o_end:
                # Start is in the other tuple
                # 20-34 & 19-20
                untouched = [this for this in other_tuples if this != other_tuple]
                logging.debug(f"start {untouched=}")
                new_tuple = (o_start, max(o_end, end))
                logging.debug(f"start {new_tuple=}")
                untouched.append(new_tuple)
                return original_tuples, untouched
            elif end <= o_end and end >= o_start:
                # End is in the other tuple
                # 20-34 & 32-39
                untouched = [this for this in other_tuples if this != other_tuple]
                logging.debug(f"end {untouched=}")
                new_tuple = (min(o_start, start), o_end)
                logging.debug(f"end {new_tuple=}")
                untouched.append(new_tuple)
                return original_tuples, untouched
    return original_tuples, refined_tuples

def part_2(input_data):
    input_data = input_data.strip()
    part = "building_ranges"
    ranges_evaluated = 0
    fresh_ingredients = set()
    fresh_on_hand = 0
    range_tuples = []
    for line in input_data.split("\n"):
        line = line.strip()
        if not line and ranges_evaluated > 0:
            # Blank line signals switch
            part = "evaluating_ingredients"
            logging.info("Moving to evaluating_ingredients")
        # Build tuples
        elif part == "building_ranges":
            ranges_evaluated += 1
            logging.info(f"Evaluating range #{ranges_evaluated}: {line}")
            start, end = line.split("-")
            start = int(start)
            end = int(end)
            range_tuples.append((start, end))
        elif part == "evaluating_ingredients":
            continue
    original_tuples = []
    refined_tuples = range_tuples
    while refined_tuples != original_tuples:
        original_tuples, refined_tuples = reduce_tuple_overlap(refined_tuples)
        logging.debug(f"Refined to: {pprint.pformat(refined_tuples)}")
    answer = 0
    for start, end in refined_tuples:
        answer += end + 1 - start
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
