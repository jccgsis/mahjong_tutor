class Player:
	def __init__(self, name, score=0):
		self.name = name
		self.points = score
		self.hand = []
		self.wind = None

	def add_to_hand(self, tile):
		"""Add a tile to the player's hand."""
		self.hand.append(tile)

	def discard_tile(self, tile):
		"""Remove a tile from the player's hand if it exists."""
		if tile in self.hand:
			self.hand.remove(tile)

	def show_hand(self):
		"""Display the tiles in the player's hand."""
		return ', '.join(self.hand)

	def update_score(self, points):
		"""Update the player's score by a certain number of points."""
		self.score += points

	def __str__(self):
		return f"Player: {self.name}, Score: {self.score}, Hand: {self.show_hand()}"