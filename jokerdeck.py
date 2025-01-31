from playingcard import PlayingCard
from carddeck import CardDeck

class JokerDeck(CardDeck): # JokerDeck inherits from CardDeck
    def _make_deck(self):
        super()._make_deck()  # call parent class method
        for joker_number in range(1, 3):
            joker = PlayingCard(f"Joker{joker_number}", "Joker")
            self._cards.append(joker)

if __name__ == "__main__":
    j = JokerDeck()
    j.shuffle()
    print(f"{j.cards = }")
    for i in range(10):
        print(j.draw())
    print()