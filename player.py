from tiles import Tile
from utils import *
import random


class Player:
    def __init__(self, player_index):
        self.name = "Player " + str(player_index)
        self.points = 0
        self.hand = []
        self.bonus_tiles = []
        self.player_index = player_index
        self.isHuman = player_index == 1
        self.meld_array = []  #
        self.hasWon = False
        self.suggest_tiles_array = (
            []
        )  # either pung first and then chow [Bamboos9, Dots 5, WindWest, Bamboos5, Bamboos8, Dots2, Dots6 ]
        self.revealed_hand = []  # everythign here has to be added to discard_dict
        self.possible_pungs_array = []
        self.possible_chows_array = []
        self.tiles_to_discard = []

    # Below are win cases:
    # [3 completed melds] [D8 D8 B2 B2]
    # [4 completed melds] [B2]

    def print_tiles_to_discard(self):
        temp_tiles_to_discard = []
        # single tiles of dragons+winds, then single tiles of 1-9
        dragon_wind_list = [t for t in self.hand if t.suit in ["Dragon", "Wind"]]
        for tile in dragon_wind_list:
            if dragon_wind_list.count(tile) == 1:
                temp_tiles_to_discard.append(tile)
        for tile in self.hand:
            if (
                tile.suit in ["Dots", "Characters", "Bamboos"]
                and self.hand.count(tile) == 1
            ):
                possible_chows = [
                    Tile(tile.suit, str(int(tile.rank) + 2)),
                    Tile(tile.suit, str(int(tile.rank) + 1)),
                    Tile(tile.suit, str(int(tile.rank) - 1)),
                    Tile(tile.suit, str(int(tile.rank) - 2)),
                ]
                tiles_count = 0
                for t in possible_chows:
                    if t in self.hand:
                        tiles_count += 1
                if tiles_count == 0:
                    temp_tiles_to_discard.append(tile)
            if (
                tile.suit not in ["Dragon", "Wind"]
                and self.hand.count(tile) == 1
                and self.can_chow(tile) == False
            ):
                temp_tiles_to_discard.append(tile)
        self.tiles_to_discard = temp_tiles_to_discard.copy()
        if self.tiles_to_discard:
            print("Tiles to discard: ", self.tiles_to_discard)
        else:
            print("All tiles are equally viable. Prioritise discarding chow tiles as pairs may be used to win or to pung.")

    # either same suit above or below, or same suit 2 above or below, at least one other tile

    def can_win(self, tile):
        if len(self.meld_array) == 4 and self.hand[0] == tile:
            return True
        elif (
            len(self.meld_array) == 3
            and self.hand[0] == self.hand[1]
            and self.hand[2] == self.hand[3]
            and (tile == self.hand[0] or tile == self.hand[2])
        ):
            return True
        return False

    def can_pung(self, discarded_tile):
        for tile in self.hand:
            if self.hand.count(tile) == 2 and tile == discarded_tile:
                return True
        return False

    def can_chow(self, tile):
        if tile in self.possible_chows_array:
            return True
        else:
            False

    def suggest_tiles(self, discard_dict):
        self.suggest_tiles_array = set()
        self.possible_pungs_array = set()
        self.possible_chows_array = set()
        for tile in self.hand:
            if self.hand.count(tile) == 2 and discard_dict[tile] < 2:
                self.suggest_tiles_array.add(tile)
                self.possible_pungs_array.add(tile)
        for i in range(len(self.hand) - 1):
            if not (self.hand[i].suit in SUITS):
                continue
            if (
                self.hand[i].suit == self.hand[i + 1].suit
                and int(self.hand[i + 1].rank) - int(self.hand[i].rank) == 1
            ):
                lower_rank = int(self.hand[i].rank) - 1
                higher_rank = int(self.hand[i + 1].rank) + 1
                if lower_rank >= 1 and discard_dict[tile] < 3:
                    self.suggest_tiles_array.add(
                        Tile(self.hand[i].suit, str(lower_rank))
                    )
                    self.possible_chows_array.add(
                        Tile(self.hand[i].suit, str(lower_rank))
                    )
                if higher_rank <= 9 and discard_dict[tile] < 3:
                    self.suggest_tiles_array.add(
                        Tile(self.hand[i].suit, str(higher_rank))
                    )
                    self.possible_chows_array.add(
                        Tile(self.hand[i].suit, str(higher_rank))
                    )

            if (
                self.hand[i].suit == self.hand[i + 1].suit
                and int(self.hand[i + 1].rank) - int(self.hand[i].rank) == 2
            ):
                if discard_dict[tile] < 3:
                    self.suggest_tiles_array.add(
                        Tile(self.hand[i].suit, str(int(self.hand[i].rank) + 1))
                    )
                    self.possible_chows_array.add(
                        Tile(self.hand[i].suit, str(int(self.hand[i].rank) + 1))
                    )
        print("Look out for these tiles: ", sorted(list(self.suggest_tiles_array)))

    def check_win(self):
        if len(self.meld_array) == 4 and self.hand[0] == self.hand[1]:
            self.hasWon = True

    def categorise_hand(self):
        # prioritise pungs first
        for current_tile in self.hand:
            if self.hand.count(current_tile) == 3:
                self.meld_array.append([current_tile, current_tile, current_tile])
                for i in range(3):
                    self.hand.remove(current_tile)
        # meld_bools_array = []
        # for i in range(len(self.hand) - 3):
        #     meld_bools_array.append(
        #         is_valid_pung(self.hand[i], self.hand[i + 1], self.hand[i + 2])
        #     )
        # for i, value in enumerate(meld_bools_array):
        #     if value == True:
        #         meld = [self.hand[i], self.hand[i + 1], self.hand[i + 2]]
        #         self.meld_array.append(meld)
        # for meld in self.meld_array: #DODGY LINE
        #     for tile in meld:
        #         if tile in self.hand:
        #             self.hand.remove(tile)

        # now go for chows
        # print(self.hand)
        for current_tile in self.hand:
            if current_tile.suit not in SUITS:
                continue
            meld_temp_array = [current_tile]
            find_tile = Tile(current_tile.suit, str(int(current_tile.rank) + 1))
            if find_tile in self.hand:
                meld_temp_array.append(find_tile)
            if len(meld_temp_array) == 2:
                find_last_tile = Tile(
                    current_tile.suit, str(int(current_tile.rank) + 2)
                )
                if find_last_tile in self.hand:
                    meld_temp_array.append(find_last_tile)
            if len(meld_temp_array) == 3:
                self.meld_array.append(meld_temp_array)
                self.hand.remove(current_tile)
                self.hand.remove(find_tile)
                self.hand.remove(find_last_tile)
        # print(len(self.meld_array) * 3)
        # print(len(self.hand))

        # meld_bools_array = []
        # unique_hand = sorted(list(set(self.hand)))
        # for i in range(len(unique_hand) - 3):
        #     meld_bools_array.append(
        #         is_valid_chow(unique_hand[i], unique_hand[i + 1], unique_hand[i + 2]) #TODO implement 6 77 8 fix, 1234 => 123, 234, while loop removing as you go
        #     )
        #     #D1 D2 D3 D4 => [D1D2D3] [D2D3D4]
        # for i, value in enumerate(meld_bools_array):
        #     if value == True:
        #         meld = [unique_hand[i], unique_hand[i + 1], unique_hand[i + 2]]
        #         self.meld_array.append(meld)
        # for meld in self.meld_array:
        #     for tile in meld:
        #         if tile in self.hand:
        #             self.hand.remove(tile)
        if self.isHuman:
            print(f"Completed melds: {self.meld_array}\n")
            print(f"Current hand: {self.hand} \n")

    # completed
    def draw_tile(self, game):
        if len(game.tiles) == 0:
            raise Exception("No more tiles to draw!")
        drawn_tile = game.tiles.pop(0)
        if self.is_bonus_tile(drawn_tile):
            self.bonus_tiles.append(drawn_tile)
            self.draw_tile_from_back(game)
        else:
            self.hand.append(drawn_tile)
        self.hand = sorted(self.hand)
        if self.isHuman:
            print(f"Player {self.player_index} drew a tile: {drawn_tile}, {self.print_tile_emoji(drawn_tile)}")
        if self.is_bonus_tile(drawn_tile):
            print(
                f"Player {self.player_index} drew a bonus tile: {drawn_tile}. {self.print_tile_emoji(drawn_tile)}"
            )

    # [[Bamboos4, Bamboos5, Bamboos6]] [Bamboos2, Bamboos7, Bamboos8, Characters3, Characters5, Characters7, Characters7, Dots3, Dots8, DragonWhite]
    def draw_tile_from_back(self, game):
        if len(game.tiles) == 0:
            raise Exception("No more tiles to draw!")
        drawn_tile = game.tiles.pop()
        while self.is_bonus_tile(drawn_tile):
            self.bonus_tiles.append(drawn_tile)
            if len(game.tiles) == 0:
                raise Exception("No more tiles to draw!")
            drawn_tile = game.tiles.pop()
        self.hand.append(drawn_tile)
        self.hand.sort()

    def is_bonus_tile(self, tile):
        if tile.suit == "Flower" or tile.suit == "Season":
            # print(f"Player {self.player_index} drew a bonus tile: {tile}")
            return True
        else:
            return False

    def discard_tile(self, game):
        self.print_vertical_hand()

        while True:
            try:
                print(f"Player {self.player_index}")
                tile_index = int(input("Which tile would you like to discard?:")) - 1
                if 0 <= tile_index < len(self.hand):
                    discarded_tile = self.hand[tile_index]
                    game.discard_pile.append((self.hand[tile_index], self.player_index))
                    game.discard_dict[self.hand[tile_index]] += 1
                    self.hand.remove(self.hand[tile_index])
                    break
                else:
                    print(
                        f"Invalid input. Please enter a tile index number between 1 and {len(self.hand)}."
                    )
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        print(f"Player {self.player_index} discarded {discarded_tile}")

    def check_bonus_tile(self, game, tile):
        if tile.suit == "Flower" or tile.suit == "Season":
            print(
                f"Player {self.player_index} drew a bonus tile: {tile} {self.print_tile_emoji(tile)}"
            )
            self.bonus_tiles.append(tile)
            self.hand.remove(tile)
            self.draw_tile_from_back(game)

    def print_tile_emoji(self, tile):
        # Dictionary of all Mahjong tiles with their corresponding Unicode
        tile_emojis = {
            "DragonRed": "\U0001F004",
            "DragonWhite": "\U0001F006",
            "DragonGreen": "\U0001F005",
            "WindEast": "\U0001F000",
            "WindSouth": "\U0001F001",
            "WindWest": "\U0001F002",
            "WindNorth": "\U0001F003",
            "Bamboos1": "\U0001F010",
            "Bamboos2": "\U0001F011",
            "Bamboos3": "\U0001F012",
            "Bamboos4": "\U0001F013",
            "Bamboos5": "\U0001F014",
            "Bamboos6": "\U0001F015",
            "Bamboos7": "\U0001F016",
            "Bamboos8": "\U0001F017",
            "Bamboos9": "\U0001F018",
            "Characters1": "\U0001F007",
            "Characters2": "\U0001F008",
            "Characters3": "\U0001F009",
            "Characters4": "\U0001F00A",
            "Characters5": "\U0001F00B",
            "Characters6": "\U0001F00C",
            "Characters7": "\U0001F00D",
            "Characters8": "\U0001F00E",
            "Characters9": "\U0001F00F",
            "Dots1": "\U0001F019",
            "Dots2": "\U0001F01A",
            "Dots3": "\U0001F01B",
            "Dots4": "\U0001F01C",
            "Dots5": "\U0001F01D",
            "Dots6": "\U0001F01E",
            "Dots7": "\U0001F01F",
            "Dots8": "\U0001F020",
            "Dots9": "\U0001F021",
            "FlowerPlum": "\U0001F022",  # Plum
            "FlowerOrchid": "\U0001F023",  # Orchid
            "FlowerChrysanthemum": "\U0001F024",  # Chrysanthemum
            "FlowerBamboo": "\U0001F025",  # Bamboo
            "SeasonSpring": "\U0001F026",  # Spring
            "SeasonSummer": "\U0001F027",  # Summer
            "SeasonAutumn": "\U0001F028",  # Autumn
            "SeasonWinter": "\U0001F029",  # Winter
        }
        if str(tile) in tile_emojis:
            return tile_emojis[str(tile)]
        else:
            return f"Emoji for {tile} not found."

    def pung(self, game):
        pung_tile = game.discard_pile.pop()[0]
        self.hand.append(pung_tile)
        self.revealed_hand.append([pung_tile, pung_tile, pung_tile])
        self.categorise_hand()
        if self.isHuman:
            self.print_tiles_to_discard()
            self.discard_tile(game)
        else:
            self.discard_tile_AI(game)

    def chow(self, game):
        chow_tile = game.discard_pile.pop()[0]
        self.hand.append(chow_tile)
        old_meld_array = self.meld_array.copy()
        self.categorise_hand()
        for meld in self.meld_array:
            if meld not in old_meld_array:
                self.revealed_hand.append(meld)
        if self.isHuman:
            self.print_tiles_to_discard()
            self.discard_tile(game)
        else:
            self.discard_tile_AI(game)

    # TODO but not necessary if we aren't keeping score
    def update_score(self, points):
        """Update the player's score by a certain number of points."""
        self.points += points

    def __str__(self):
        return f"Player: {self.name}, Hand: {self.hand}"

    def print_vertical_hand(self):
        count = 0
        for row in range(len(self.hand) // 2):
            print(
                count + 1,
                self.hand[count],
                self.print_tile_emoji(self.hand[count]),
                "\t\t\t",
                count + 2,
                self.hand[count + 1],
                self.print_tile_emoji(self.hand[count + 1]),
            )
            count += 2
        if len(self.hand) % 2 == 1:
            print(count + 1, self.hand[-1], self.print_tile_emoji(self.hand[-1]))

    def discard_tile_AI(self, game):
        if len(self.tiles_to_discard) == 0:
            random_index = random.randint(0, len(self.hand) - 1)
            discard_tile = self.hand[random_index]
        else:
            discard_tile = self.tiles_to_discard[0]
        game.discard_pile.append((discard_tile, self.player_index))
        game.discard_dict[discard_tile] += 1
        if discard_tile in self.hand:
            self.hand.remove(discard_tile)
        print(
            f"Player {self.player_index} discarded {discard_tile} {self.print_tile_emoji(discard_tile)}"
        )


"""
draw tile
print vertical hand
discard tile

"""
