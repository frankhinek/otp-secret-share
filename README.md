# One-Time Pad Secret Sharing

This utility is an implementation of One-Time Padding (OTP) intended to be used for secret splitting.

Simplistically, you randomly generate a new key with exactly the same length as the secret you wish to split.  This
random key is XOR'd with the secret producing a ciphertext string.  To recover the original secret, the randomly
generated key and ciphertext are XOR'd.  In this way, you can "split" a secret into two generated keys and give the keys
to two people or store in two locations.

Anyone in possession of the two keys can use them to recover the original secret.

## Usage Tutorial

This tutorial will walk you through an example of splitting and recovering two strings (a "password"
and a "secret").  It is recommended that you follow the steps in this tutorial at least once before
using this utility to ensure that you understand how the two input values are split and in which
order you should enter characters engraved or stamped on to the backup plates when attempting
recovery.  It is rather easy to get confused and if the values aren't engraved/stamped on to the
plates and/or entered in the wrong order during recovery, your data may be unrecoverable.

### Available Commands

There are only two operations accessible from the command-line interface (CLI):

* `split` - Split a secret into two keys or "shares"
* `recover` - Recover the original secret by entering the two "shares"

The utility was designed to take as input a **password** and a **secret** to be split into two shares
each and stored on a pair of Bitcoin seed phrase metal plates.

### Split Plaintext into Shares

To split a secret into two shares, append the `split` command when running the `secret.py` script.

```shell
$ python secret.py split
```

You will be prompted to enter the **password** first followed by the **secret**.

```shell
Enter password to split: examplepassword
Enter secret to split: examplesecret
```

After the two input values are entered, the utility will generate the two shares (1 randomly generated key and the ciphertext resulting for the XOR operation between the generated key and secret value entered by the user) for each input and graphically display the values generated
in the manner they should be engraved or stamped on to the metal backup plates:

```shell
  ╔══════════════════════════════════════════════════════════╗
  ║                    BACKUP PLATE SET 1                    ║
  ╚══════════════════════════════════════════════════════════╝
  ┏━━━━━━━━━━━━━━━━━━━━━━━━┓        ┏━━━━━━━━━━━━━━━━━━━━━━━━┓
  ┃                        ┃        ┃                        ┃
  ┃  1   6 2 c 6 f 5 b a   ┃        ┃ 13   f f 8 e 8 5 c 3   ┃
  ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃        ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃
  ┃  2   6 0 6 7 3 a a d   ┃        ┃ 14   4 4 a 4 7 5 9 0   ┃
  ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃        ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃
  ┃  3   e 9 b 6 2 6 2 4   ┃        ┃ 15   0 2 b 0 4 3 b 2   ┃
  ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃        ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃
  ┃  4   4 4 3 7 8 3       ┃        ┃ 16   6 4               ┃
  ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃        ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃
  ┃  5                     ┃        ┃ 17                     ┃
  ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃        ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃
  ┃  6                     ┃        ┃ 18                     ┃
  ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃        ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃
  ┃  7                     ┃        ┃ 19                     ┃
  ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃        ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃
  ┃  8                     ┃        ┃ 20                     ┃
  ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃        ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃
  ┃  9                     ┃        ┃ 21                     ┃
  ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃        ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃
  ┃ 10                     ┃        ┃ 22                     ┃
  ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃        ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃
  ┃ 11                     ┃        ┃ 23                     ┃
  ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃        ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃
  ┃ 12                     ┃        ┃ 24                     ┃
  ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃        ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃
  ┗━━━━━━━━━━━━━━━━━━━━━━━━┛        ┗━━━━━━━━━━━━━━━━━━━━━━━━┛

  ╔══════════════════════════════════════════════════════════╗
  ║                    BACKUP PLATE SET 2                    ║
  ╚══════════════════════════════════════════════════════════╝
  ┏━━━━━━━━━━━━━━━━━━━━━━━━┓        ┏━━━━━━━━━━━━━━━━━━━━━━━━┓
  ┃                        ┃        ┃                        ┃
  ┃  1   7 b e 9 4 d 7 1   ┃        ┃ 13   9 a f 6 e 4 a e   ┃
  ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃        ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃
  ┃  2   0 0 b 5 f d d 8   ┃        ┃ 14   3 4 c 8 1 0 e 3   ┃
  ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃        ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃
  ┃  3   8 c 5 5 5 5 3 2   ┃        ┃ 15   6 7 d 3 3 1 d 7   ┃
  ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃        ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃
  ┃  4   b 4 5 e 7         ┃        ┃ 16   1 0               ┃
  ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃        ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃
  ┃  5                     ┃        ┃ 17                     ┃
  ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃        ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃
  ┃  6                     ┃        ┃ 18                     ┃
  ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃        ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃
  ┃  7                     ┃        ┃ 19                     ┃
  ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃        ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃
  ┃  8                     ┃        ┃ 20                     ┃
  ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃        ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃
  ┃  9                     ┃        ┃ 21                     ┃
  ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃        ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃
  ┃ 10                     ┃        ┃ 22                     ┃
  ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃        ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃
  ┃ 11                     ┃        ┃ 23                     ┃
  ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃        ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃
  ┃ 12                     ┃        ┃ 24                     ┃
  ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃        ┃     └─┴─┴─┴─┴─┴─┴─┴─┘  ┃
  ┗━━━━━━━━━━━━━━━━━━━━━━━━┛        ┗━━━━━━━━━━━━━━━━━━━━━━━━┛
```

