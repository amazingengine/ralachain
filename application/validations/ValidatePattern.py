from enum import Enum
import re


class ValidatePattern(Enum):
    # 半角英数字 + - + _
    URLKEY_PATTERN = re.compile(r'[\w+]+')
    # 日本語
    MULTIBYTE_PATTERN = re.compile(r'[\x01-\x7E]+')
