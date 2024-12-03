import pathlib
import re


def load_input(file_path: pathlib.Path) -> str:
    with file_path.open() as f:
        return f.read()


def calculate_with_do_and_dont(string: str) -> int:
    mul_pattern = r"mul\((\d+),(\d+)\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    score = 0
    should_multiply = True

    position = 0

    while position < len(string):
        if do_match := re.match(do_pattern, string[position:]):
            should_multiply = True
            position += do_match.end()
            continue

        if dont_match := re.match(dont_pattern, string[position:]):
            should_multiply = False
            position += dont_match.end()
            continue

        if mul_match := re.match(mul_pattern, string[position:]):
            if should_multiply:
                score += int(mul_match.group(1)) * int(mul_match.group(2))
            position += mul_match.end()
            continue

        position += 1

    return score


if __name__ == "__main__":
    input_ = load_input(pathlib.Path(__file__).parent / "input")
    print(calculate_with_do_and_dont(input_))
# 78683433
