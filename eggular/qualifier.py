import sys
from typing import Any
from typing import List
from typing import Optional

SAMPLE01 = rows = [
    ["Lemon"],
    ["Sebastiaan"],
    ["KutieKatj9"],
    ["Jake"],
    ["Not Joe"],
]


class Eggular:
    """Tabular Eggs"""

    def __init__(
        self, rows: List[List[Any]], labels: Optional[List[Any]], centered: bool
    ) -> None:
        self.rows = rows
        self.labels = labels
        self.centered = centered

        self.table_string = ""

    def __str__(self) -> str:
        """Print the rendered table"""
        return self.table_string


def make_table(
    rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False
) -> str:
    """
    :param rows: 2D list containing objects that have a single-line
        representation (via `str`). All rows must be of the same length.
    :param labels: List containing the column labels. If present, the
        length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else
        they are left aligned.
    :return: A table representing the rows passed in.
    """
    egg_table = Eggular(rows, labels, centered)

    return egg_table.table_string


if __name__ == "__main__":
    print(make_table(SAMPLE01))
    sys.exit(0)
