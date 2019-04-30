import re

from validations.ValidatePattern import ValidatePattern


class Validation(object):
    def urlvalue(self, key):
        match = re.fullmatch(ValidatePattern.URLKEY_PATTERN.value, key)
        if match:
            return key
        else:
            raise ValueError(
                f'{key} is a string outside "{ValidatePattern.URLKEY_PATTERN.value}"pattern:.')

    def multi_byte(self, key):
        match = re.fullmatch(ValidatePattern.MULTIBYTE_PATTERN.value, key)
        if match:
            return key
        else:
            raise ValueError(
                f'"{key}" is a multi-byte pattern.If you want to use multibyte,\
please specify the optionof ini file.'
            )
