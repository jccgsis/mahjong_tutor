from tiles import Tile

class Player:
	def __init__(self, player_index):
		self.name = "Player " + str(player_index)
		self.points = 0
		self.hand = []
		self.bonus_tile = []
		self.players = []
		self.wind = None	
		self.isHuman = (player_index == 1)

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
                    
	def add_to_hand(self, tile):
		"""Add a tile to the player's hand."""
		self.hand.append(tile)

	def discard_tile(self, tile):
		"""Remove a tile from the player's hand if it exists."""
		if tile in self.hand:
			self.hand.remove(tile)
			
	def print_hand(self):
		"""Print the contents of the player's hand."""
		for tile in self.hand:
			print(tile)

	def update_score(self, points):
		"""Update the player's score by a certain number of points."""
		self.points += points

	def __str__(self):
		return f"Player: {self.name}, Points: {self.points}, Hand: {self.print_hand()}"
	
if __name__ == "__main__":
	player = Player(1)
	print(player)
	tile = Tile('Characters', 1)
	player.add_to_hand(tile)
	player.print_hand()
	player.update_score(10)
	print(player)