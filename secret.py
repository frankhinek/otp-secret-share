"""
An implementation of One-Time Padding (OTP)

In cryptography, the one-time pad (OTP) is an encryption technique that cannot be cracked, but requires the use of a
single-use pre-shared key that is not smaller than the message being sent. In this technique, a plaintext is paired with
a random secret key (also referred to as a one-time pad). Then, each bit or character of the plaintext is encrypted by
combining it with the corresponding bit or character from the pad using modular addition.

The resulting ciphertext will be impossible to decrypt or break if the following four conditions are met:

[1] The key must be at least as long as the plaintext.
[2] The key must be random (uniformly distributed in the set of all possible keys and independent of the plaintext),
    entirely sampled from a non-algorithmic, chaotic source such as a hardware random number generator.
[3] The key must never be reused in whole or in part.
[4] The key must be kept completely secret by the communicating parties.

Reference: https://en.wikipedia.org/wiki/One-time_pad
"""

from sys import argv
from otp_secret_sharing.display import print_header, print_note_blank_rows, print_note_success, print_note_switch_plate, print_note_switch_set, print_plates
from otp_secret_sharing.utils import clear_screen, decrypt, one_time_pad, collect_input

def usage_instructions():
    return (
        "Usage: secretshare [OPTIONS] COMMAND\n\n"
        "  Utility for splitting secrets into two shares that can be given to\n"
        "  two people or stored in two locations.  Uses One-Time Padding (OTP).\n\n"
        "Options:\n"
        "  -h, --help     Display help for the utility.\n\n"
        "Commands:\n"
        "  split          Split a plaintext secret into two keys or shares.\n"
        "  recover        Recover the plaintext secret by entering the two shares."
    )

if __name__ == '__main__':
    # Determine the type of operation to perform: split or recover
    match argv:
        case command, argument:
            match argument:
                case "split":
                    clear_screen()
                    password_input = input("Enter password to split: ")
                    secret_input = input("Enter secret to split: ")
                    # Generate the shares using One-Time Padding XOR technique.
                    password_shares = one_time_pad(password_input)
                    secret_shares = one_time_pad(secret_input)
                    # Print the shares to the terminal.
                    clear_screen()
                    print_plates(password_shares, secret_shares)

                case "recover":
                    clear_screen()
                    print_header(1)
                    print_note_blank_rows()
                    print("Type the values from rows 1-12 of the\n"
                          "first metal plate in Backup Set #1.\n")
                    password_share_a = collect_input(1, 12).lower()
                    
                    clear_screen()
                    print_header(1)
                    print_note_switch_plate(13)
                    print("Type the values from rows 13-24 of the\n"
                          "second metal plate in Backup Set #1.\n")
                    secret_key_share_a = collect_input(13, 24).lower()

                    clear_screen()
                    print_header(2)
                    print_note_switch_set(2)
                    print("Type the values from rows 1-12 of the\n"
                          "first metal plate in Backup Set #2.\n")
                    password_share_b = collect_input(1, 12).lower()

                    clear_screen()
                    print_header(2)
                    print_note_switch_plate(13)
                    print("Type the values from rows 13-24 of the\n"
                          "second metal plate in Backup Set #2.\n")
                    secret_key_share_b = collect_input(13, 24).lower()
                    
                    # Recover the password.
                    password_plaintext = decrypt(password_share_a, password_share_b)

                    # Recover the secret key.
                    secret_plaintext = decrypt(secret_key_share_a, secret_key_share_b)

                    # Display the password and secret key to the user.
                    clear_screen()
                    print_note_success()
                    longest = len(password_plaintext) if len(password_plaintext) > len(secret_plaintext) else len(secret_plaintext)
                    print(
                          "╔════════════╤═" + "═"*longest + "═╗\n"
                         f"║ PASSWORD   │ {password_plaintext:<{longest}} ║\n"
                          "╠════════════╪═" + "═"*longest + "═╣\n"
                         f"║ SECRET KEY │ {secret_plaintext:<{longest}} ║\n"
                          "╚════════════╧═" + "═"*longest + "═╝\n")
                
                case _:
                    print(usage_instructions())
        
        case _:
            print(usage_instructions())
