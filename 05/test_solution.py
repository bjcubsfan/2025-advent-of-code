import logging
import pytest

from solution import part_1, part_2

input_data = """3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""


def test_part_1():
    calc_part_1 = part_1(input_data)
    assert calc_part_1 == 3


@pytest.mark.parametrize(
   "expected, input_data",
   [
       (14, """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""),
       (14, """3-5
10-14
16-20
17-19
13-17
12-18

1
"""),
   ],
)
def test_part_2(expected, input_data):
    calc_part_2 = part_2(input_data)
    assert calc_part_2 == expected
