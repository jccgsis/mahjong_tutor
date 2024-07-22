import random
import board
import player 
import meld

# CONSTANTS

NUM_PLAYERS = 4
TILES_PER_PLAYER = 13
STARTING_TOP_OF_PILE = 51
STARTING_BOTTOM_OF_PILE = 143

class MahjongGame:
    def __init__(self):
        self.tiles = board.create_tiles()
    def __init__(self, suit='DefaultSuit', rank='DefaultRank'):
        self.suit = suit
        self.rank = rank
        self.players = [player.Player(f"Player {i+1}") for i in range(NUM_PLAYERS)]  # Create 4 Player instances
        self.discard_pile = []
        self.top_of_pile = STARTING_TOP_OF_PILE
        self.bottom_of_pile = STARTING_BOTTOM_OF_PILE
        self.current_player = 1  # Player 1 starts the game   
    def draw_tile(self, current_player):
        tile = self.tiles.pop(self.top_of_pile)
        self.players[current_player].hand.append(tile)
        if self.top_of_pile > self.bottom_of_pile:
            raise Exception("No more tiles to draw!")
        self.top_of_pile += 1
    def draw_tile_from_back(self, current_player):
        tile = self.tiles.pop(self.bottom_of_pile)
        self.players[current_player].hand.append(tile)
        if self.top_of_pile < self.bottom_of_pile:
            raise Exception("No more tiles to draw!")
        self.bottom_of_pile -= 1
#TODO implement discard_tile
    def discard_tile(self, current_player, tile_index):
        tile = self.players[current_player].hand.pop(tile_index)
        self.discard_pile.append(tile)
        print(f"Player {current_player} discarded {tile}")
        return tile
#TODO implement check_bonus_tile
    def check_bonus_tile(self, current_player):   
        for tile in self.players[current_player].hand:
            if tile.suit == "Season" or tile.suit == "Flower":
                        # Your logic here
                print(f"Player {current_player} drew a bonus tile!")
                self.discard_pile.append(tile)
                self.players[current_player].hand.remove(tile)
                self.players[current_player].hand.draw_tile_from_back(current_player)
                    

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
"""
game = MahjongGame()
game.shuffle_tiles()
game.deal_tiles()
game.print_one_player_hand(2)
game.check_bonus_tile(2)
game.draw_tile(2)
#game.print_one_player_hand(2)
#game.list_tiles()
#game.list_abbreviate_tiles()
#game.count_tiles()

TODO: SEE BELOW
def check_win_condition(self, current_player):
def game_loop(game):
    turn = 0
    while len(game.tiles) <= 14:  # Continue until no more tiles to draw
        current_player = turn % 4
        print(f"Player {current_player + 1}'s turn:")
        
        game.draw_tile(current_player)
        game.check_win_condition(current_player)
        
        turn += 1

# Run the game loop
game_loop(game)
"""
def main():
    game = MahjongGame()
    game.shuffle_tiles()
    game.deal_tiles()
    game_loop(game)
