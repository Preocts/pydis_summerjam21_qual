from eggular.qualifier import Eggular
from eggular.qualifier import make_table
from eggular.qualifier import SAMPLE01


EXAMPLE01_RESULT = "".join(
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


def test_sample_01() -> None:
    """Result match against example 01"""

    result = make_table(SAMPLE01)

    assert result == EXAMPLE01_RESULT


def test_find_column_sizes() -> None:
    """Find the correct max column size"""
    expected = [10]
    eggtable = Eggular(SAMPLE01, None, False)

    eggtable.find_column_sizes()

    assert eggtable.col_sizes == expected
