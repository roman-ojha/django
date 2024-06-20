# https://docs.python.org/3/library/logging.html

# Django Logging: https://docs.djangoproject.com/en/5.0/topics/logging/#logging-explanation
import logging
import sys

# create a logger object
logger = logging.getLogger('myLogger')  # getLogger(<name_of_logger>)

# Add formatter
# These use LogRecord attributes:
# https://docs.python.org/3/library/logging.html#logrecord-objects
formatter = logging.Formatter(
    fmt="%(name)s:%(asctime)s %(levelname)s: - %(message)s")

# Define the Handler objects
console_handler = logging.StreamHandler(
    stream=sys.stdout)  # stdout = standard out system
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler(
    filename='logs.txt')  # storing logging into files
file_handler.setFormatter(formatter)

# add Handler to the root logger
# Logger can has multiple handler and it will send log output to all the handlers
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# a function we will call


def division(numerator, denominator):
    try:
        return numerator/denominator
    except ZeroDivisionError:
        logger.critical(
            f"Division by zero error with parameters: {numerator}/{denominator}")
        logger.error(
            f"Division by zero error with parameters: {numerator}/{denominator}", exc_info=True)  # 'exc_info' will stack trace as well
        logger.exception(
            f"Division by zero error with parameters: {numerator}/{denominator}")  # No need of 'exc_info' for exception logger
        logger.warning(
            f"Division by zero error with parameters: {numerator}/{denominator}")

# NOTE: you should not output logs containing email address or password or any other secure information


if __name__ == "__main__":
    division(4, 0)
