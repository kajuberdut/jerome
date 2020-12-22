import re
import typing as t

import dataclasses


@dataclasses.dataclass
class StringReplacer(object):
    """
    Given a replacement map, instantiate a StringReplacer.
    :param dict replacements: replacement dictionary {value to find: value to replace}
    """

    replacements: t.Dict[str, str]

    def __post_init__(self):
        # Place longer ones first to keep shorter substrings from matching where the longer ones should take place
        # For instance given the replacements {'ab': 'AB', 'abc': 'ABC'} against the string 'hey abc', it should produce
        # 'hey ABC' and not 'hey ABc'
        sorted_replacement_keys = sorted(self.replacements, key=len, reverse=True)
        escaped_replacement_keys = [re.escape(key) for key in sorted_replacement_keys]

        # Create a big OR regex that matches any of the substrings to replace
        self.pattern = re.compile("|".join(escaped_replacement_keys))

    def process(self, string: str) -> str:
        """
        Process the given string by replacing values as configured
        :param str string: string to perform replacements on
        :rtype: str
        """
        # For each match, look up the new string in the replacements via the old string
        return self.pattern.sub(lambda match: self.replacements[match.group(0)], string)
