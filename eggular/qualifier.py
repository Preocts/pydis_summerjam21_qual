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

    TOP_LEFT = "┌"
    TOP_RIGHT = "┐"
    BOT_LEFT = "└"
    BOT_RIGHT = "┘"
    HORZ = "─"
    VERT = "│"

    def __init__(
        self, rows: List[List[Any]], labels: Optional[List[Any]], centered: bool
    ) -> None:
        self.rows = rows
        self.labels = labels
        self.centered = centered

        # We can always assume all rows will have the same # of entries
        self.total_columns = len(rows[0])
        self.col_sizes: List[int] = [0 for _ in range(self.total_columns)]

        self.table_string = ""

    def render_table(self) -> str:
        """Runs all steps to make a table"""
        self._find_column_sizes()

        table_values = "\n".join(self._table_values())

        table_rows = [
            self._table_top(),
            table_values,
            self._table_bottom(),
        ]

        return "\n".join(table_rows)

    def _find_column_sizes(self) -> None:
        """Finds the max column width"""
        for row in self.rows:
            for idx, column_value in enumerate(row):
                if len(column_value) > self.col_sizes[idx]:
                    self.col_sizes[idx] = len(column_value)

    def _table_top(self) -> str:
        """Generates top of table"""
        table_top = f"{self.TOP_LEFT}{self.HORZ}"
        for size in self.col_sizes:
            table_top += self.HORZ * size
        return f"{table_top}{self.HORZ}{self.TOP_RIGHT}"

    def _table_bottom(self) -> str:
        """Generates bottom of table"""
        table_top = f"{self.BOT_LEFT}{self.HORZ}"
        for size in self.col_sizes:
            table_top += self.HORZ * size
        return f"{table_top}{self.HORZ}{self.BOT_RIGHT}"

    def _table_values(self) -> List[str]:
        """Generates rows of table values"""
        table_values: List[str] = []
        for row in self.rows:
            table_row = ""
            for idx, column_value in enumerate(row):
                padded_value = self._pad_value(column_value, idx)
                table_row += f"{self.VERT} {padded_value}"
            table_row += f" {self.VERT}"
            table_values.append(table_row)
        return table_values

    def _pad_value(self, value: str, col: int) -> str:
        """Pads the value with spaces"""
        pad_size = self.col_sizes[col] - len(value)
        return value + " " * pad_size


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

    return egg_table.render_table()


if __name__ == "__main__":
    print(make_table(SAMPLE01))
    sys.exit(0)
