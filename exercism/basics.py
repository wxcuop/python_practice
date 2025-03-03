"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

# Constants
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2  # Assuming it takes 2 minutes to prepare each layer

# Function to calculate remaining bake time
def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

# Function to calculate preparation time based on the number of layers
def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate preparation time.

    :param number_of_layers: int - number of layers in the lasagna.
    :return: int - preparation time (in minutes).
    """
    return number_of_layers * PREPARATION_TIME

# Function to calculate total elapsed time
def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate total elapsed time.

    :param number_of_layers: int - number of layers in the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total elapsed time (in minutes).
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
