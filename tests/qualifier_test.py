from typing import Generator

import pytest

from eggular.qualifier import Eggular
from eggular.qualifier import make_table
from eggular.qualifier import SAMPLE01


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


@pytest.fixture(scope="function", name="sample01")
def fixture_sample01() -> Generator[Eggular, None, None]:
    """Example 01 test fixture"""
    eggtable = Eggular(SAMPLE01, None, False)

    eggtable.render_table()

    yield eggtable


def test_sample_01() -> None:
    """Result match against example 01"""

    result = make_table(SAMPLE01)

    assert result == EXAMPLE01_RESULT


def test_find_column_sizes(sample01: Eggular) -> None:
    """Find the correct max column size"""
    expected = [10]

    assert sample01.col_sizes == expected
