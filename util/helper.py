import re


def remove_spaces(s: str) -> str:
    """Replaces multiple whitespaces with a single space."""
    return re.sub(" +", " ", s.replace("\t", " ")).replace(" \n ", "\n")


def remove_spaces_concisely(s: str) -> str:
    """Convert every pdf page to a single line in the output."""
    return re.sub("\s+", " ", s).replace(" \n", "\n")


def hello():
    print("Hello World")
