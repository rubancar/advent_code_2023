from exercises import Day1, Day1Two
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    day1 = Day1Two()
    day1.load_data()
    day1.execute_exercise()
