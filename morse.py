class Morse:
    morse_chart = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----",
        ", ": "--..--",
        ".": ".-.-.-",
        "?": "..--..",
        "!": "-.-.--",
        "/": "-..-.",
        "-": "-....-",
        "(": "-.--.",
        ")": "-.--.-",
    }
    characters = list(morse_chart.keys())
    codes = list(morse_chart.values())

    @classmethod
    def in_morse_chart(cls, char: str = None) -> tuple[str, str] | None:
        """ Checks if letter, number, symbol, or morse is in the chart. """

        try:
            mod_char = char.strip().upper()

            if cls.is_morse(char):
                return (
                    cls.characters[cls.codes.index(mod_char)],
                    cls.codes[cls.codes.index(mod_char)],
                )

            return (
                cls.characters[cls.characters.index(mod_char)],
                cls.morse_chart[mod_char],
            )

        except (ValueError, TypeError, AttributeError):
            return None

    @classmethod
    def is_morse(cls, morse: str = None) -> bool:
        """ Checks if morse is valid. """

        try:
            if not morse.strip():  # Checks if morse is empty
                return False

            for char in cls.clean_morse(morse).split(" "):
                for symbol in char:
                    if symbol not in [".", "-"]:
                        return False
            return True

        except AttributeError:
            return False

    @classmethod
    def clean_morse(cls, morse: str) -> str:
        """ Spaces in the start, between, or end will be removed. """

        raw = [char for char in morse.split(" ") if char.strip()]
        return "  ".join(raw)

    @classmethod
    def add_morse(cls, char: str = None, morse: str = None):
        """ Adds morse code to the chart. """

        try:
            if cls.is_morse(morse):
                if (char.upper(), morse) not in cls.morse_chart.items():
                    cls.morse_chart.update({char.upper(): cls.clean_morse(morse)})

                    # Updates the values of the list when a morse is added
                    cls.characters = list(cls.morse_chart.keys())
                    cls.codes = list(cls.morse_chart.values())

                else:
                    print("Morse code already in the chart.")
            else:
                # This will be printed if:
                # - Morse code consist of characters other than dots and dashes.
                # - No morse code is specified.
                print("Invalid or no morse code specified.")

        except TypeError as err:
            print(err)


class MorseEncrypt(Morse):
    @classmethod
    def encrypt_letter(cls, char: str = None) -> str | None:
        """ Encrypts a letter. """

        try:
            return " " if char == " " else cls.morse_chart.get(char.upper()) + " "

        except (TypeError, ValueError):
            return None

    @classmethod
    def encrypt(cls, message: str = None) -> str | None:
        """ Encrypts a message. """

        try:
            morse_message: str = ""

            for char in message.upper():
                morse_message += cls.encrypt_letter(char)

            return morse_message.strip()

        except (ValueError, TypeError, AttributeError):
            return None


class MorseDecrypt(Morse):
    @classmethod
    def decrypt_morse(cls, char: str = None) -> str | None:
        """ Decrypts a single morse code. """

        try:
            return (
                " "
                if char.strip() == ""
                else cls.characters[cls.codes.index(char.strip())]
            )

        except (ValueError, AttributeError):
            return None

    @classmethod
    def decrypt(cls, message: str = None) -> str | None:
        """ Decrypts a message. """

        decrypted_message = ""

        try:
            for morse in message.split(" "):
                decrypted_message += cls.decrypt_char(morse)

            return decrypted_message

        except (ValueError, AttributeError, TypeError):
            return None


def main():
    Morse.add_morse("GUI", "--.        ---.           ---            ")
    print(f"In morse code chart: {Morse.in_morse_chart('5')}")
    print(f"Cleaned morse: {Morse.clean_morse('--.        ---.           ---')}")
    print(f"Encrypt: {MorseEncrypt.encrypt('Hello World!')}")
    print(
        f"Decrypt: {MorseDecrypt.decrypt('.... . .-.. .-.. ---  .-- --- .-. .-.. -.. -.-.--')}"
    )
    print(f"Encrypt letter: {MorseEncrypt.encrypt_letter('x')}")
    print(f"Decrypt letter: {MorseDecrypt.decrypt_morse('-..-')}")


if __name__ == "__main__":
    main()
