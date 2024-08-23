from tiles import Tile

# Define suits
SUITS = ['Characters', 'Bamboos', 'Dots'] #3 suits * 1-9 numbers * 4 tiles = 108 ONLY POSSIBLE CHOW 
WINDS = ['East', 'South', 'West', 'North'] #4 winds * 4 tiles = 16
DRAGONS = ['Red', 'Green', 'White'] #3 dragons * 4 tiles = 12
FLOWERS = ['Plum', 'Orchid', 'Chrysanthemum', 'Bamboo'] #4 flowers = 4
SEASONS = ['Spring', 'Summer', 'Autumn', 'Winter'] #4 seasons = 4

# Create a full set of tiles
def create_tiles():
    
#example hand D1, D1, D1, D2, D3, etc.'''
#discard pile D1, D4, D4, D4i am g

    tiles = []
    for suit in SUITS:
        for value in range(1, 10):
            for _ in range(4):  # Each tile appears 4 times
                tiles.append(Tile(suit, str(value)))
    
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

def is_valid_pair(tile1, tile2):
    if(tile1 == tile2):
        return True
    else:
        return False

def is_valid_meld(tile1, tile2, tile3):
    if(is_valid_pung(tile1, tile2, tile3) or is_valid_chow(tile1, tile2, tile3)):
        return True
    return False

def is_valid_pung(tile1, tile2, tile3):
    if(tile1 == tile2 == tile3):
        return True
    return False

def is_valid_chow(tile1, tile2, tile3):
    if(tile1.suit in SUITS and tile1.suit == tile2.suit == tile3.suit):
            arranged = sorted([tile1,tile2,tile3])
            if (int(arranged[0].rank) == int(arranged[1].rank)-1 == int(arranged[2].rank)-2):
                return True
            else:
                return False
    else:
        return False
    
#TODO def can_pung(discarded_tile)
#TODO def can_chow(discarded_tile)
#TODO def can_win(discarded_tile)
        
    
    
'''
#TODO sort hand by melds
D1, D1, D1, D2, D3
Input: starting hand array 
# Algorithm: look for completed pungs first, then completed chows. 2 melds
# PUt those in a finishedarray[]. Then find individual tiles and put them in a want_to_discard[]
# then identify if remaining tiles are chow_pair() or pung_pair
# pung_pair is isValidPair
have an array for wanted_tiles[]
# if chow_pair, place missing tiles in wanted_tiles
# if pung_pair, place tile in wanted_tiles
#each player should have an int of 4 melds and 1 pair

def sort_hand(self):

ACTUAL ARRAYS
hand []
bonus_tiles []

UTIL ARRAYS

related_tiles [] = related_tile_sweep(hand)
completed_meld_array [] = 3tiles_related_sweep(related_tiles)
wanted_tiles [] = PUNG MISSING or CHOW MISSING
tiles_to_discard [] = !relatedTile


#TODO is_valid_pair()

def is_valid_pair():

#TODO is_meld_double():

D1, D1, want D1
B7, B8, want B9
    return D1


#TODO print_tile_emoji
'''