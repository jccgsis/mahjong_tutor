from game import MahjongGame
from utils import list_tiles, create_tiles
from tiles import Tile
from player import Player

def initialise_game():
    return 

def main():
    players = [Player(i+1) for i in range(4)]  # Create 4 Player instances

    game = MahjongGame(create_tiles())
    game.shuffle_tiles()
    game.deal_tiles(players)
    i = 0
    while(True):
            player = players[i % len(players)]
            for p in players:
                 if len(game.discard_pile) > 0 and p.can_win(game.discard_pile[-1][0]):
                      print(f"Player {p.player_index} can win!")
                      #
                      break
            for p in players:
                if len(game.discard_pile) > 0 and p.can_pung(game.discard_pile[-1][0]):
                    print(f"Player {p.player_index} can pung!")
                    break
            for p in players:
                 if len(game.discard_pile) > 0 and p.can_chow(game.discard_pile[-1][0]):
                     print(f"Player {p.player_index} can chow!")
                     break
            player.draw_tile(game)
            player.categorise_hand()
            player.suggest_tiles(game.discard_dict)
            player.discard_tile(game)
            print(game.discard_pile)
            i += 1
    '''
    #TODO Player turn int
    #TODO Tiles to discard prioritised  
    #TODO interrupt()
    #TODO Game Logic: Player actions: discard, Interrupt[Win, Pung, Chow]
    '''

if __name__ == "__main__":
    main()