### Recover Plaintext from Shares

To recover the **password** and **secret** values that were split into two shares each and engraved
or stamped on to metal seed phrase backup plates, append the `recover` command when running the `secret.py` script.

```shell
$ python secret.py recover
```

You will be prompted to enter the values from the first pair of plates (i.e., "BACKUP PLATE SET 1")
starting with rows 1 to 12 and then followed by rows 13-24.

_NOTE_: If the metal plate only contains values in some of the rows, press the ENTER key after
you've finished entering values and the utility will skip the remaining rows and request input
for the next plate in the set.

```shell
╔═════════════════════╗
║ BACKUP PLATE SET #1 ║
╚═════════════════════╝

Type the values from rows 1-12 of the
first metal plate in Backup Set #1.

ROW 1: 62c6f5ba
ROW 2: 60673aad
ROW 3: e9b62624
ROW 4: 443783
ROW 5:
```

After pressing the ENTER key during the `ROW 5:` prompt to indicate there are no further values
recorded on this plate, the utility will prompt you to enter the values for **BACKUP PLATE SET #1**
rows 13-24:

```shell
╔═════════════════════╗
║ BACKUP PLATE SET #1 ║
╚═════════════════════╝

 ___________________
/\                  \
\_| Switch to plate |
  | with rows 13-24 |
  |   ______________|_
   \_/________________/

Type the values from rows 13-24 of the
second metal plate in Backup Set #1.

ROW 13: ff8e85c3
ROW 14: 44a47590
ROW 15: 02b043b2
ROW 16: 64
ROW 17:
```

After pressing the ENTER key during the `ROW 17:` prompt to indicate there are no further values
recorded on this plate, the utility will prompt you to switch to **BACKUP PLATE SET #2** and enter
the values from rows 1-12:

```shell
╔═════════════════════╗
║ BACKUP PLATE SET #2 ║
╚═════════════════════╝

 ____________________
/\                   \
\_| Switch to Backup |
  | Plate Set #2     |
  |   _______________|_
   \_/_________________/

Type the values from rows 1-12 of the
first metal plate in Backup Set #2.

ROW 1: 7be94d71
ROW 2: 00b5fdd8
ROW 3: 8c555532
ROW 4: b45e7
ROW 5:
```

After pressing the ENTER key during the `ROW 5:` prompt to indicate there are no further values
recorded on this plate, the utility will prompt you to enter the values for the remaining
rows 13-24 of **BACKUP PLATE SET #2**:

```shell
╔═════════════════════╗
║ BACKUP PLATE SET #2 ║
╚═════════════════════╝

 ___________________
/\                  \
\_| Switch to plate |
  | with rows 13-24 |
  |   ______________|_
   \_/________________/

Type the values from rows 13-24 of the
second metal plate in Backup Set #2.

ROW 13: 9af6e4ae
ROW 14: 34c810e3
ROW 15: 67d331d7
ROW 16: 10
ROW 17:
```

After all of the rows have been entered from both sets of backup plates (4 plates total), the
utility will recover the original **password** and **secret** values that were split into shares:

```shell
                ______________________________________
       ________|                                      |_______
       \       |         PASSWORD AND SECRET          |      /
        \      |       SUCCESSFULLY RECOVERED!        |     /
        /      |______________________________________|     \
       /__________)                                (_________\

╔════════════╤═════════════════╗
║ PASSWORD   │ examplepassword ║
╠════════════╪═════════════════╣
║ SECRET KEY │ examplesecret   ║
╚════════════╧═════════════════╝
```

## REFERENCE

### One-Time Pad Reference

From [Wikipedia](https://en.wikipedia.org/wiki/One-time_pad):

> In cryptography, the one-time pad (OTP) is an encryption technique that cannot be cracked, but requires the use of a
single-use pre-shared key that is not smaller than the message being sent. In this technique, a plaintext is paired with
a random secret key (also referred to as a one-time pad). Then, each bit or character of the plaintext is encrypted by
combining it with the corresponding bit or character from the pad using modular addition.
>
> The resulting ciphertext will be impossible to decrypt or break if the following four conditions are met:
>
> 1. The key must be at least as long as the plaintext.
> 2. The key must be random (uniformly distributed in the set of all possible keys and independent of the plaintext),
> entirely sampled from a non-algorithmic, chaotic source such as a hardware random number generator.
> 2. The key must never be reused in whole or in part.
> 3. The key must be kept completely secret by the communicating parties.

### Building Executable with Pyinstaller

[Pyinstaller](https://pyinstaller.org) can be used to bundle this OTP secret sharing utility and all
its dependencies into a single package that a user can run without installing a Python interpreter
or any modules.

To build or rebuild a single bundled executable, run the following command in a terminal application
from the root directory of this repository.

```shell
pyinstaller --onefile --console -n secretshare secret.py
```

After Pyinstaller runs, the bundled executable is stored in the `dist/` directory and can be run from
a terminal with the following commands:

```shell
cd dist/
./secretshare [split] [recover]
```
