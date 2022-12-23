
COMPONENT_TOP    = "┏━━━━━━━━━━━━━━━━━━━━━━━━┓"
COMPONENT_SPACER = "┃                        ┃"
COMPONENT_GRID   = "┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃"
COMPONENT_BOTTOM = "┗━━━━━━━━━━━━━━━━━━━━━━━━┛"

def build_plate(string: str, set: int, start: int) -> list:
    """Utility function to assemble the rows of a build plate display that can be printed to screen.

    Args:
        string (str): Text that will be stamped/engraved onto the plate
        set (int): Backup plate set number (typically, 1 or 2)
        start (int): Starting row number for the plate (typically, 1 or 13)

    Raises:
        ValueError: Raise a ValueError if the function is called with a text string that is longer than 96 characters
                    since this is the maximum number of characters that can be stamped/engraved losslessly onto a plate
                    with twelve rows of eight characters.

    Returns:
        list: A list of rows from the plate that can be printed to screen
    """
    if len(string) > 96:
        raise ValueError("Too many characters - Plate can store 96 characters maximum!")
    
    plate = []
    plate.append(COMPONENT_TOP)
    plate.append(COMPONENT_SPACER)
    for i in range(0, len(string), 8):
        row_num = int(i/8+start)
        plate.append(component_row(row_num, string[i:i+8]))
        plate.append(COMPONENT_GRID)
    if row_num % 12 < 12:
        new_rows = [[component_row(add_row, ""), COMPONENT_GRID] for add_row in range(row_num%12+start, 12+start)]
        flattened_new_rows = [item for sublist in new_rows for item in sublist]
        plate.extend(flattened_new_rows)
    plate.append(COMPONENT_BOTTOM)

    return plate


def plate_set_title(title: str) -> str:
    """Utility function to assemble a title box that can be printed to screen.

    Args:
        title (str): Title to display in the box

    Returns:
        str: String containing the rows of the title box
    """
    title_length = 56
    return (f"  ╔═" + "═"*title_length + "═╗\n"
            f"  ║ {title: ^{title_length}} ║\n"
            f"  ╚═" + "═"*title_length + "═╝")

def component_row(num: int, chars: list) -> str:
    """Utility function to assemble a row that displays the row number and up to eight characters,
    as they would appear on a backup plate.

    Args:
        num (int): _description_
        chars (list): _description_

    Returns:
        str: _description_
    """
    values = " ".join(char for char in chars)
    output = f"┃ {num: >2}   {values: <15}   ┃"
    return output

def print_plates_h(plate_set: dict) -> None:
    """Print two plates horizontally (side-by-side).

    Args:
        plate_set (dict): A dictionary with keys 1 and 2 with values that are the rows of the plates as lists.
    """
    for row_num, _ in enumerate(plate_set[1]):
        print(f"  {plate_set[1][row_num]}        {plate_set[2][row_num]}")
    print("")

def print_header(num: int) -> None:
    print(  "╔═════════════════════╗\n"
           f"║ BACKUP PLATE SET #{num} ║\n"
            "╚═════════════════════╝\n")

def print_note_blank_rows() -> None:
    print("        _\|/_\n"
          "        (o o)\n"
          "+----oOO-{_}-OOo----------------------+\n"
          "|                                     |\n"
          "|   If subsequent rows on the metal   |\n"
          "|      plate are blank, press the     |\n"
          "|        ENTER key to proceed.        |\n"
          "|                                     |\n"
          "+------------------------------------*/\n")

def print_note_switch_plate(num: int) -> None:
    """Utility function to print a message to the screen that informs the user they need to switch plates.
    Typically, the integer value passed will be either 1 for a plate with rows 1-12 or 13 for a plate with rows 13-24.

    Args:
        num (int): Value that determines which row numbers to display
    """
    value = f"{num}-{num+11}"
    print(" ___________________\n"
          "/\                  \\\n"
          "\_| Switch to plate |\n"
         f"  | with rows {value: <5} |\n"
          "  |   ______________|_\n"
          "   \_/________________/\n")

def print_note_switch_set(num: int) -> None:
    """Utility function to print a message to the screen that informs the user they need to switch backup plate sets.
    Typically, the integer value passed will be either 1 or 2.

    Args:
        num (int): _description_
    """
    print(" ____________________\n"
          "/\                   \\\n"
          "\_| Switch to Backup |\n"
         f"  | Plate Set #{num}     |\n"
          "  |   _______________|_\n"
          "   \_/_________________/\n")

def print_note_success() -> None:
    print("                ______________________________________\n"
          "       ________|                                      |_______\n"
          "       \       |         PASSWORD AND SECRET          |      /\n"
          "        \      |       SUCCESSFULLY RECOVERED!        |     /\n"
          "        /      |______________________________________|     \\\n"
          "       /__________)                                (_________\\\n")

def print_plates(password_shares, secret_shares):
    plate_set_1 = {
        1: build_plate(password_shares[0], 1, 1),
        2: build_plate(secret_shares[0], 1, 13)
    }

    plate_set_2 = {
        1: build_plate(password_shares[1], 2, 1),
        2: build_plate(secret_shares[1], 2, 13)
    }

    print(plate_set_title("BACKUP PLATE SET 1"))
    print_plates_h(plate_set_1)
    print(plate_set_title("BACKUP PLATE SET 2"))
    print_plates_h(plate_set_2)