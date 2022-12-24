from os import name as os_name, system as os_system
from secrets import choice

CHAR_POOL = "0123456789abcdef"

def check_repeating_sequence(value_a: str, value_b: str, sequence_length: int) -> tuple[bool, str]:
    """Checks whether the string values contain any repeating sequences of the specified length.

    Args:
        value_a (str): First string to compare
        value_b (str): Second string to compare
        sequence_length (int): Pattern length to check for

    Returns:
        tuple[bool, str]: True if repeating sequence found; False otherwise. If True, the matching pattern found is returned.
    """
    if len(value_a) < sequence_length or len(value_b) < sequence_length:
        raise ValueError(f"Both input values must be at least {sequence_length} characters in length!")

    for i in range(0,len(value_a),sequence_length):
        a_sequence = value_a[i:i+sequence_length]
        if len(a_sequence) == sequence_length:
            if a_sequence in value_b:
                return True, a_sequence
    
    return False, None

def clear_screen():
    # check and make call for specific operating system
    _ = os_system('cls' if os_name in ('nt', 'dos') else 'clear')

def collect_input(start: int, end: int) -> str:
    """Collect input by row from the user and return as a concatenated string.  If a row is left blank, stop collecting
    input and return.

    Args:
        start (int): First row number
        end (int): Last row number

    Returns:
        str: Concatenated values entered by the user
    """
    return_value = ""
    for i in range(start, end+1):
        input_value = input(f"ROW {i}: ")
        if input_value:
            return_value += input_value
        else:
            break
    return return_value

def decrypt(ct_hex: str, psk_hex: str) -> str:
    """Use the encrypt() function to perform bitwise XOR on the input hex strings, which if performed using the
    pre-shared key used to create the ciphertext, will return the original secret in plaintext.

    Args:
        ct_hex (str): Ciphertext as string of hexadecimal characters
        psk_hex (str): Randomly generated pre-shared key used in the one-time pad operation

    Returns:
        str: Decrypted plaintext secret
    """
    # Use the encrypted message (ciphertext) and pre-shared key to recover the original secret.
    decrypted_hex = encrypt(ct_hex, psk_hex)

    # Convert from hex string back to UTF-8 string
    decrypted_string = bytes.fromhex(decrypted_hex).decode('utf-8')

    return decrypted_string

def encrypt(secret_hex: str, psk_hex: str) -> str:
    """Bitwise XOR the input strings and return the ciphertext as a hex string.

    Args:
        secret_hex (str): Plaintext secret to encrypt
        psk_hex (str): Randomly generated pre-shared key used in the one-time pad operation

    Returns:
        str: Ciphertext as string of hexadecimal characters
    """
    # Bitwise XOR the secret and the key.
    ciphertext_int = int(secret_hex, 16) ^ int(psk_hex, 16)

    # Convert the resulting integer result to hex.
    ciphertext_hex = format(ciphertext_int, 'x')

    return ciphertext_hex

def generate_otp(length: int) -> str:
    """Generate a random string of the specified length using hexadecimal characters 0-9a-f.  This random secret key is
    referred to as a one-time pad when used in the encryption technique of the same name.
    
    NOTE: The random module built into Python does not generate truly random numbers. They are computed using an
    algorithm that creates numbers that only appear random, which is good enough in most cases. However, for the
    one-time pad to work, the pad must be generated from a truly random source; otherwise, it loses its mathematically
    perfect secrecy.  Python 3.6 and later have the secrets module, which uses the operating system's source of truly
    random numbers (often gathered from random events, such as the time between the user's keystrokes).

    Args:
        length (int): Length of the random string to generate

    Returns:
        str: Randomly generated string of hexadecimal characters
    """
    if not(0 < length <= 96):
        # Verify the string being split/encrypted is no more than 96 characters, since that is the backup plate max.
        raise ValueError("OTP value must be between 1 and 96 characters in length!")

    return "".join(choice(CHAR_POOL) for _ in range(length))

def one_time_pad(plaintext: str) -> tuple[str, str]:
    """Takes a plaintext input and performs a one-time pad operation by:
    [1] Generating a random secret key, called the one-time pad, that matches the length of the plaintext input.
    [2] Each bit or character of the plaintext is encrypted by combining it with the corresponding bit or character
        from the one-time pad using modular addition.
    [3] Returns the one-time pad key and the ciphertext resulting from the one-time pad operation as hex strings.

    Args:
        plaintext (str): Plaintext input to split

    Returns:
        tuple[str, str]: Pre-shared key and ciphertext result of OTP operation
    """
    if type(plaintext) is not str:
        raise ValueError("Input value must be of type string!")
    
    # Convert the plaintext to hex.
    plaintext_hex = str_to_hex(plaintext)

    # Determine the length of the hex string in characters.
    key_length = len(plaintext_hex)

    pattern_free = False
    while not pattern_free:
        # Generate a random value of equivalent length to the secret in hex, which will be the pre-shared key.
        pre_shared_key_hex = generate_otp(key_length)

        # Encrypt the input secret using the generated key.
        ciphertext_hex = encrypt(plaintext_hex, pre_shared_key_hex)

        match_found, _ = check_repeating_sequence(plaintext_hex, ciphertext_hex, 2)
        pattern_free = False if match_found else True

    return pre_shared_key_hex, ciphertext_hex

def str_to_hex(string: str) -> str:
    """Convert from string in ASCII format to a hexademical representation.

    Args:
        string (str): Input string of typically ASCII characters

    Returns:
        str: String of hexadecimal characters
    """
    # Convert from the ASCII input string to a bytes object encoded with UTF-8 and then
    # convert from a bytes object to a string of hexadecimal characters.
    return string.encode("utf-8").hex()