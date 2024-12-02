import pathlib
from collections.abc import Iterator


def load_input(path: pathlib.Path) -> list[list[int]]:
    with path.open("r") as input_file:
        return [list(map(int, line.split())) for line in input_file]


def is_row_increasing(row: list[int]) -> bool:
    return all(row[i] < row[i + 1] for i in range(len(row) - 1))


def is_row_decreasing(row: list[int]) -> bool:
    return all(row[i] > row[i + 1] for i in range(len(row) - 1))


def diff_is_less_than(row: list[int], *, diff: int) -> bool:
    return all(abs(row[i] - row[i + 1]) <= diff for i in range(len(row) - 1))


def diff_is_less_than_three(row: list[int]) -> bool:
    return diff_is_less_than(row, diff=3)


def check_row_safety(row: list[int]) -> bool:
    return (is_row_increasing(row) or is_row_decreasing(row)) and diff_is_less_than_three(row)


def check_data_safety(data: list[list[int]]) -> Iterator[bool]:
    for row in data:
        yield check_row_safety(row)


def iterator_with_problem_damping(row: list[int]) -> Iterator[list[int]]:
    index = 0
    while index < len(row):
        yield row[:index] + row[index + 1 :]
        index += 1


def check_data_safety_with_problem_damping(data: list[list[int]]) -> Iterator[bool]:
    for row in data:
        if check_row_safety(row):
            yield True
            continue

        damped_row_safety = False
        for damped_row in iterator_with_problem_damping(row):
            if check_row_safety(damped_row):
                damped_row_safety = True
                break
        yield damped_row_safety


if __name__ == "__main__":
    small_input = load_input(pathlib.Path(__file__).parent / "small_input")

    safety_of_small_input = list(check_data_safety(small_input))
    print(f"Small input safety: {sum(1 for c in safety_of_small_input if c)}")

    input_data = load_input(pathlib.Path(__file__).parent / "input")
    safety_of_input_data = list(check_data_safety(input_data))
    print(f"Input safety: {sum(1 for c in safety_of_input_data if c)}")

    print("==============")
    print("With problem damping")
    print("==============")

    safety_of_small_input_with_problem_damping = list(
        check_data_safety_with_problem_damping(small_input)
    )
    print(f"Small input safety: {sum(1 for c in safety_of_small_input_with_problem_damping if c)}")

    safety_of_input_data_with_problem_damping = list(
        check_data_safety_with_problem_damping(input_data)
    )
    print(f"Input safety: {sum(1 for c in safety_of_input_data_with_problem_damping if c)}")
