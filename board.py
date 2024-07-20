class Tile:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.suit}{self.value}"

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
    
    return tiles
