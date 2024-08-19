from game import MahjongGame
from utils import list_tiles, create_tiles
from tiles import Tile

def main():
    game = MahjongGame(create_tiles())
    game.shuffle_tiles()
    game.deal_tiles()
    game.print_one_player_hand(1)
    game.print_one_player_hand(2)
    '''
    game.list_tiles()
    game.list_abbreviate_tiles()
    game.count_tiles()
    game.check_win_condition(2)
    #game.game_loop()
    '''