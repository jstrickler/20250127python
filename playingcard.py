"""
   playingcard -- provide Playing Card Class
"""
class PlayingCard:  # inherits from 'object'
    """
     Playing Card -- represent one standard playing card

     Synopsis: 
     c = PlayingCard(RANK, SUIT)
    """
    def __init__(self, rank, suit):
        self._rank = rank  # private BY CONVENTION
        self._suit = suit

    # getter property
    @property
    def rank(self):
        """
        Card rank from 2 through A
        """
        return self._rank

    # getter property
    @property
    def suit(self):
        """
        Card suit (clubs, diamonds, hearts, or spades)
        """
        return self._suit

    def __str__(self):
        return f"{self.rank}-{self.suit}"

    def __repr__(self):
        return f"PlayingCard('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    pc = PlayingCard("10", "Diamonds")  # call class initializer (AKA constructor)
    print(f"pc is {pc}")  # str()
    print(f"{pc = }")     # repr()
    print(f"{type(pc) = }")
    print(f"{pc.rank = }")
    print(f"{pc.suit = }")
