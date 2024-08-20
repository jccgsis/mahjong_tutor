from game import MahjongGame
from utils import list_tiles, create_tiles, print_one_player_hand
from tiles import Tile
from player import Player

def initialise_game():
    return 

def main():
    players = [Player(i+1) for i in range(4)]  # Create 4 Player instances

    game = MahjongGame(create_tiles())
    game.shuffle_tiles()
    game.deal_tiles(players)
    for player in players:
        print(player)
        player.check_bonus_tile()
        while len(player.hand) < 13:
            player.draw_tile_from_back(game)
        print(player)
    '''
    game.list_tiles()
    game.list_abbreviate_tiles()
    game.count_tiles()
    game.check_win_condition(2)
    #game.game_loop()
    '''

if __name__ == "__main__":
    main()