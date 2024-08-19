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

