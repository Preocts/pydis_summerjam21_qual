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


def test_sample_01() -> None:
    """Result match against example 01"""

    result = make_table(SAMPLE01_ROWS)

    assert result == EXAMPLE01_RESULT


def test_sample_02() -> None:
    """Result match against example 01"""

    result = make_table(SAMPLE02_ROWS, SAMPLE02_LABELS)

    assert result == EXAMPLE02_RESULT


@pytest.mark.parametrize(
    ("eggtable", "expected"),
    (
        (Eggular(SAMPLE01_ROWS, None, False), [10]),
        (Eggular(SAMPLE02_ROWS, SAMPLE02_LABELS, False), [10, 9, 7]),
    ),
)
def test_find_column_sizes(eggtable: Eggular, expected: List[int]) -> None:
    """Find the correct max column size"""
    eggtable.render_table()
    assert eggtable.col_sizes == expected
