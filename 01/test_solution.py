import logging
import pytest

from solution import part_1, part_2

input_data = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

def test_part_1():
    calc_part_1 = part_1(input_data)
    assert calc_part_1 == 3


@pytest.mark.parametrize(
   "this_input_data, expected",
   [
       ("""L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
""", 6),
       ("""L500
R1000
L50
L5
R5
R5
""", 17),
       ("""L500
R1000
L50
L5
""", 16),
   ],)
def test_part_2(this_input_data, expected):
    calc_part_2 = part_2(this_input_data)
    assert calc_part_2 == expected
