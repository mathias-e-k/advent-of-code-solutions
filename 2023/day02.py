from utils import read_file_to_list




def split_game(game: str) -> list:
    # This could have been a class maybe
    output = []
    game = game.partition(": ")[2]
    for subset in game.split("; "):
        subset_dicts = []
        colors = subset.split(", ")
        for color_value_pair in colors:
            value = int(color_value_pair.partition(" ")[0])
            color = color_value_pair.partition(" ")[2]
            subset_dicts.append([color, value])
        output.append(subset_dicts)
    return output


def count_possible_games(games: list) -> int:
    bag = {"red":12, "green":13, "blue":14}
    total = 0
    for id, game in enumerate(games):
        id += 1
        possible_game = True
        formatted_game = split_game(game)
        for subset in formatted_game:
            for color in subset:
                if color[1] > bag[color[0]]:
                    possible_game = False
        if possible_game:
            total += id
    return total

def sum_power_of_games(games: list) -> int:
    # the power of a game is the minimum number of cubes, all multiplied together
    total = 0
    for game in games:
        minimum = {"red":0, "green":0, "blue":0}
        formatted_game = split_game(game)
        for subset in formatted_game:
            for color in subset:
                if color[1] > minimum[color[0]]:
                    minimum[color[0]] = color[1]
        power = 1
        for i in minimum.values():
            power *= i
        total += power
    return total



if __name__ == "__main__":
    games = read_file_to_list("inputs/02/input.txt")
    print(count_possible_games(games))
    print(sum_power_of_games(games))
