import os
import pathlib
import sys
from urllib.error import HTTPError
from urllib import request

from generate_docs.repo import LanguageCollection, SampleProgram


def create_md_link(text: str, url: str) -> str:
    """
    Generates a markdown link in the form [text](url).
    :param text: the link text
    :param url: the url to link
    :return: a markdown link
    """
    separator = ""
    return separator.join(["[", text, "]", "(", url, ")"])


def build_language_link(language: LanguageCollection) -> str:
    """
    A handy abstraction for the create_md_link() method which creates a link to a sample programs language page.
    (e.g., https://sample-programs.therenegadecoder.com/languages/c/)
    :param language: the language to link
    :return: a markdown link to the language page if it exists; an empty string otherwise
    """
    if not verify_link(language.sample_program_url):
        markdown_url = ""
    else:
        markdown_url = create_md_link("Here", language.sample_program_url)
    return markdown_url


def build_doc_link(sample_program: SampleProgram, text: str) -> str:
    """
    A handy abstraction for the create_md_link() method which creates a link to a sample programs docs page.
    (e.g., https://sample-programs.therenegadecoder.com/projects/even-odd/c/)
    :param sample_program: the sample program
    :param text: the label for the link
    :return: a markdown link to the docs page if it exists; an empty string otherwise
    """
    if not verify_link(sample_program.sample_program_doc_url):
        markdown_url = f":warning: {create_md_link(text, sample_program.sample_program_issue_url)}"
    else:
        markdown_url = f":white_check_mark: {create_md_link(text, sample_program.sample_program_doc_url)}"
    return markdown_url


def build_req_link(sample_program: SampleProgram) -> str:
    """
    A handy abstraction for the create_md_link() method which creates a link to a sample programs docs page.
    (e.g., https://sample-programs.therenegadecoder.com/projects/even-odd/c/)
    :param sample_program: the sample program
    :return: a markdown link to the docs page if it exists; an empty string otherwise
    """
    if not verify_link(sample_program.sample_program_req_url):
        print(f"{sample_program.file_name} is not currently supported by this repo.")
        sys.exit(1)
    else:
        return f"{create_md_link('Requirements', sample_program.sample_program_req_url)}"


def verify_link(url: str) -> bool:
    """
    Verifies that a URL is a valid URL.
    :param url: a website URL
    :return: True if the URL is valid; False otherwise
    """
    req = request.Request(url)
    req.get_method = lambda: 'HEAD'
    print(f"Trying: {url}")
    try:
        request.urlopen(req)
        print(f"\tVALID")
        return True
    except HTTPError:
        print(f"\tINVALID")
        return False


class MarkdownPage:
    def __init__(self, name: str):
        self.name: str = name
        self.ext = ".md"
        self.wiki_url_base: str = "/jrg94/sample-programs/wiki/"
        self.content = list()

    def __str__(self):
        return f"{self.name}\n{self._build_page()}"

    def _build_page(self):
        return "\n".join(self.content)

    def add_content(self, *lines: str):
        self.content.extend(lines)

    def add_table_header(self, *args):
        column_separator = " | "
        header = column_separator.join(args)
        divider = column_separator.join(["-----"] * len(args))
        self.content.append(header)
        self.content.append(divider)

    def add_table_row(self, *args):
        column_separator = " | "
        row = column_separator.join(args)
        self.content.append(row)

    def add_section_break(self):
        self.content.append("")

    def output_page(self, dump_dir):
        pathlib.Path(dump_dir).mkdir(parents=True, exist_ok=True)
        output_file = open(os.path.join(dump_dir, self._get_file_name()), "w+")
        output_file.write(self._build_page())
        output_file.close()

    def _get_file_name(self):
        separator = "-"
        file_name = f"{separator.join(self.name.split())}{self.ext}"
        return file_name
