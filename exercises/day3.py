from exercises.base_exercise import BaseExercise
import logging

logger = logging.getLogger(__name__)

class Day3(BaseExercise):
    def __init__(self):
        super().__init__()
        self.data_matrix = None

    def calibration(self):
        self.data_matrix = []
        for line in self.text_lines:
            row = [int(ch) if ch.isnumeric() else False if ch == '.' else True for ch in line]
            self.data_matrix.append(row)

    def execute_exercise(self):
        good_numbers = []
        row_count = 0
        for row in self.data_matrix:
            logger.info(row)
            building_number = ""
            start_pos = 0
            count = 0
            for i in row:
                if type(i) == int:
                    if not building_number:
                        start_pos = count
                    building_number += str(i)
                    count += 1
                    if count != len(row):
                        continue
                count += 1
                if building_number:
                    logger.info(f"number: {building_number}, start_pos: {start_pos} end_pos: {count - 1}")
                    valid_inline = self.check_inline(row, start_pos, count-1)
                    valid_after_or_before = self.check_before_after_line(start_pos, count - 1, row_count)
                    logger.info(f"check inline: {valid_inline}")
                    logger.info(f"check after or before: {valid_after_or_before}")
                    if valid_inline or valid_after_or_before:
                        good_numbers.append(int(building_number))
                building_number = ""
            row_count += 1
        logger.info(f"Total: {sum(good_numbers)}")

    def check_inline(self, line, start, end):
        # after = False
        # before = False
        new_start = start - 1 if start != 0 else 0
        new_end = end + 1 if end != len(line) - 1 else end
        sub_array = line[new_start:new_end]
        sub_array_boolean = [True if x == True and type(x) == bool else False for x in  sub_array]

        # if start != 0:
        #     before = line[start]
        # if end != len(line) - 1:
        #     after = line[end]
        return any(sub_array_boolean)

    def check_before_after_line(self, start, end, row_number):
        check_before = False
        check_after = False
        if row_number != 0:
            before_row = self.data_matrix[row_number-1]
            check_before = self.check_inline(before_row, start, end)

        if row_number != len(self.data_matrix) - 1:
            after_row = self.data_matrix[row_number+1]
            check_after = self.check_inline(after_row, start, end)

        return check_after or check_before




class Day3Two(BaseExercise):

    def calibration(self):
        self.data_matrix = []
        for line in self.text_lines:
            row = [int(ch) if ch.isnumeric() else True if ch == '*' else False for ch in line]
            self.data_matrix.append(row)

    def execute_exercise(self):
        good_numbers = []
        row_count = 0
        for row in self.data_matrix:
            logger.info(f"Row: {row}")
            new_good_numbers = self.check_before_after_line(row_count)
            good_numbers.extend(new_good_numbers)
            row_count += 1
        logger.info(f"Total: {sum(good_numbers)}")


    def check_before_after_line(self, row_number):
        good_numbers = []
        if row_number == 0 or row_number == len(self.data_matrix) - 1:
            return good_numbers

        # TODO: this was a complete waste of time for a bad understanding of the problem
        # before_row = self.data_matrix[row_number - 1]
        # after_row = self.data_matrix[row_number + 1]
        # simplified_row = []
        # for i in range(0, len(before_row)):
        #     if type(before_row[i]) == int and type(after_row[i]) == int:
        #         simplified_row.append(3)
        #     elif type(before_row[i]) == int:
        #         simplified_row.append(1)
        #     elif type(after_row[i]) == int:
        #         simplified_row.append(2)
        #     else:
        #         simplified_row.append(0)

        # logger.info(f"Simplified row {simplified_row}")
        current_pos = 0
        reviewed_at_above = 0
        reviewed_at_below = 0
        for col in self.data_matrix[row_number]:
            # if * is found check
            if col and type(col) == bool:
                # start_sub = current_pos - 1 if current_pos > 0 else 0
                # end_sub = current_pos + 2 if current_pos  != len(self.data_matrix[row_number]) - 1 else current_pos + 1
                # sub_matrix = simplified_row[start_sub:end_sub]
                # match_above_below = self.at_least_one_difference(sub_matrix)
                # if match_above_below:
                new_numbers, max_col_reviewed = self.get_numbers_up_to_col(self.data_matrix[row_number-1], current_pos, reviewed_at_above)
                reviewed_at_above = max_col_reviewed

                new_numbers_below, max_col_reviewed_below = self.get_numbers_up_to_col(self.data_matrix[row_number+1], current_pos, reviewed_at_below)
                reviewed_at_below = max_col_reviewed_below

                new_numbers_inline, _ = self.get_numbers_up_to_col(self.data_matrix[row_number], current_pos, None)

                if len(new_numbers) + len(new_numbers_below) + len(new_numbers_inline) == 2:
                    base_total = 1
                    for_logging = []
                    # worst code ever, tired of wasting time
                    if len(new_numbers) == 1:
                        base_total *= new_numbers[0]
                        for_logging.append(new_numbers[0])
                    if len(new_numbers_below) == 1:
                        base_total *= new_numbers_below[0]
                        for_logging.append(new_numbers_below[0])
                    if len(new_numbers_inline) == 1:
                        base_total *= new_numbers_inline[0]
                        for_logging.append(new_numbers_inline[0])

                    if len(new_numbers) == 2:
                        base_total = new_numbers[0] * new_numbers[1]
                        for_logging.extend([new_numbers[0], new_numbers[1]])
                    if len(new_numbers_below) == 2:
                        base_total = new_numbers_below[0] * new_numbers_below[1]
                        for_logging.extend([new_numbers_below[0], new_numbers_below[1]])
                    if len(new_numbers_inline) == 2:
                        base_total = new_numbers_inline[0] * new_numbers_inline[1]
                        for_logging.extend([new_numbers_inline[0], new_numbers_inline[1]])

                    good_numbers.append(base_total)
                    logger.info(f"Multiplication: {for_logging}, base_total: {base_total}")

            current_pos += 1
        return good_numbers

    def get_numbers_up_to_col(self, row, up_to_col, reviewed_at):
        building_number = ""
        start_pos = 0
        good_numbers = []
        for col_i in range(0, len(row)):
            if type(row[col_i]) == int:
                if not building_number:
                    start_pos = col_i
                building_number += str(row[col_i])
                # count += 1
                if col_i != len(row) - 1:
                    continue

            if not building_number and col_i > up_to_col + 1:
                return good_numbers, col_i

            if building_number:
                if start_pos <= up_to_col + 1 and col_i - 1 >= up_to_col - 1:
                # if (up_to_col - 1 <= col_i - 1 <= up_to_col + 1) or (up_to_col - 1 <= start_pos <= up_to_col + 1):
                    good_numbers.append(int(building_number))

            building_number = ""

            if col_i == up_to_col + 1:
                return good_numbers, col_i
        return good_numbers, len(row) - 1


    def at_least_one_difference(self, array):
        initial = None
        other = None
        for i in array:
            if i == 3:
                return True
            elif i != 0 and initial is None:
                initial = i
            elif i != 0:
                other = i

        if initial is not None and other is not None:
            return initial != other

        return False




