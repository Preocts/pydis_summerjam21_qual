import datetime
from typing import Any
from typing import List

import pytest

from eggular.qualifier import Eggular
from eggular.qualifier import make_table


SAMPLE01_ROWS: List[List[Any]] = [
    ["Lemon"],
    ["Sebastiaan"],
    ["KutieKatj9"],
    ["Jake"],
    ["Not Joe"],
]
SAMPLE02_ROWS: List[List[Any]] = [
    ["Lemon", 18_3285, "Owner"],
    ["Sebastiaan", 18_3285.1, "Owner"],
    ["KutieKatj", 15_000, "Admin"],
    ["Jake", "MoreThanU", "Helper"],
    ["Joe", -12, "Idk Tbh"],
]

SAMPLE02_LABELS = ["User", "Messages", "Role"]

SAMPLE03_ROWS = [
    ["Ducky Yellow", 3],
    ["Ducky Dave", 12],
    ["Ducky Tube", 7],
    ["Ducky Lemon", 1],
]
SAMPLE03_LABELS = ["Name", "Duckiness"]

SAMPLE04_ROWS = [
    [None, None, None],
    [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
]
NOW = datetime.datetime.now()
SAMPLE04_LABELS = [NOW, 0, "zero"]

EXAMPLE01_RESULT = "\n".join(
    [
        "┌────────────┐",
        "│ Lemon      │",
        "│ Sebastiaan │",
        "│ KutieKatj9 │",
        "│ Jake       │",
        "│ Not Joe    │",
        "└────────────┘",
    ]
)

EXAMPLE02_RESULT = "\n".join(
    [
        "┌────────────┬───────────┬─────────┐",
        "│ User       │ Messages  │ Role    │",
        "├────────────┼───────────┼─────────┤",
        "│ Lemon      │ 183285    │ Owner   │",
        "│ Sebastiaan │ 183285.1  │ Owner   │",
        "│ KutieKatj  │ 15000     │ Admin   │",
        "│ Jake       │ MoreThanU │ Helper  │",
        "│ Joe        │ -12       │ Idk Tbh │",
        "└────────────┴───────────┴─────────┘",
    ]
)

EXAMPLE03_RESULT = "\n".join(
    [
        "┌──────────────┬───────────┐",
        "│     Name     │ Duckiness │",
        "├──────────────┼───────────┤",
        "│ Ducky Yellow │     3     │",
        "│  Ducky Dave  │    12     │",
        "│  Ducky Tube  │     7     │",
        "│ Ducky Lemon  │     1     │",
        "└──────────────┴───────────┘",
    ]
)

EXAMPLE04_RESULT = "\n".join(
    [
        "┌────────────────────────────┬───────────┬───────────┐",
        f"│ {NOW} │     0     │   zero    │",
        "├────────────────────────────┼───────────┼───────────┤",
        "│            None            │   None    │   None    │",
        "│         [1, 2, 3]          │ [1, 2, 3] │ [1, 2, 3] │",
        "└────────────────────────────┴───────────┴───────────┘",
    ]
)


@pytest.mark.parametrize(
    ("row", "label", "centered", "expected"),
    (
        (SAMPLE01_ROWS, None, False, EXAMPLE01_RESULT),
        (SAMPLE02_ROWS, SAMPLE02_LABELS, False, EXAMPLE02_RESULT),
        (SAMPLE03_ROWS, SAMPLE03_LABELS, True, EXAMPLE03_RESULT),
        (SAMPLE04_ROWS, SAMPLE04_LABELS, True, EXAMPLE04_RESULT),
    ),
)
def test_sample_01(
    row: List[List[Any]], label: List[Any], centered: bool, expected: Any
) -> None:
    """Result match against example 01"""

    result = make_table(row, label, centered)

    assert result == expected


def test_sample_02() -> None:
    """Result match against example 01"""

    result = make_table(SAMPLE02_ROWS, SAMPLE02_LABELS)

    assert result == EXAMPLE02_RESULT


@pytest.mark.parametrize(
    ("eggtable", "expected"),
    (
        (Eggular(SAMPLE01_ROWS, None, False), [10]),
        (Eggular(SAMPLE02_ROWS, SAMPLE02_LABELS, False), [10, 9, 7]),
        (Eggular(SAMPLE03_ROWS, SAMPLE03_LABELS, True), [12, 9]),
    ),
)
def test_find_column_sizes(eggtable: Eggular, expected: List[int]) -> None:
    """Find the correct max column size"""
    eggtable.render_table()
    assert eggtable.col_sizes == expected
