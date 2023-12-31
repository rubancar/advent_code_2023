from exercises import Day1, Day1Two, Day2, Day2Two, Day3, Day3Two, Day4, Day4Two
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    problem = Day4Two()
    problem.load_data()
    problem.calibration()
    problem.execute_exercise()
