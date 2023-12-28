class MorseCodeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


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
    def _clean_morse(cls, morse: str) -> str:
        """Spaces in the start, between, or end will be removed."""

        # Create a list of morse without leading and trailing spaces.
        clean_morse = [char for char in morse.split(" ") if char.strip()]

        # Join the morse with two spaces in between each element.
        return "  ".join(clean_morse)

    @classmethod
    def is_morse(cls, morse: str = None) -> bool:
        """Checks if morse is valid."""

        try:
            if not morse.strip():  # Check if empty string.
                return False

            # If a set of character or a character is present in {".", "-"},
            # then set(char) <= valid_symbols will evaluate to True.
            return all(
                set(char) <= {".", "-"} for char in cls._clean_morse(morse).split(" ")
            )

        except AttributeError:
            return False

    @classmethod
    def in_morse_chart(cls, char: str = None) -> tuple[str, str] | None:
        """Checks if letter, number, symbol, or morse is in the chart."""

        try:
            mod_char = char.strip().upper()

            # Check if the input character is Morse code.
            if cls.is_morse(char):
                # If Morse code, return the corresponding character and code from the list.
                return (
                    cls.characters[cls.codes.index(mod_char)],
                    cls.codes[cls.codes.index(mod_char)],
                )

            # If not, return the corresponding character and code from the list.
            return (
                cls.characters[cls.characters.index(mod_char)],
                cls.morse_chart[mod_char],
            )

        except (ValueError, TypeError, AttributeError):
            return None

    @classmethod
    def _update_chart(cls, char, morse):
        cls.morse_chart.update({char.upper(): cls._clean_morse(morse)})

        # Update each list to store the added item.
        cls.characters = list(cls.morse_chart.keys())
        cls.codes = list(cls.morse_chart.values())

    @classmethod
    def add_morse(cls, char: str = None, morse: str = None):
        """Adds morse code to the chart."""

        if not cls.is_morse(morse):
            raise MorseCodeError("Invalid or no morse code specified.")

        if (char.upper(), morse) in cls.morse_chart.items():
            raise MorseCodeError("Morse code already in the chart.")

        # Add to morse chart.
        cls._update_chart(char, morse)


class MorseEncrypt(Morse):
    @classmethod
    def encrypt_char(cls, char: str = None) -> str | None:
        """Encrypts a character."""

        try:
            return (
                " " # Adds a trailing space.
                if char.strip() == ""
                else cls.morse_chart.get(char.upper().strip()) + " "
            )

        except (TypeError, ValueError):
            return None

    @classmethod
    def encrypt(cls, message: str = None) -> str | None:
        """Encrypts a message."""

        morse_message = ""
        morse_message_li = []  # For debugging white spaces issue.

        try:
            for char in message.upper():
                morse_message += cls.encrypt_char(char)
                morse_message_li.append(cls.encrypt_char(char))

            return morse_message

        except (ValueError, TypeError, AttributeError):
            return None


class MorseDecrypt(Morse):
    @classmethod
    def decrypt_morse(cls, char: str = None) -> str | None:
        """Decrypts a single morse code."""

        try:
            return (
                " "  # Adds a trailing space.
                if char.strip() == ""
                else cls.characters[cls.codes.index(char.strip())]
            )

        except (ValueError, AttributeError):
            return None

    @classmethod
    def decrypt(cls, message: str = None) -> str | None:
        """Decrypts a message."""

        decrypted_message = ""
        decrypted_message_li = []  # For debugging white spaces issue.

        try:
            for morse in message.split(" "):
                decrypted_message += cls.decrypt_morse(morse)
                decrypted_message_li.append(cls.decrypt_morse(morse))

            return decrypted_message

        except (ValueError, AttributeError, TypeError):
            return None


def main():
    Morse.add_morse("GUI", ".---...-")
    print(f"In morse code chart: {Morse.in_morse_chart('GUI')}")
    print(f"Encrypt: {MorseEncrypt.encrypt('HELLO World!')}")
    print(
        f"Decrypt: {MorseDecrypt.decrypt('.... . .-.. .-.. ---  --. .. - .... ..- -... -.-.--')}"
    )
    print(f"Encrypt character: {MorseEncrypt.encrypt_char('d')}")
    print(f"Decrypt letter: {MorseDecrypt.decrypt_morse('-..-        ')}")
    print(f"Is morse: {Morse.is_morse('--.  ---.  ---')}")


if __name__ == "__main__":
    main()
