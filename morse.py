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
        "/": "-..-.",
        "-": "-....-",
        "(": "-.--.",
        ")": "-.--.-",
    }
    characters = list(morse_chart.keys())
    codes = list(morse_chart.values())

    @classmethod
    def in_morse_chart(cls, char: str = None):
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
    def is_morse(cls, morse) -> bool:
        return bool("." in morse or "-" in morse)

    @classmethod
    def add_morse(cls, char: str = None, morse: str = None):
        if cls.is_morse(morse):
            if (char.upper(), morse) not in cls.morse_chart.items():
                cls.morse_chart.update({char.upper(): morse})

                cls.characters = list(cls.morse_chart.keys())
                cls.codes = list(cls.morse_chart.values())


class MorseEncrypt(Morse):
    @classmethod
    def encrypt_letter(cls, char: str = None) -> str | None:
        try:
            return " " if char == " " else cls.morse_chart.get(char) + " "
        except (TypeError, ValueError):
            return None

    @classmethod
    def encrypt(cls, message: str = None) -> str:
        try:
            morse_message: str = ""

            for char in message.upper():
                morse_message += cls.encrypt_letter(char)

            return morse_message.strip()

        except (ValueError, TypeError, AttributeError):
            return None


class MorseDecrypt(Morse):
    @classmethod
    def decrypt_char(cls, char: str = None) -> str | None:
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
        decrypted_message = ""
        try:
            for morse in message.split(" "):
                decrypted_message += cls.decrypt_char(morse)

            return decrypted_message

        except (ValueError, AttributeError, TypeError):
            return None


Morse.add_morse("new", "-. . .--")
print(Morse.morse_chart)
print(Morse.in_morse_chart("n"))
print(MorseEncrypt.encrypt("hello world"))
# print(MorseDecrypt.decrypt("-.-- . .- ....  -... .. - -.-. ...."))
# print(MorseDecrypt.decrypt_char())
