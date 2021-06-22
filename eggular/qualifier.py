"""
Qualifier round for PyDiscord Summer Code Jam '21

Author: Preocts (Discord: Preocts#8196)
"""
from typing import Any
from typing import List
from typing import Optional


class Eggular:
    """Tabular Eggs"""

    VERT = "│"
    TOP_BORDER = ("┌", "─", "┬", "┐")
    MID_BORDER = ("├", "─", "┼", "┤")
    BOT_BORDER = ("└", "─", "┴", "┘")

    def __init__(
        self, rows: List[List[Any]], labels: Optional[List[Any]], centered: bool
    ) -> None:
        self.rows = [self._stringify(row) for row in rows]
        self.labels = self._stringify(labels) if labels is not None else None
        self.centered = centered

        # Qualifier: can assume all rows will have the same # of entries
        self.total_columns = len(rows[0])
        self.col_sizes: List[int] = [0 for _ in range(self.total_columns)]

        self.table_string = ""

    def render_table(self) -> str:
        """Creates a printing string of the table"""
        self._find_column_sizes()

        self.table_string = self._table_border(*self.TOP_BORDER)

        if self.labels is not None:
            self.table_string += "\n" + self._table_rows([self.labels])[0]
            self.table_string += "\n" + self._table_border(*self.MID_BORDER)

        self.table_string += "\n" + "\n".join(self._table_rows(self.rows))

        self.table_string += "\n" + self._table_border(*self.BOT_BORDER)

        return self.table_string

    @staticmethod
    def _stringify(list_data: List[Any]) -> List[str]:
        """Return given list with strings instead"""
        return [str(data) for data in list_data]

    def _find_column_sizes(self) -> None:
        """Finds the max column width"""
        check_rows = self.rows.copy()
        if self.labels is not None:
            check_rows.append(self.labels.copy())

        for row in check_rows:
            for idx, column_value in enumerate(row):
                if len(column_value) > self.col_sizes[idx]:
                    self.col_sizes[idx] = len(column_value)

    def _table_border(self, left: str, mid: str, seg: str, right: str) -> str:
        """Generates border row of table"""
        table_top = ""

        for idx, size in enumerate(self.col_sizes):
            leading = left if idx == 0 else seg
            table_top += f"{leading}{mid * (size + 2)}"

        return f"{table_top}{right}"

    def _table_rows(self, rows: List[List[str]]) -> List[str]:
        """Generates rows of table values"""
        table_values: List[str] = []
        for row in rows:
            table_row = ""
            for idx, column_value in enumerate(row):
                padded_value = self._pad_value(column_value, idx)
                table_row += f"{self.VERT} {padded_value} "

            table_values.append(table_row + self.VERT)
        return table_values

    def _pad_value(self, value: str, col: int) -> str:
        """Pads the value with spaces, accounts for centered flag"""
        pad_size = self.col_sizes[col] - len(value)
        left = pad_size // 2 if self.centered else 0
        right = pad_size // 2 + pad_size % 2 if self.centered else pad_size

        return " " * left + value + " " * right


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
