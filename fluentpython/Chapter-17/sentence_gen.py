import re
import reprlib

RE_WORD = re.compile(r"\w+")


class Sentence:
    def __init__(self, text: str):
        self.text = text
        self.words = RE_WORD.findall(self.text)

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word


s = Sentence("Hello what's up how are you doing today")
print(s)
it = iter(s)
for ele in s:
    print(ele)
