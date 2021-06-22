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
