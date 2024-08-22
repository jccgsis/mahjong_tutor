from tiles import Tile
from utils import *


class Player:
    def __init__(self, player_index):
        self.name = "Player " + str(player_index)
        self.points = 0
        self.hand = []
        self.bonus_tiles = []
        self.player_index = player_index
        self.isHuman = player_index == 1
        self.meld_array = []
        self.hasWon = False
        self.suggest_tiles_array = [] #either pung first and then chow [Bamboos9, Dots 5, WindWest, Bamboos5, Bamboos8, Dots2, Dots6 ]

    # TODO canInterrupt()

    def suggest_tiles(self, discard_dict):
        self.suggest_tiles_array = set()
        for tile in self.hand:
            if self.hand.count(tile) == 2 and discard_dict[tile] < 2:
                self.suggest_tiles_array.add(tile)
        for i in range(len(self.hand)-1):
            if not (self.hand[i].suit in SUITS):
                continue
            if self.hand[i].suit == self.hand[i+1].suit and int(self.hand[i+1].rank) - int(self.hand[i].rank) == 1:
                lower_rank = int(self.hand[i].rank) - 1
                higher_rank = int(self.hand[i+1].rank) + 1
                if lower_rank >= 1 and discard_dict[tile] < 3:
                    self.suggest_tiles_array.add(Tile(self.hand[i].suit, str(lower_rank)))
                if higher_rank <= 9 and discard_dict[tile] < 3:                          
                    self.suggest_tiles_array.add(Tile(self.hand[i].suit, str(higher_rank)))
            if self.hand[i].suit == self.hand[i+1].suit and int(self.hand[i+1].rank) - int(self.hand[i].rank) == 2:
                if  discard_dict[tile] < 3:
                    self.suggest_tiles_array.add(Tile(self.hand[i].suit, str(int(self.hand[i].rank)+1)))
        print("Look out for these tiles: ", sorted(list(self.suggest_tiles_array)))
                
                

    #D1 D1 D1 D2 D3 []
    def check_win(self):
        if len(self.meld_array) == 4 and self.hand[0]==self.hand[1]:
            self.hasWon = True
     
    def categorise_hand(self):
        meld_bools_array = []
        for i in range(len(self.hand) - 3):
            meld_bools_array.append(
                is_valid_pung(self.hand[i], self.hand[i + 1], self.hand[i + 2])
            )
        for i, value in enumerate(meld_bools_array):
            if value == True:
                meld = [self.hand[i], self.hand[i + 1], self.hand[i + 2]]
                self.meld_array.append(meld)
        for meld in self.meld_array:
            for tile in meld:
                if tile in self.hand:
                    self.hand.remove(tile)
        meld_bools_array = []

        unique_hand = sorted(list(set(self.hand)))
        for i in range(len(unique_hand) - 3):
            meld_bools_array.append(
                is_valid_chow(unique_hand[i], unique_hand[i + 1], unique_hand[i + 2]) #TODO implement 6 77 8 fix, 1234 => 123, 234, while loop removing as you go 
            )
            #D1 D2 D3 D4 => [D1D2D3] [D2D3D4]
        for i, value in enumerate(meld_bools_array):
            if value == True:
                meld = [unique_hand[i], unique_hand[i + 1], unique_hand[i + 2]]
                self.meld_array.append(meld)
        for meld in self.meld_array:
            for tile in meld:
                if tile in self.hand:
                    self.hand.remove(tile)
        print(self.meld_array, self.hand)

    # completed
    def draw_tile(self, game):
        if len(game.tiles) == 0:
            raise Exception("No more tiles to draw!")
        drawn_tile = game.tiles.pop(0)
        if self.is_bonus_tile(drawn_tile):
            self.bonus_tiles.append(drawn_tile)
            self.draw_tile_from_back(game)
        else:
            self.hand.append(drawn_tile)
        self.hand = sorted(self.hand)

    def draw_tile_from_back(self, game):
        if len(game.tiles) == 0:
            raise Exception("No more tiles to draw!")
        drawn_tile = game.tiles.pop()
        while self.is_bonus_tile(drawn_tile):
            self.bonus_tiles.append(drawn_tile)
            if len(game.tiles) == 0:
                raise Exception("No more tiles to draw!")
            drawn_tile = game.tiles.pop()
        self.hand.append(drawn_tile)
        self.hand.sort()

    def is_bonus_tile(self, tile):
        if tile.suit == "Flower" or tile.suit == "Season":
            print(f"Player {self.player_index} drew a bonus tile: {tile}")
            return True
        else:
            return False

    def discard_tile(self, game):
        self.print_vertical_hand()
        tile_index = int(input("Which tile would you like to discard?:")) - 1
        tile = self.hand.pop(tile_index)
        game.discard_pile.append((tile, self.player_index))
        game.discard_dict[tile] += 1

        print(f"Player {self.player_index} discarded {tile}")

    def check_bonus_tile(self, tile):
        if tile.suit == "Flower" or tile.suit == "Season":
            print(f"Player {self.player_index} drew a bonus tile: {tile}")
            self.bonus_tiles.append(tile)
            self.hand.remove(tile)
            self.draw_tile_from_back(game)

    # TODO but not necessary if we aren't keeping score
    def update_score(self, points):
        """Update the player's score by a certain number of points."""
        self.points += points

    def __str__(self):
        return f"Player: {self.name}, Hand: {self.hand}"

    def print_vertical_hand(self):
        count = 0
        for row in range(len(self.hand) // 2):
            print(count + 1, self.hand[count], "\t\t", count + 2, self.hand[count + 1])
            count += 2
        if len(self.hand) % 2 == 1:
            print(count + 1, self.hand[-1])


# TODO player do_turn function implement
"""
draw tile
print vertical hand
discard tile

"""
