class Tile:
    def __init__(self, suit=None, rank=None):
        self.suit = suit
        self.rank = rank

    def __getitem__(self, index):
        if index == 0:
            return self.suit
        elif index == 1:
            return self.rank

    def __repr__(self):
        return f"{self.suit}{self.rank}" if self.suit and self.rank else "EmptyTile"

    def __lt__(self,other):
        if self.suit != other.suit:
            return self.suit < other.suit
        if self.rank != other.rank:
            return self.rank < other.rank
        return False
    
    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank