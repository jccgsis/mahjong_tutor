class Tile:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __getitem__(self, index):
        if index == 0:
            return self.suit
        elif index == 1:
            return self.rank

    def __repr__(self):
        return f"{self.suit}{self.rank}"

# Define suits
SUITS = ['Characters', 'Bamboos', 'Dots']
WINDS = ['East', 'South', 'West', 'North']
DRAGONS = ['Red', 'Green', 'White']
FLOWERS = ['Plum', 'Orchid', 'Chrysanthemum', 'Bamboo']
SEASONS = ['Spring', 'Summer', 'Autumn', 'Winter']

# Create a full set of tiles
def create_tiles():
    tiles = []
    for suit in SUITS:
        for value in range(1, 10):
            for _ in range(4):  # Each tile appears 4 times
                tiles.append(Tile(suit, value))
    
    for wind in WINDS:
        for _ in range(4):
            tiles.append(Tile('Wind', wind))
    
    for dragon in DRAGONS:
        for _ in range(4):
            tiles.append(Tile('Dragon', dragon))
    
    for flower in FLOWERS:
        tiles.append(Tile('Flower', flower))
    
    for season in SEASONS:
        tiles.append(Tile('Season', season))
    print("The number of generated tiles is: ", len(tiles))
    return tiles

def list_tiles():
    for tile in tiles:
        print(tile)  # Print each tile using its __repr__ method

#list_tiles()