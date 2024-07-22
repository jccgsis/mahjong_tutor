from board import Tile

class Player:
	def __init__(self, player_index):
		self.name = "Player " + str(player_index)
		self.points = 0
		self.hand = [Tile() for _ in range(14)]
		self.wind = None	
		self.isHuman = (player_index == 1)
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
		self.score += points

	def __str__(self):
		return f"Player: {self.name}, Score: {self.score}, Hand: {self.show_hand()}"