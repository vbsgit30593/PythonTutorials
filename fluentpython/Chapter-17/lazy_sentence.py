import re
import reprlib

RE_WORD = re.compile(r"\w+")


class SentenceLazy:
    def __init__(self, text: str):
        self.text = text

    def __repr__(self):
        return "SentenceLazy(%s)" % reprlib.repr(self.text)

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()


s = SentenceLazy("HELOSDSDS  ASDASFAF AFAWWFAFSFAF")
for ele in s:
    print(ele)
