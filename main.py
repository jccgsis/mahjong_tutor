from game import MahjongGame
from utils import list_tiles, create_tiles
from tiles import Tile
from player import Player
import sys


def initialise_game():
    return


def main():
    players = [Player(i + 1) for i in range(4)]  # Create 4 Player instances

    game = MahjongGame(create_tiles())
    game.shuffle_tiles()
    game.deal_tiles(players)
    i = 0
    gameWon = [p.hasWon for p in players]
    pung_switch = False
    while True not in gameWon:
        print("-----------------------------------------------------------")
        current_player = players[i % len(players)]
        current_player.draw_tile(game)
        current_player.categorise_hand()
        current_player.suggest_tiles(game.discard_dict)
        #current_player.print_tiles_to_discard()
        current_player.discard_tile(game)
        print(game.discard_pile)
        for p in players:
            if len(game.discard_pile) > 0 and p.can_win(game.discard_pile[-1][0]):
                print(f"Player {p.player_index} can win!")
                if input("Do you want to win? (y/n)") == "y":
                    p.hasWon = True
                    print(f"Player {p.player_index} has won!")
                    print(p.meld_array)
                    sys.exit()
        for p in players:
            if len(game.discard_pile) > 0 and p.can_pung(game.discard_pile[-1][0]):
                print(f"Player {p.player_index} can pung!")
                if input("Do you want to pung? (y/n)") == "y":
                    p.pung(game)
                    i = p.player_index
                    pung_switch = True
                    break
        for p in players:
            if len(game.discard_pile) > 0 and p.can_chow(game.discard_pile[-1][0]) and current_player.player_index == p.player_index - 1:
                print(f"Player {p.player_index} can chow!")
                if input("Do you want to chow? (y/n)") == "y":
                    p.chow(game)
                    i += 1
                    break
        if pung_switch:
            pung_switch = False
            continue
        i += 1
    """
    #TODO Tiles to discard 
    #   
    #TODO interrupt()
    #TODO 
    """


if __name__ == "__main__":
    main()
