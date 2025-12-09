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
    lines = []
    for line in input_data.split("\n"):
        line = line.strip()
        lines.append(line)
    columns = len(line)
    problems = [[] for column in range(columns)]
    for line in lines[:-1]:
        line = line.split()
        for index, number in enumerate(line):
            number = int(number)
            try:
                problems[index].append(number)
            except IndexError:
                import IPython; IPython.embed()
    answer = 0
    logging.debug(f"{pprint.pformat(problems)}")
    for index, oper in enumerate(lines[-1].split()):
        this_answer = None
        if oper == "*":
            for number in problems[index]:
                if this_answer is None:
                    this_answer = number
                    logging.debug(f"start mul with {number}")
                else:
                    logging.debug(f"{this_answer} * {number}")
                    this_answer = this_answer.__mul__(number)
            answer += this_answer
        elif oper == "+":
            for number in problems[index]:
                if this_answer is None:
                    this_answer = number
                    logging.debug(f"start add with {number}")
                else:
                    logging.debug(f"{this_answer} + {number}")
                    this_answer = this_answer.__add__(number)
            answer += this_answer
        else:
            sys.exit("How did we get here?")
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
