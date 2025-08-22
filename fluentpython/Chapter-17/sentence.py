import re
import reprlib


RE_WORD = re.compile(r"\w+")


class Sentence:
    def __init__(self, text: str) -> None:
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index: int) -> str:
        return self.words[index]

    def __len__(self) -> int:
        return len(self.words)

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)

    # def __iter__(self):


s = Sentence(text="Hi I am Vaibhav Hi I am Vaibhav Hi I am VaibhavHi I am Vaibhav")
print(s)
# print(s[2])
print(len(s))

for ele in s:
    print(ele)
