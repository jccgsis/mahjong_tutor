import random
from board import create_tiles

class MahjongGame:
    def __init__(self):
        self.tiles = create_tiles()
        random.shuffle(self.tiles)
        self.players = [[], [], [], []]  # Four players
        self.dead_wall = []

    def draw_tile(self, player_index):
        if len(self.tiles) > 14:  # Reserve some tiles for the dead wall
            tile = self.tiles.pop()
            self.players[player_index].append(tile)
        else:
            print("No more tiles to draw!")

    def deal_tiles(self):
        for _ in range(13):  # Each player gets 13 tiles initially
            for i in range(4):
                self.draw_tile(i)

        # Reserve 14 tiles for the dead wall
        self.dead_wall = self.tiles[-14:]
        self.tiles = self.tiles[:-14]

    # Abbreviation function
    def abbreviate_tile_name(tile_name):
        # Define a mapping for the prefixes
        prefix_mapping = {'Dots': 'D', 'Bamboo': 'B', 'Characters': 'C'}
        # Extract the prefix and the number from the tile name
        for prefix, abbreviation in prefix_mapping.items():
            if tile_name.startswith(prefix):
                # Replace the prefix with its abbreviation and return
                return tile_name.replace(prefix, abbreviation)
        # If the tile name doesn't match any prefix, return it unchanged
        return tile_name

    def show_hands(self):
        for i, player in enumerate(self.players):
            abbreviated_hand = ', '.join(map(lambda tile: self.abbreviate_tile_name(str(tile))))
            print(f"Player {i + 1}'s hand: {abbreviated_hand}")

# Create a game instance and deal tiles
game = MahjongGame()
game.deal_tiles()
game.show_hands()

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
