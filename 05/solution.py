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
    part = "building_ranges"
    ranges_evaluated = 0
    fresh_ingredients = set()
    fresh_on_hand = 0
    for line in input_data.split("\n"):
        line = line.strip()
        if not line and ranges_evaluated > 0:
            # Blank line signals switch
            part = "evaluating_ingredients"
            logging.info("Moving to evaluating_ingredients")
        elif part == "building_ranges":
            logging.debug(f"building_ranges line: '{line}'")
            ranges_evaluated += 1
            logging.info(f"Evaluating range #{ranges_evaluated}: {line}")
            start, end = line.split("-")
            start = int(start)
            end = int(end)
            for num in range(start, end + 1):
                fresh_ingredients.add(num)
        elif part == "evaluating_ingredients":
            logging.debug(f"evaluating_ingredients line: '{line}'")
            num = int(line)
            if num in fresh_ingredients:
                fresh_on_hand += 1 
    return fresh_on_hand


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
