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
        self.remaining_tiles = len(tiles)
        self.discard_pile = []
        self.current_player = 1  # Player 1 starts the game
    
    def deal_tiles(self, players):
        for _ in range(13):  # Each player gets 13 tiles initially
            for i in range(4):
                players[i].draw_tile(self)

   
    def shuffle_tiles(self):
        random.shuffle(self.tiles)

    
        
    #def count_tiles(self):
       # print(len(self.tiles))
# Create a game instance and deal tiles

#game.list_tiles()
#game.list_abbreviate_tiles()
#game.count_tiles()
"""
TODO: check_win_condition()
def check_win_condition(self, current_player):


'''
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

"""
Interruption Priority Order: Win > Pung (any player's turn end) > Chow (preceeding player's turn end)

Game Loop Psuedocode:
While(!gameover){
    TurnLoop
    if interruption:
        interrupting player's turn
    
}
Turn Loop Pseudocode:
    Draw tile
    Discard tile
    Next player turn

"""