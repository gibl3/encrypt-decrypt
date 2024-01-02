import string


class Caesar:
    def __init__(self) -> None:
        self._alphabet = string.ascii_lowercase
        self._alpha_len = len(self._alphabet)

    @property
    def alpha_len(self):
        return self._alpha_len

    @property
    def alphabet(self):
        return self._alphabet

    def decrypt(self, shift: int = 3, text: str = ""):
        decrypted_text = ""

        try:
            if not text.strip():
                return None

            for letter in text.lower():
                if not letter.isalpha():
                    decrypted_text += letter

                else:
                    sub_idx = (self._alphabet.index(letter) - shift) % self._alpha_len
                    decrypted_text += self._alphabet[sub_idx]

            return decrypted_text

        except (ValueError, AttributeError, TypeError):
            return None


class CaesarEncrypt:
    def __init__(self, caesar) -> None:
        self._caesar = caesar

    def encrypt(self, shift: int = 3, text: str = ""):
        try:
            return self._encrypt_text(shift, text.lower())

        except (ValueError, AttributeError, TypeError):
            return None

    def _encrypt_text(self, shift: int, text: str) -> str:
        encrypted_text = ""

        if not text.strip():
            return None

        for letter in text:
            if not letter.isalpha():
                encrypted_text += letter
            else:
                encrypted_text += self._encrypt_letter(letter, shift)

        return encrypted_text

    def _encrypt_letter(self, letter: str, shift: int) -> str:
        sub_idx = (self._caesar.alphabet.index(letter) + shift) % self._caesar.alpha_len
        return self._caesar.alphabet[sub_idx]


class CaesarDecrypt:
    def __init__(self, caesar) -> None:
        self._caesar = caesar

    def decrypt(self, shift: int = 3, text: str = ""):
        try:
            return self._decrypt_text(shift, text.lower())

        except (ValueError, AttributeError, TypeError):
            return None

    def _decrypt_text(self, shift: int, text: str) -> str:
        decrypted_text = ""

        if not text.strip():
            return None

        for letter in text:
            if not letter.isalpha():
                decrypted_text += letter
            else:
                decrypted_text += self._decrypt_letter(letter, shift)

        return decrypted_text

    def _decrypt_letter(self, letter: str, shift: int) -> str:
        sub_idx = (self._caesar.alphabet.index(letter) - shift) % self._caesar.alpha_len
        return self._caesar.alphabet[sub_idx]


def main():
    caesar = Caesar()
    encrypt = CaesarEncrypt(caesar)
    decrypt = CaesarDecrypt(caesar)

    print(encrypt.encrypt(shift=21, text="Hello, world!"))
    print(decrypt.decrypt(shift=21, text="czggj, rjmgy!"))


if __name__ == "__main__":
    main()
