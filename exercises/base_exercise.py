from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class BaseExercise:
    data_path = Path(__file__).parent.parent.joinpath('data')

    def __init__(self):
        self.text_lines = None
        self.name = self.__class__.__name__.lower()
        self.text_data = None

    def load_data(self):
        file_to_read = self.data_path.joinpath(f"{self.name}.txt")
        logger.info(f"Reading file {file_to_read}")
        try:
            with open(file_to_read, "r") as data_file:
                self.text_data = data_file.read()
                self.text_lines = self.text_data.splitlines()
        except FileNotFoundError:
            logger.error(f"File {self.name}.txt not found")
            exit(1)



    def calibration(self):
        print(f"running calibration on {len(self.text_data)}")

    def execute_exercise(self):
        print(f"executing calibration on {len(self.text_data)}")