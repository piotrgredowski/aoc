import pathlib


def load_input(path: pathlib.Path) -> tuple[list[int], list[int]]:
    left, right = [], []
    with path.open() as f:
        for line in f:
            left.append(int(line.split()[0]))
            right.append(int(line.split()[1]))
    return left, right


def get_total_distance(left: list[int], right: list[int]) -> int:
    left_sorted = sorted(left)
    right_sorted = sorted(right)

    total_distance = 0

    for left_item, right_item in zip(left_sorted, right_sorted, strict=False):
        distance = abs(left_item - right_item)
        total_distance += distance

    return total_distance


def get_similarity_score(left: list[int], right: list[int]) -> int:
    total_score = 0

    for item in left:
        how_many_items_in_right = right.count(item)
        item_score = how_many_items_in_right * item
        total_score += item_score

    return total_score


if __name__ == "__main__":
    path_to_input = pathlib.Path(__file__).parent / "day_1_input"

    left, right = load_input(path_to_input)

    total_distance = get_total_distance(left, right)

    print(f"{total_distance=}")

    similarity_score = get_similarity_score(left, right)
    print(f"{similarity_score=}")
