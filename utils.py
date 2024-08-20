from tiles import Tile

# Create a full set of tiles
def create_tiles():
    # Define suits
    SUITS = ['Characters', 'Bamboos', 'Dots']
    WINDS = ['East', 'South', 'West', 'North']
    DRAGONS = ['Red', 'Green', 'White']
    FLOWERS = ['Plum', 'Orchid', 'Chrysanthemum', 'Bamboo']
    SEASONS = ['Spring', 'Summer', 'Autumn', 'Winter']
    
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

def list_tiles(game):
    for tile in game.tiles:
        print(tile)  # Print each tile using its __repr__ method

#TODO count_tiles()
def count_tiles(game):
    return len(game.tiles)

def print_all_players_hands(players):
        for player in players:
            print(player)

#TODO check functionality of abbreviatoins 
def abbreviate_tile_name(self, tile):
        # Extract the suit from the tile object
        suit = tile.suit

        # Abbreviate the suit
        if suit == "Bamboos":
            suit = "B"
        elif suit == "Characters":
            suit = "C"
        elif suit == "Dots":
            suit = "D"
        elif suit == "Wind":
            suit = "W"  

        # Return the abbreviated tile name
        return f"{suit}{tile.rank}"
 
    
def list_abbreviate_tiles(self):
    for tile in self.tiles:
        print(self.abbreviate_tile_name(tile))

#TODO sort hand by melds

def sort_hand(self):