import pathlib
import re


def load_input(file_path: pathlib.Path) -> str:
    with file_path.open() as f:
        return f.read()


def find_mul_operations(input_: str) -> list[tuple[int, int]]:
    return [(int(a), int(b)) for a, b in re.findall(r"mul\((\d+),(\d+)\)", input_)]


def calculate_mul_operations(all_mul_operations: list[tuple[int, int]]) -> int:
    return sum(a * b for a, b in all_mul_operations)


if __name__ == "__main__":
    input_ = load_input(pathlib.Path(__file__).parent / "input")

    mul_operations = find_mul_operations(input_)

    result = calculate_mul_operations(mul_operations)
    print(result)
