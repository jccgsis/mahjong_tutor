import random
import player 
import meld
from tiles import Tile
from flask import Flask
from utils import create_tiles
# CONSTANTS

NUM_PLAYERS = 4
TILES_PER_PLAYER = 13
STARTING_TOP_OF_PILE = 51
STARTING_BOTTOM_OF_PILE = 143

class MahjongGame:
    def __init__(self, tiles):
        self.tiles = tiles
        self.players = [player.Player(f"Player {i+1}") for i in range(NUM_PLAYERS)]  # Create 4 Player instances
        self.discard_pile = []
        self.top_of_pile = STARTING_TOP_OF_PILE
        self.bottom_of_pile = STARTING_BOTTOM_OF_PILE
        self.current_player = 1  # Player 1 starts the game
    
    


    def print_all_players_hands(self):
        for i, player in enumerate(self.players):
            print(f"Player {i + 1}: {player.print_hand()}")
    def print_one_player_hand(self, player_index):
        print(f"Player {player_index}'s hand: ")
        print(self.players[player_index].print_hand())
    def deal_tiles(self):
        for _ in range(TILES_PER_PLAYER):  # Each player gets 13 tiles initially
            for i in range(NUM_PLAYERS):
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

game = MahjongGame(create_tiles())
game.shuffle_tiles()
game.deal_tiles()
game.print_one_player_hand(2)

#game.list_tiles()
#game.list_abbreviate_tiles()
#game.count_tiles()
"""
TODO: SEE BELOW
def check_win_condition(self, current_player):
def game_loop(game):
    turn = 0
    while len(game.tiles) <= 14:  # Continue until no more tiles to draw
        current_player = turn % 4
        print(f"Player {current_player + 1}'s turn:")
        
        game.draw_tile(current_player)
        game.check_bonus_tile(current_player)
        game.check_win_condition(current_player)
        game.discard_tile(current_player, 0)
        turn += 1
        game.check_
# Run the game loop
game_loop(game)

"""

"""
4 tiles * 9 suits * 4 = 144 tiles

def main():
    game = MahjongGame()
    game.shuffle_tiles()
    game.deal_tiles()
    game_loop(game)
"""
