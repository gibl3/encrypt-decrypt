import string


class Vigenere:
    def __init__(self) -> None:
        self._alphabet = string.ascii_uppercase

    def _shift_letter(self, mode, key, letter, key_idx):
        key_char = self._get_key_char(key, key_idx)
        letter_idx, key_char_idx = self._get_indices(letter, key_char)

        new_idx = (letter_idx + key_char_idx * mode) % len(self._alphabet)
        return self._alphabet[new_idx]

    def _get_indices(self, letter, key_char):
        key_char_idx = self._alphabet.index(key_char.upper())
        letter_idx = self._alphabet.index(letter)

        return letter_idx, key_char_idx

    def _get_key_char(self, key: str, key_idx: int):
        #  Returns the letter of the given key at the specified index.
        return key[key_idx % len(key)]

    def _shift_text(self, text: str, key: str, mode: int):
        shifted_text = ""
        key_idx = 0
        text = text.upper()

        if not text.strip():
            return None

        for letter in text:
            if not letter.isalpha():
                shifted_text += letter
            else:
                shifted_text += self._shift_letter(mode, key, letter, key_idx)
                key_idx += 1

        return shifted_text

    def encrypt(self, text: str, key: str):
        try:
            return self._shift_text(text, key, 1)

        except (ValueError, AttributeError, TypeError):
            return None

    def decrypt(self, text: str, key: str):
        try:
            return self._shift_text(text, key, -1)

        except (ValueError, AttributeError, TypeError):
            return None


def main():
    key = "vigenere"
    text = "Hello, world!"
    cipher_text = "CMRPB, AFVGL!"

    vigenere = Vigenere()

    print(vigenere.encrypt(text, key))
    print(vigenere.decrypt(cipher_text, key))


if __name__ == "__main__":
    main()
