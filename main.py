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
        if current_player.isHuman:
            current_player.suggest_tiles(game.discard_dict)
            current_player.print_tiles_to_discard()
        if current_player.isHuman:
            current_player.discard_tile(game)
        else:
            current_player.discard_tile_AI(game)
        for p in players:
            if len(game.discard_pile) > 0 and p.can_win(game.discard_pile[-1][0]):
                print(f"Player {p.player_index} can win!")
                if p.isHuman:
                    if input("Do you want to win? (y/n)") == "y":
                        p.hand.append(game.discard_pile[-1][0])
                        p.hasWon = True
                        p.categorise_hand()
                        print(f"Player {p.player_index} has won!")
                        print(p.meld_array)
                        sys.exit()
                else:
                    p.hasWon = True
                    p.hand.append(game.discard_pile[-1][0])
                    p.categorise_hand()
                    print(f"Player {p.player_index} has won!")
                    print(p.meld_array)
                    sys.exit()
        for p in players:
            if len(game.discard_pile) > 0 and p.can_pung(game.discard_pile[-1][0]):
                print(f"Player {p.player_index} can pung!")
                if p.isHuman:
                    if input("Do you want to pung? (y/n)") == "y":
                        p.pung(game)
                        i = p.player_index
                        pung_switch = True
                        break
                else:
                    p.pung(game)
                    i = p.player_index
                    pung_switch = True
                    print(p.meld_array) #bots
                    break
        for p in players:
            if len(game.discard_pile) > 0 and p.can_chow(game.discard_pile[-1][0]) and current_player.player_index == p.player_index - 1:
                print(f"Player {p.player_index} can chow!")
                if p.isHuman:
                    if input("Do you want to chow? (y/n)") == "y":
                        p.chow(game)
                        i += 1
                        break
                    else:
                        p.chow(game)
                        i += 1
                        print(p.meld_array)
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
