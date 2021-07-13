import os
import pathlib
from typing import Iterable
from urllib.error import HTTPError
from urllib import request


class Header:
    def __init__(self, text: str, level: int) -> None:
        self.text: str = text
        self.level: int = level

    def __str__(self) -> str:
        return f"{'#' * self.level} {self.text}"

    def promote(self):
        if self.level > 1:
            self.level -= 1

    def demote(self):
        if self.level < 6:
            self.level += 1


class OrderedList:
    def __init__(self, items: Iterable) -> None:
        self.items: Iterable = items

    def __str__(self) -> str:
        return "\n".join([f"{index + 1}. {item}" for index, item in enumerate(self.items)])


class Link:
    def __init__(self, text: str, url: str) -> None:
        self.text = text
        self.url = url

    def __str__(self) -> str:
        return f"[{self.text}]({self.url})"

    def verify_link(self) -> bool:
        """
        Verifies that a URL is a valid URL.
        :return: True if the URL is valid; False otherwise
        """
        req = request.Request(self.url)
        req.get_method = lambda: 'HEAD'
        print(f"Trying: {self.url}")
        try:
            request.urlopen(req)
            print(f"\tVALID")
            return True
        except HTTPError:
            print(f"\tINVALID")
            return False


class Table:
    def __init__(self, header: Iterable, body: Iterable[Iterable], footer: Iterable) -> None:
        self.header = header
        self.body = body
        self.footer = footer

    def __str__(self) -> str:
        rows = list()
        rows.append(self.header)
        rows.extend(self.body)
        rows.append(self.footer)
        return f"{' | '.join(rows)}"

    def verify(self):
        assert len({len(i) for i in self.body}) == 1
        assert len(self.header) == len(self.footer) == len(self.body[0])


class Text:
    def __init__(self) -> None: 
        self.content = list()

    def __str__(self) -> str:
        return " ".join(self.content)        

    def add(self, text, style=None):
        if style == "bold":
            text = f"**{text}**"
        elif style == "italics":
            text = f"*{text}*"
        self.content.add(text)

class Document:

    def __init__(self, name: str) -> None:
        self.name = name
        self.ext = ".md"
        self.contents = list()

    def __str__(self):
        return f"{self.name}\n{self._build_page()}"

    def add_element(self, element):
        self.contents.append(element)

    def add_header(self, text, level):
        self.contents.append(Header(text, level))

    def add_text(self, text: str):
        self.contents.append(Text(text))

    def output_page(self, dump_dir):
        pathlib.Path(dump_dir).mkdir(parents=True, exist_ok=True)
        output_file = open(os.path.join(dump_dir, self._get_file_name()), "w+")
        output_file.write(self._build_page())
        output_file.close()

    def _build_page(self):
        return "\n\n".join(self.content)

    def _get_file_name(self):
        separator = "-"
        file_name = f"{separator.join(self.name.split())}{self.ext}"
        return file_name
