"""These errors prove the checker sees package types instead of Any."""

from snakemd import Inline, Table

link: str = Inline("unlinked").get_link()
Inline(123)

Table(["head"]).add_row(123)
