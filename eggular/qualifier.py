import sys
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
        self.labels = [str(label) for label in labels] if labels is not None else []
        self.centered = centered

        # We can always assume all rows will have the same # of entries
        self.total_columns = len(rows[0])
        self.col_sizes: List[int] = [0 for _ in range(self.total_columns)]

        self.table_string = ""

    def render_table(self) -> str:
        """Runs all steps to make a table"""
        self._find_column_sizes()

        table_rows = self._table_border(*self.TOP_BORDER)

        if self.labels:
            table_rows += "\n" + "\n".join(self._table_rows([self.labels]))
            table_rows += "\n" + self._table_border(*self.MID_BORDER)

        table_rows += "\n" + "\n".join(self._table_rows(self.rows))

        table_rows += "\n" + self._table_border(*self.BOT_BORDER)

        return table_rows

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
        table_top = f"{left}{mid}"

        for idx, size in enumerate(self.col_sizes):
            if idx == 0:
                table_top = f"{left}{mid * (size + 2)}"
            else:
                table_top += f"{seg}{mid * (size + 2)}"
        return f"{table_top}{right}"

    def _table_rows(self, rows: List[List[str]]) -> List[str]:
        """Generates rows of table values"""
        table_values: List[str] = []
        for row in rows:
            table_row = ""
            for idx, column_value in enumerate(row):
                padded_value = self._pad_value(column_value, idx)
                if idx == 0:
                    table_row += f"{self.VERT} {padded_value}"
                else:
                    table_row += f" {self.VERT} {padded_value}"

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
    from tests.qualifier_test import SAMPLE01_ROWS
    from tests.qualifier_test import SAMPLE02_ROWS
    from tests.qualifier_test import SAMPLE02_LABELS
    from tests.qualifier_test import SAMPLE03_ROWS
    from tests.qualifier_test import SAMPLE03_LABELS

    print(make_table(SAMPLE01_ROWS))
    print("\n\n")
    print(make_table(SAMPLE02_ROWS, SAMPLE02_LABELS))
    print("\n\n")
    print(make_table(SAMPLE03_ROWS, SAMPLE03_LABELS, True))
    sys.exit(0)
