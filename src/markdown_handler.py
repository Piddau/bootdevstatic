import re
from enum import Enum

class BlockTypes(Enum):
    PARAGRAPH = "paragraph"
    HEADER = "header"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    CODE = "code"
    QUOTE = "quote"

def markdown_to_blocks(markdown):
    strings = markdown.split("\n\n")
    blocks = [s.strip() for s in strings if s.strip()]
    return blocks

def block_to_block_type(markdown):
    header_re = r"^#+\s"
    unordered_list_re = r"^(\s*[-\*\+]\s+)+"
    ordered_list_re = r"^(\s*\d+\.\s+)+"
    code_re = r"^```[\s\S]*```$"
    quote_re = r"^>\s"

    if re.match(header_re, markdown):
        return BlockTypes.HEADER
    elif re.match(unordered_list_re, markdown):
        return BlockTypes.UNORDERED_LIST
    elif re.match(ordered_list_re, markdown):
        return BlockTypes.ORDERED_LIST
    elif re.match(code_re, markdown):
        return BlockTypes.CODE
    elif re.match(quote_re, markdown):
        return BlockTypes.QUOTE
    else:
        return BlockTypes.PARAGRAPH