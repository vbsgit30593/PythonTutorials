import reprlib
import re


RE_WORD = re.compile(r"\w+")


class SentenceGenerate:
    def __init__(self, text: str):
        self.text = text

    def __repr__(self):
        return "SentenceGenerate(%s)" % reprlib.repr(self.text)

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))


sen = SentenceGenerate("asdasd asdSADsada ADadsaddasa dasff")
print(sen)

for word in sen:
    print(word)
