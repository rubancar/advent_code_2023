from exercises.base_exercise import BaseExercise
import logging
from copy import copy

logger = logging.getLogger(__name__)

class Day4(BaseExercise):

    def __init__(self):
        super().__init__()
        self.cards = None

    def calibration(self):
        self.cards = []
        for line_text in self.text_lines:
            card_name, lists = line_text.split(':')
            winning_numbers, your_numbers = lists.split('|')
            # if the argument is omitted, the string is split by whitespace
            winning_numbers = winning_numbers.strip().split()
            your_numbers = your_numbers.strip().split()
            winning_numbers = [ int(n) for n in winning_numbers]
            your_numbers = [ int(n) for n in your_numbers]
            self.cards.append((winning_numbers, your_numbers))
        # logger.info(self.cards)

    def execute_exercise(self):
        points = 0
        for winning_numbers, your_numbers in self.cards:
            p, _ = self.calculate_points(winning_numbers, your_numbers)
            points += p

        logger.info("Total: {}".format(points))

    def calculate_points(self, winning_numbers, your_numbers):
        numbers_in_card = 0
        your_numbers_ = copy(your_numbers)
        for winning_i in winning_numbers:
            try:
                your_numbers_.index(winning_i)
                # as it throws an error, it doesn't reach this code if the element is not present in the list
                your_numbers_.remove(winning_i)
                numbers_in_card += 1
            except ValueError:
                pass
        if numbers_in_card:
            return 2 ** (numbers_in_card - 1), numbers_in_card
        return 0, 0


class Day4Two(Day4):

    def execute_exercise(self):
        new_cards = [1]*len(self.cards)
        n_cards = self.calculate_cards_starting_row2(self.cards, new_cards)
        logger.info(f"Cards: {n_cards}")


    def calculate_cards_starting_row(self, cards: list, row_count: list):
        """
        Calculate numbers of cards using recursion, the stop condition is that when no cards are passed to the function,
        return 0
        :param cards: list of cards and winning cards
        :param row_count: an array keeping the number of each cards in each position
        :return: numbers of cards for the whole matrix + call to the same function with the submatrix starting from row + 1
        """
        if not len(cards):
            return 0
        counted_cards = 0
        k = 0

        for winning_numbers, your_numbers in cards:

            for n in range(row_count[k]):
                _, winning_cards = self.calculate_points(winning_numbers, your_numbers)
                for j in range(winning_cards):
                    row_count[k+1+j] += 1
                counted_cards += 1
                row_count[k] -= 1
            k += 1
        # we call to the same function but this time starting from the second row (first row has been processed)
        return counted_cards + self.calculate_cards_starting_row(cards[1:len(cards)], row_count[1:len(cards)])


    def calculate_cards_starting_row2(self, cards: list, row_count: list):
        """
        Using the old time for calculating the cards
        :param cards: list of cards and winning cards
        :param row_count: an array keeping the number of each cards in each position
        :return: total numbers of cards
        """
        if not len(cards):
            return 0

        i = 0
        new_cards = 0
        for winning_numbers, your_numbers in cards:
            for k in range(row_count[i]):
                _, winning_cards = self.calculate_points(winning_numbers, your_numbers)
                for j in range(winning_cards):
                    row_count[i+1+j] += 1
                    new_cards += 1
            i += 1
        logger.info(row_count)
        logger.info("New cards: " + str(new_cards))
        return new_cards + len(cards)
