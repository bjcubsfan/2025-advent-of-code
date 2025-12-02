import logging
import pytest

from solution import part_1, part_2

input_data = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224, 1698522-1698528,446443-446449,38593856-38593862,565653-565659, 824824821-824824827,2121212118-2121212124"""


def test_part_1():
    calc_part_1 = part_1(input_data)
    assert calc_part_1 == 1227775554


@pytest.mark.parametrize(
   "expected, input_string",
   [
       (4174379265, """11-22,95-115,998-1012,1188511880-1188511890,222220-222224, 1698522-1698528,446443-446449,38593856-38593862,565653-565659, 824824821-824824827,2121212118-2121212124"""),
       (676767, """676766-676768"""),
   ],
)
def test_part_2(expected, input_string):
    calc_part_2 = part_2(input_string)
    assert calc_part_2 == expected
