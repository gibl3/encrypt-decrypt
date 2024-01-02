import string


class Caesar:
    def __init__(self) -> None:
        self._alphabet = string.ascii_lowercase
        self._alpha_len = len(self._alphabet)

    def _shift_letter(self, letter: str, shift: int, mode: int) -> str:
        sub_idx = (self._alphabet.index(letter) + shift * mode) % self._alpha_len
        return self._alphabet[sub_idx]

    def _shift_text(self, shift: int, text: str, mode: int) -> str:
        shifted_text = ""

        if not text.strip():
            return None

        for letter in text:
            if not letter.isalpha():
                shifted_text += letter
            else:
                shifted_text += self._shift_letter(letter, shift, mode)

        return shifted_text

    def encrypt(self, shift: int = 3, text: str = ""):
        try:
            return self._shift_text(shift, text.lower(), 1)

        except (ValueError, AttributeError, TypeError):
            return None

    def decrypt(self, shift: int = 3, text: str = ""):
        try:
            return self._shift_text(shift, text.lower(), -1)

        except (ValueError, AttributeError, TypeError):
            return None


def main():
    caesar = Caesar()

    print(caesar.encrypt(shift=21, text="Hello, world!"))
    print(caesar.decrypt(shift=21, text="czggj, rjmgy!"))


if __name__ == "__main__":
    main()
