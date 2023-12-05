import functools
import math

from exercises.base_exercise import BaseExercise
import logging

logger = logging.getLogger(__name__)

class Day2(BaseExercise):
    game_config = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    def __init__(self):
        super().__init__()
        self.parsed_data = {}

    def calibration(self):
        for line in self.text_lines:
            # [Game 1]:[ 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green]
            game, configs = line.split(":")
            # [Game] [1]
            game_, game_id = game.split(" ")
            self.parsed_data[int(game_id)] = []
            # [ 3 blue, 4 red];[ 1 red, 2 green, 6 blue];[ 2 green]
            list_configs = configs.split("; ")
            for config_i in list_configs:
                # [ 3 blue],[ 4 red]
                result_game_i = {}
                list_color_config_i = config_i.split(", ")
                for color_i in list_color_config_i:
                    # [ 3] [blue]
                    num_color, color_name = color_i.strip().split(" ")
                    result_game_i[color_name.strip()] = int(num_color.strip())
                self.parsed_data[int(game_id)].append(result_game_i)


    def execute_exercise(self):
        valid_games = []
        for game_key, game_results in self.parsed_data.items():
            logger.info(game_results)
            valid_games.append(game_key)
            skip_game = False
            for game_i in game_results:
                for color_i, value_i in game_i.items():
                    if value_i > self.game_config[color_i]:
                        # to avoid pop an empty list
                        if valid_games:
                            valid_games.pop()
                        skip_game = True
                        logger.info(f"Game {game_key} BAD")
                        break
                if skip_game:
                    break
        logger.info(f"Valida games: {valid_games}")
        logger.info(f"Total: {sum(valid_games)}")




class Day2Two(Day2):

    def execute_exercise(self):
        game_powers = []
        for game_key, game_results in self.parsed_data.items():
            logger.info(game_results)
            minimun_by_color = {"red":1, "green":1, "blue":1}
            for game_i in game_results:
                for color_i, value_i in game_i.items():
                    if value_i > minimun_by_color[color_i]:
                        minimun_by_color[color_i] = value_i
            game_powers.append(functools.reduce(lambda a, b: a*b, minimun_by_color.values()))
        logger.info(f"Total: {sum(game_powers)}")
