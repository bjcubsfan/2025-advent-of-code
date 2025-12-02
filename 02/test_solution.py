import logging
import pytest

from solution import part_1, part_2

input_data = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224, 1698522-1698528,446443-446449,38593856-38593862,565653-565659, 824824821-824824827,2121212118-2121212124"""


# @pytest.mark.parametrize(
#    "encrypted_room, is_real_room",
#    [
#        ("aaaaa-bbb-z-y-x-123[abxyz]", True),
#        ("a-b-c-d-e-f-g-h-987[abcde]", True),
#        ("not-a-real-room-404[oarel]", True),
#        ("totally-real-room-200[decoy]", False),
#    ],
# )
def test_part_1():
    calc_part_1 = part_1(input_data)
    assert calc_part_1 == 1227775554


def test_part_2():
    calc_part_2 = part_2(input_data)
    assert calc_part_2 == 4174379265
