import random
from board import create_tiles, list_tiles
from player import Player

# CONSTANTS

NUM_PLAYERS = 4
TILES_PER_PLAYER = 13
STARTING_TOP_OF_PILE = 51
STARTING_BOTTOM_OF_PILE = 143

class MahjongGame:
    def __init__(self):
        self.tiles = create_tiles()
        random.shuffle(self.tiles)
        self.players = [Player(f"Player {i+1}") for i in range(4)]  # Create 4 Player instances
        self.discard_pile = []
        self.top_of_pile = self.tiles[STARTING_TOP_OF_PILE]
        self.bottom_of_pile = self.tiles[STARTING_BOTTOM_OF_PILE]

#TODO implement draw_tile() method
    """
    def draw_tile(self, player_index):
        if len(self.tiles) > 14:  # Reserve some tiles for the dead wall
            tile = self.tiles.pop()
            self.players[player_index].add_to_hand(tile)
        else:
            print("No more tiles to draw!")
    """
    def deal_tiles(self):
        for _ in range(13):  # Each player gets 13 tiles initially
            for i in range(4):
                self.players[i].add_to_hand(self.tiles.pop())


    def shuffle_tiles(self):
        random.shuffle(self.tiles)

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
    #TODO: Implement the show_hands method
    """
    def show_all_hands(self):
        for i, player in enumerate(self.players):
            print(f"Player {i + 1}: {player.show_hand()}
    """
    def list_tiles(self):
        # Implementation similar to what's in board.py
        for tile in self.tiles:
            print(tile)
        print("The number of tiles in game is: ", len(self.tiles))
    def list_abbreviate_tiles(self):
        for tile in self.tiles:
            print(self.abbreviate_tile_name(tile))
        
    #def count_tiles(self):
       # print(len(self.tiles))
# Create a game instance and deal tiles
game = MahjongGame()
game.deal_tiles()
game.shuffle_tiles()
game.list_tiles()
#game.list_abbreviate_tiles()
#game.count_tiles()
"""
def game_loop(game):
    turn = 0
    while len(game.tiles) > 14:  # Continue until no more tiles to draw
        current_player = turn % 4
        print(f"Player {current_player + 1}'s turn:")
        
        game.draw_tile(current_player)
        game.show_hands()
        
        turn += 1

# Run the game loop
game_loop(game)

class Tile:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __getitem__(self, index):
        if index == 0:
            return self.suit
        elif index == 1:
            return self.rank
        else:
            raise IndexError("Index out of range")
"""