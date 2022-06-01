import csv
import datetime as dt
import pytz


class Level:
    """
    Level is a class that is relevant to level points that are measured in Civil Engineering.
    """

    def __init__(self):
        """
        Takes Instrument Height and Acceptable Variation from user when initializing the class object.
        Time is the time when the object is created
        """
        self.instrument_height = float(input("Please Enter the Instrument Height of the measurement: "))
        self.acceptable_variation = float(input("Enter the acceptable variation: "))
        self.measure_level = []

        # Hard coded timezone
        self.time_zone_tp = pytz.timezone('Asia/Taipei')
        self.time = dt.datetime.now(self.time_zone_tp).strftime("%Y/%m/%d_%H:%M")

    def __str__(self):
        return f"Instrument Height: {self.instrument_height}\n" \
               f"Acceptable Variation: {self.acceptable_variation}\n" \
               f"Level Points: {self.measure_level}\n"

    @classmethod
    def is_float(cls, str_text) -> bool:
        """
        Class method that helps determine whether the input is valid.
        :param str_text: str
        :return: bool
        """
        try:
            float(str_text)
            return True

        except ValueError:
            return False

    def take_level_points(self) -> None:
        """
        Takes measurement inputs from the user.
        :return: None
        """
        take_input = True

        while take_input:
            level_point = input("Input Measured level, type (n) to quit: \n")
            if level_point.lower() == "n":
                # break when user inputs 'N' or 'n'
                take_input = False

            elif Level.is_float(level_point) and abs(
                    self.instrument_height - float(level_point)) <= self.acceptable_variation:
                # if valid, append to the measurement_level list
                self.measure_level.append(float(level_point))

            elif Level.is_float(level_point) and abs(
                    self.instrument_height - float(level_point)) > self.acceptable_variation:
                # invalid level inputs that disobeyed the variation
                self.measure_level.append(f"Level Invalid: {level_point}")
            else:
                # anything else that user inputs is invalid
                self.measure_level.append(f"Input Invalid: {level_point}")

    @property
    def results(self):
        """
        Returns a list of calculated results from the input data
        :return:
        """

        return list(map(lambda x: round(self.instrument_height - x, 2) if Level.is_float(x) else x, self.measure_level))

    @property
    def highest_point_level(self) -> float:
        """
        Returns the highest point level from the measurement result.
        :return: float
        """
        if all(isinstance(x, str) for x in self.results):
            # If there is no valid input, return 0
            return 0
        else:
            return max(list(filter(lambda x: Level.is_float(x), self.results)))

    @property
    def lowest_point_level(self) -> float:
        """
        Returns the lowest point level from the measurement result.
        :return: float
        """
        if all(isinstance(x, str) for x in self.results):
            # If there is no valid input, return 0
            return 0
        else:
            return min(list(filter(lambda x: Level.is_float(x), self.results)))

    @property
    def invalid_points(self) -> int:
        """
        Count total invalid points(including error inputs and inputs that disobeyed the variation)
        from the measurement result.
        :return: int
        """
        count = 0
        for result in self.results:
            if not Level.is_float(result):
                count += 1
        return count

    @property
    def invalid_level_points(self) -> int:
        """
        Count total invalid points(including error inputs and inputs that disobeyed the variation)
        from the measurement result.
        :return: int
        """
        count = 0
        for result in self.results:
            if not Level.is_float(result) and str(result)[0: 13] == "Level Invalid":
                count += 1
        return count

    @property
    def invalid_inputs(self) -> int:
        """
        Count total invalid error inputs from the measurement result.
        :return: int
        """
        count = 0
        for result in self.results:
            if not Level.is_float(result) and str(result)[0: 13] == "Input Invalid":
                count += 1
        return count

    def output_to_csv(self):
        """
        Create a csv file with a custom input name.
        :return: None
        """
        case_name = input("Enter the case name: ")
        with open(f"{case_name}_measurement.csv", mode='w', newline='') as csvfile:
            default_field = ["Instrument Height", "Acceptable Variation"]
            default_values = [self.instrument_height, self.acceptable_variation]
            empty_row = []
            field_names = ["User Inputs", "Calculated Result"]

            result_writer = csv.writer(csvfile, delimiter=',')
            result_writer.writerows([default_field, default_values, empty_row, field_names])

            for user_input, calculated_result in zip(self.measure_level, self.results):
                result_writer.writerow([user_input, calculated_result])

    def output_to_pdf(self):
        pass
