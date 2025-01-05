import collections
import enum
from random import choice

# Creates a class of objects which contain only attrs and
# no methods
# This creates a Card class which has a Card object which contains
# only rank and suit attr
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchCard:
    ranks = [str(rank) for rank in range(2,11)] + list('JQKA')
    suits = "spades diamonds clubs hearts".split()
    def __init__(self):
        self._cards = [
            Card(rank, suit)
                for suit in self.suits 
                    for rank in self.ranks
        ]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

# Since we have the getitem and len in place, we can do the following
deck = FrenchCard()
print (deck[0])
print (len(deck))
print (choice(deck))
print (deck[2:10])

for idx, d in enumerate(deck):
    print (f"DECK {idx} : {d}")

print (Card('Q', 'hearts') in deck)