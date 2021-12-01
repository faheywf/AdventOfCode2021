from typing import List


def load_day_one_input() -> List[int]:
    with open("day1.txt", "r") as f:
        lines = f.readlines()
    return [int(line) for line in lines]

def day_one_part_one() -> int:
    readings = load_day_one_input()
    num_increasing = 0
    prev_reading = readings[0]
    for reading in readings[1:]:
        if reading > prev_reading:
            num_increasing += 1
        prev_reading = reading
    return num_increasing

def day_one_part_two() -> int:
    readings = load_day_one_input()
    a = 0
    b = 1
    c = 2

    num_increasing = 0
    prev_reading = readings[a] + readings[b] + readings[c]
    a, b, c = 1, 2, 3
    while c < len(readings):
        reading = readings[a] + readings[b] + readings[c]
        if reading > prev_reading:
            num_increasing += 1
        prev_reading = reading
        a += 1
        b += 1
        c += 1

    return num_increasing
