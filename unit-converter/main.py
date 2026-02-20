import logging
from rich import print

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def convert_f_to_c(unit: float) -> float:
    """
    This function applies the formula to convert Fahrenheit units to Celsius.
    :param unit: Unit to be converted in Fahrenheit
    :return: Converted unit in Celsius
    """
    return (unit - 32) / 1.8


def convert_c_to_f(unit: float) -> float:
    """
    "This functions takes a unit in Celsius and converts it to Fahrenheit"
    :param unit:
    :return:
    """
    return (unit * 1.8) + 32


def convert_miles_to_km(unit: float) -> float:
    """
    TODO: Add docstrings
    :param unit:
    :return:
    """
    return unit * 1.60934


def convert_km_to_miles(unit: float) -> float:
    """
    TODO: Add docstrings
    :param unit:
    :return:
    """
    return unit / 1.60934


def convert_lbs_to_kg(unit: float) -> float:
    """
    TODO: Add docstrings
    :param unit:
    :return:
    """
    return unit * 0.453592


def convert_kg_to_lbs(unit: float) -> float:
    """
    TODO: Add docstrings
    :param unit:
    :return:
    """
    return unit / 0.453592


def temperature_menu() -> None:
    """
    TODO: Add docstrings
    :return:
    """
    print("1. C to F")
    print("2. F to C")
    print("3. Go Back")
    temp_option = input("Pick a conversion\n")
    try:
        if temp_option == "1" or temp_option == "2":
            num = input("Insert a number:\n")
            casted_num = float(num)
            if temp_option == "1":
                print(convert_c_to_f(casted_num))
            elif temp_option == "2":
                print(convert_f_to_c(casted_num))
    except ValueError:
        logger.error(f"{num} is not a number")


def distance_menu() -> None:
    """
    TODO: Add docstrings
    :return:
    """
    print("1. Miles to KM")
    print("2. KM to Miles ")
    print("3. Go Back")
    dist_option = input("Pick a conversion\n")
    try:
        if dist_option == "1" or dist_option == "2":
            num = input("Insert a number:\n")
            casted_num = float(num)
            if dist_option == "1":
                print(convert_miles_to_km(casted_num))
            elif dist_option == "2":
                print(convert_km_to_miles(casted_num))
    except ValueError:
        logger.error(f"{num} is not a number")


def weight_menu() -> None:
    print("1. LBS TO KG")
    print("2. KG TO LBS")
    print("3. Go Back")
    weight_option = input("Pick a conversion:\n")
    try:
        if weight_option == "1" or weight_option == "2":
            num = input("Insert a number:\n")
            casted_num = float(num)
            if weight_option == "1":
                print(convert_lbs_to_kg(casted_num))
            elif weight_option == "2":
                print(convert_kg_to_lbs(casted_num))
    except ValueError:
        logger.error(f"{num} is not a number")


def main():
    while True:
        print("Welcome to the Unit Converter")
        print("1. Temperature")
        print("2. Distance")
        print("3. Weight")
        print("Press 'Q' to quit")

        option = input("Select an option\n")

        if option == "1":
            temperature_menu()

        elif option == "2":
            distance_menu()

        elif option == "3":
            weight_menu()

        elif option == "q" or option == "Q":
            break

        else:
            print("Option not found")


if __name__ == "__main__":
    main()
