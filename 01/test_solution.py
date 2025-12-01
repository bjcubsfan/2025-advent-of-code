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

# @pytest.mark.parametrize(
#    "encrypted_room, is_real_room",
#    [
#        ("aaaaa-bbb-z-y-x-123[abxyz]", True),
#        ("a-b-c-d-e-f-g-h-987[abcde]", True),
#        ("not-a-real-room-404[oarel]", True),
#        ("totally-real-room-200[decoy]", False),
#    ],)
def test_part_1():
    calc_part_1 = part_1(input_data)
    assert calc_part_1 == 3


def test_part_2():
    calc_part_2 = part_2(input_data)
    assert calc_part_2 == 6
