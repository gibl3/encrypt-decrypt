class Morse:
    def __init__(self):
        self._morse_chart = {
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
        self._characters = list(self._morse_chart.keys())
        self._codes = list(self._morse_chart.values())

    @property
    def morse_chart(self) -> dict[str, str]:
        return self._morse_chart

    @property
    def characters(self) -> list[str]:
        return self._characters

    @property
    def codes(self) -> list[str]:
        return self._codes

    def parse_morse(self, morse: str) -> str:
        """Removes leading, internal, and trailing spaces."""

        if not morse.split():
            return None

        if not all(set(char.strip()) <= {".", "-"} for char in morse.split()):
            return None

        # NOTE: This will not return a formatted morse code in a sentence structure
        # NOTE: rather it will return a sequence of morse codes separated with double spaces.
        return "  ".join(morse.split())

    def _has_dots_and_dashes(self, morse: str = None) -> bool:
        """Parse and checks if morse contains valid symbols."""
        # NOTE: As long as it only contains dots and dashes,
        # doesn't matter the spacing, it will return True. Otherwise, False.

        try:
            if not morse.strip():  # Check if empty string.
                return False

            # Split the given Morse code into individual characters.
            # For each character in the split Morse code:
            # Check if set(char) is a subset of the set {".", "-"}.
            # If set(char) contains only the characters ".", or "-", it is considered as valid.
            # If set(char) contains any other characters, it is considered as invalid.
            # Return True if all set(char)s are valid, False otherwise.
            return all(set(char.strip()) <= {".", "-"} for char in morse.split())

        except AttributeError:
            return False

    def in_morse_chart(self, char: str = None) -> tuple[str, str] | None:
        """Checks if a letter, number, symbol, or morse is in the chart."""

        try:
            mod_char = char.strip().upper()

            if self._has_dots_and_dashes(char):
                return (
                    self.characters[self.codes.index(mod_char)],
                    self.codes[self.codes.index(mod_char)],
                )

            return (
                self.characters[self.characters.index(mod_char)],
                self.morse_chart[mod_char],
            )

        except (ValueError, TypeError, AttributeError):
            return None

    def _is_morse_in_chart(self, char: str, morse: str) -> bool:
        """Checks if morse code or character is already in the chart."""

        return (
            (char.upper(), morse.strip()) in self._morse_chart.items()
            or morse.strip() in self._codes
            or char.upper().strip() in self._characters
        )

    def add_morse(self, char: str = None, morse: str = None):
        """Adds morse code to the chart."""

        if not self._has_dots_and_dashes(morse):
            raise ValueError("Invalid or no morse code specified.")

        if self._is_morse_in_chart(char, morse):
            raise ValueError("Morse code already in the chart.")

        self._morse_chart.update({char.upper(): self.parse_morse(morse)})
        self._characters = list(self._morse_chart.keys())
        self._codes = list(self._morse_chart.values())


class MorseEncrypt:
    def __init__(self, morse) -> None:
        self._morse = morse

    def encrypt_char(self, char: str = None) -> str | None:
        """Encrypts a character."""

        try:
            return (
                " "  # Add a trailing space.
                if char.strip() == ""
                else self._morse.morse_chart.get(char.upper().strip()) + " "
            )

        except (TypeError, ValueError):
            return None

    def encrypt(self, message: str = None) -> str | None:
        """Encrypts a message."""

        morse_message = ""

        try:
            for char in message.upper():
                morse_message += self.encrypt_char(char)

            return morse_message

        except (ValueError, TypeError, AttributeError):
            return None


class MorseDecrypt:
    def __init__(self, morse) -> None:
        self._morse = morse

    def decrypt_morse(self, char: str = None) -> str | None:
        """Decrypts a single morse code."""

        try:
            return (
                " "  # Add a trailing space.
                if char.strip() == ""
                else self._morse.characters[self._morse.codes.index(char.strip())]
            )

        except (ValueError, AttributeError):
            return None

    def decrypt(self, message: str = None) -> str | None:
        """Decrypts a message."""

        decrypted_message = ""

        try:
            for morse in message.split(" "):
                decrypted_message += self.decrypt_morse(morse)

            return decrypted_message

        except (ValueError, AttributeError, TypeError):
            return None


def main():
    morse = Morse()
    morse.add_morse("67", "-.----..-.---")
    print(morse.in_morse_chart("67"))

    encrypt = MorseEncrypt(morse)
    print(encrypt.encrypt("This is bus"))

    decrypt = MorseDecrypt(morse)
    print(decrypt.decrypt("- .... .. ...  .. ...  -... ..- ..."))


if __name__ == "__main__":
    main()
