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
        drawn_tile = self.tiles.pop(0)
        self.hand.append(drawn_tile)
        if len(game.tiles) == 0:
            raise Exception("No more tiles to draw!")

    def draw_tile_from_back(self, game):
        drawn_tile = game.tiles.pop()
        self.hand.append(drawn_tile)
        if len(game.tiles) == 0:
            raise Exception("No more tiles to draw!")
   

    def discard_tile(self, game, tile_index):
        tile = self.hand.pop(tile_index)
        game.discard_pile.append((tile, self.player_index))
        print(f"Player {self.player_index} discarded {tile}")

    def check_bonus_tile(self):
        for tile in self.hand:
            if tile.suit == "Flower" or tile.suit == "Season":
                print(f"Player {self.player_index} drew a bonus tile: {tile}")
                self.bonus_tiles.append(tile)
                self.hand.remove(tile)

#TODO but not necessary if we aren't keeping score 
    def update_score(self, points):
        """Update the player's score by a certain number of points."""
        self.points += points

    def __str__(self):
        return f"Player: {self.name}, Hand: {self.hand}"


if __name__ == "__main__":
    player = Player(1)
    print(player)
    tile = Tile("Characters", 1)
    player.add_to_hand(tile)
    player.print_hand()
    player.update_score(10)
    print(player)
