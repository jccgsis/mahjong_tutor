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

    def __hash__(self):
        return hash((self.rank, self.suit))

    def __lt__(self,other):
        if self.suit != other.suit:
            return self.suit < other.suit
        if self.rank != other.rank:
            return self.rank < other.rank
        return False
    
    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank
    
    #B1 B2 B3, D1 D2 D3, C5 C6, C7, 
    #First player according to dice rolls, Flower 1 drawn, +1 point
    #Drawing all flower tiles +1 point
    #faan calculator libraries useful only for finished legally winning hands 