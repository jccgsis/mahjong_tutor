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
    turn_num = 0
    gameWon = [p.hasWon for p in players]
    pung_switch = False
    print(f"\nMahjong is a game of matching tiles into melds, groupings of either three identical tiles or a consecutive sequence of three tiles of the same suit. There are 144 tiles in the game, with 3 suits and 7 sets of honours tiles. Players take turns drawing tiles from the deck, or punging or chowing discarded tiles from other players. Punging resets the turn order. \n \nThe goal of the game is to form a complete hand of four melds and a pair, which is known as a basic winning hand. This app is designed to teach how to play Hong Kong mahjong at a level beyond basic rule comprehension. I hope you have fun and are encouraged to play the game in person! - Jack")
    while True not in gameWon:
        print("-----------------------------------------------------------")
        print(f"Turn {turn_num+1}")
        current_player = players[i % len(players)]
        current_player.draw_tile(game)
        current_player.categorise_hand()
        if current_player.can_win(current_player.hand[-1]):
            print(f"Player {current_player.player_index} can win by self-drawing!")
            if current_player.isHuman:
                if input("Do you want to win? (y/n)") == "y":
                    current_player.hasWon = True
                    current_player.categorise_hand()
                    print(f"Player {current_player.player_index} has won!")
                    print(current_player.meld_array)
                    print(current_player.hand)
                    sys.exit()
            else:
                current_player.hasWon = True
                current_player.categorise_hand()
                print(f"Player {current_player.player_index} has won!")
                print(current_player.meld_array)
                print(current_player.hand)
                sys.exit()
        if len(current_player.meld_array) >= 3:
            print(f"Player {current_player.player_index} is close to winning:")
            #print(current_player.revealed_hand)
        if current_player.isHuman:
            current_player.suggest_tiles(game.discard_dict)
            current_player.print_tiles_to_discard()
        if current_player.isHuman:
            current_player.discard_tile(game)
        else:
            #current_player.suggest_tiles(game.discard_dict)
            current_player.discard_tile_AI(game)
        for p in players:
            if len(game.discard_pile) > 0 and p.can_win(game.discard_pile[-1][0]):
                print(f"Player {p.player_index} can win by punging!")
                if p.isHuman:
                    if input("Do you want to win? (y/n)") == "y":
                        p.hand.append(game.discard_pile[-1][0])
                        p.hasWon = True
                        p.categorise_hand()
                        print(f"Player {p.player_index} has won!")
                        print(p.meld_array)
                        print(p.hand)
                        sys.exit()
                else:
                    p.hasWon = True
                    p.hand.append(game.discard_pile[-1][0])
                    p.categorise_hand()
                    print(f"Player {p.player_index} has won!")
                    print(p.meld_array)
                    print(p.hand)
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
                    print(f"Player {p.player_index} punged!")
                    p.pung(game)
                    i = p.player_index
                    pung_switch = True
                    print(p.meld_array) #bots
                    break
        for p in players:
            if len(game.discard_pile) > 0 and p.can_chow(game.discard_pile[-1][0]) and (current_player.player_index == p.player_index - 1 or (current_player.player_index == 4 and p.player_index == 1)):
                print(f"Player {p.player_index} can successfully chow!")
                if p.isHuman:
                    if input("Do you want to chow? (y/n)") == "y":
                        p.chow(game)
                        i += 1
                        break
                else:
                    print(f"Player {p.player_index} chowed!")
                    print(p.hand)
                    p.chow(game)
                    i += 1
                    print(f"Player {p.player_index}'s meld array is: {p.meld_array}")
                    break
        if pung_switch:
            pung_switch = False
            continue
        i += 1
        turn_num += 1

if __name__ == "__main__":
    main()
