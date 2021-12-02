from typing import List

class SubCommand:
    def __init__(self, command: str):
        self.direction, distance = command.split()
        self.distance = int(distance)

def load_day_two_input() -> List[SubCommand]:
    with open("day2.txt", "r") as f:
        lines = f.readlines()
    return [SubCommand(line) for line in lines]

def day_two_part_one() -> int:
    depth, horizontal_position = 0, 0
    commands = load_day_two_input()

    for command in commands:
        if command.direction == "forward":
            horizontal_position += command.distance
        elif command.direction == "up":
            depth -= command.distance
        else:
            depth += command.distance
    
    return depth * horizontal_position

def day_two_part_two() -> int:
    depth, horizontal_position, aim = 0, 0, 0
    commands = load_day_two_input()

    for command in commands:
        if command.direction == "forward":
            horizontal_position += command.distance
            depth += aim * command.distance
        elif command.direction == "up":
            aim -= command.distance
        else:
            aim += command.distance
    
    return depth * horizontal_position