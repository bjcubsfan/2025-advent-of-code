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


def find_next_best_digit(digits, final_digit_index):
    logging.debug(f"find next: {digits=} {final_digit_index=}")
    reserve_end = final_digit_index - 11
    choose_from = digits[:reserve_end]
    if not choose_from:
        max_value = max(digits)
        return max_value, digits.index(max_value)
    logging.debug(f"{choose_from=}")
    max_value = max(choose_from)
    index_max = digits.index(max_value)
    return max_value, index_max

def part_2(input_data):
    input_data = input_data.strip()
    answer = 0
    for line in input_data.split("\n"):
        this_joltage_digits = []
        line = line.strip()
        line_digits = [int(this_char) for this_char in line]
        logging.debug(f"{line_digits=}")
        next_index = 0
        for digit_index in range(12):
            max_value, index_max = find_next_best_digit(line_digits[next_index:], digit_index)
            #logging.debug(f"{max_value=} {index_max=}")
            this_joltage_digits.append(str(max_value))
            next_index = index_max + next_index + 1
            #logging.debug(f"{next_index=}")
            logging.debug(f"{digit_index=} {this_joltage_digits=} {len(this_joltage_digits)=}")
        joltage = int("".join(this_joltage_digits))
        logging.debug(f"{joltage=}")
        answer += joltage
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
