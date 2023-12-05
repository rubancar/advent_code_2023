from exercises.base_exercise import BaseExercise
import logging

logger = logging.getLogger(__name__)
class Day1(BaseExercise):

    def execute_exercise(self):
        logger.info("Running exercise from day1")
        total = 0
        for line in self.text_lines:
            logger.info(line)
            number_line = self.get_first_digit(line) + self.get_last_digit(line)
            logger.info(f"sum_line: {number_line}")
            total = total + int(number_line)
        logger.info(f"Total: {total}")
        return total

    def get_first_digit(self, line_txt):
        default = ''
        for ch in line_txt:
            value_ascii = int(ord(ch))
            if value_ascii >= 48 and value_ascii <= 57:
                return ch
        return default

    def get_last_digit(self, line_txt):
        default = ''
        for p in range(len(line_txt)-1, -1, -1):
            value_ascii = int(ord(line_txt[p]))
            if value_ascii >= 48 and value_ascii <= 57:
                default = line_txt[p]
                return default
        return default


class Day1Two(BaseExercise):
    three_letters = ["one", "two", "six"]
    four_letters = ["four", "five", "nine"]
    five_letters = ["three", "seven", "eight"]
    dict_letters = {
        3: three_letters,
        4: four_letters,
        5: five_letters
    }
    dict_translate = {
        "one": "1",
        "two": "2",
        "six": "6",
        "four": "4",
        "five": "5",
        "nine": "9",
        "three": "3",
        "seven": "7",
        "eight": "8"
    }

    def execute_exercise(self):
        logger.info("Running exercise from day1two")
        total = 0
        for line in self.text_lines:
            logger.info(line)
            number_line = self.get_first_digit(line) + self.get_last_digit(line)
            logger.info(f"sum_line: {number_line}")
            total = total + int(number_line)
        logger.info(f"Total: {total}")
        return total

    def get_first_digit(self, line_text):
        default = ''
        initial_pos = 0
        for ch in line_text:
            value_ascii = int(ord(ch))
            if self.is_digit(value_ascii):
                default = ch
            else:
                default = self.loop_forward_for_number(line_text, initial_pos)
            if default != '':
                return default
            initial_pos += 1
        return default


    def get_last_digit(self, line_text):
        default = ''
        end_pos = len(line_text) - 1
        for p in range(len(line_text) - 1, -1, -1):
            value_ascii = int(ord(line_text[p]))
            if self.is_digit(value_ascii):
                default = line_text[p]
            else:
                default = self.loop_backward_for_number(line_text, end_pos)
            if default != '':
                return default
            end_pos -= 1
        return default

    def loop_forward_for_number(self, line_text, initial_pos):
        for size_str in [3,4,5]:
            for end_i in range(initial_pos, len(line_text)):
                sub_str = line_text[initial_pos:end_i]
                # Todo: retornar cuando el string supera el tamaño máximo de texto a buscar
                if len(sub_str) in self.dict_letters and sub_str in self.dict_letters[len(sub_str)]:
                    logger.info(f"found: {sub_str}")
                    return self.dict_translate[sub_str]
        return ""

    def loop_backward_for_number(self, line_text, end_pos):
        for size_str in [3,4,5]:
            for start_i in range(end_pos, -1, -1):
                sub_str = line_text[start_i:end_pos+1]
                # Todo: retornar cuando el string supera el tamaño máximo de texto a buscar
                if len(sub_str) in self.dict_letters and sub_str in self.dict_letters[len(sub_str)]:
                    logger.info(f"found: {sub_str}")
                    return self.dict_translate[sub_str]
        return ""
    def is_digit(self, ch):
        return 48 <= ch <= 57

