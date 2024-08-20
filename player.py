from tiles import Tile


class Player:
    def __init__(self, player_index):
        self.name = "Player " + str(player_index)
        self.points = 0
        self.hand = []
        self.bonus_tiles = []
        self.player_index = player_index
        self.isHuman = player_index == 1

#completed
    def draw_tile(self, game):
        if len(game.tiles) == 0:
            raise Exception("No more tiles to draw!")
        drawn_tile = game.tiles.pop(0)
        if(self.is_bonus_tile(drawn_tile)):
            self.bonus_tiles.append(drawn_tile)
            self.draw_tile_from_back(game)
        else:
            self.hand.append(drawn_tile)
        self.hand = sorted(self.hand)
      

    def draw_tile_from_back(self, game):
        if len(game.tiles) == 0:
            raise Exception("No more tiles to draw!")
        drawn_tile = game.tiles.pop()
        while(self.is_bonus_tile(drawn_tile)):
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
        tile_index = int(input("Which tile would you like to discard?:"))-1
        tile = self.hand.pop(tile_index)
        game.discard_pile.append((tile, self.player_index))
        print(f"Player {self.player_index} discarded {tile}")


    def check_bonus_tile(self,tile):       
            if tile.suit == "Flower" or tile.suit == "Season":
                print(f"Player {self.player_index} drew a bonus tile: {tile}")
                self.bonus_tiles.append(tile)
                self.hand.remove(tile)
                self.draw_tile_from_back(game)

#TODO but not necessary if we aren't keeping score 
    def update_score(self, points):
        """Update the player's score by a certain number of points."""
        self.points += points

    def __str__(self):
        return f"Player: {self.name}, Hand: {self.hand}"

    def print_vertical_hand(self):
        count = 0
        for row in range(7):
            print(count+1, self.hand[count], "\t\t", count+2, self.hand[count+1])
            count += 2

#TODO player do_turn function implement
'''
draw tile
print vertical hand
discard tile

'''

if __name__ == "__main__":
    player = Player(1)
    print(player)
    tile = Tile("Characters", 1)
    player.add_to_hand(tile)
    player.print_hand()
    player.update_score(10)
    print(player)
