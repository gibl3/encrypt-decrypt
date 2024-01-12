grid = ["ABCDE", "FGHIJ", "LMNOP", "QRSTU", "VWXYZ"]


def tap_code(message: str):
    message = message.upper()
    cipher_text = []

    for letter in message:
        if letter == "K":
            letter = "C"

        for cell in grid:
            if letter in cell:
                row = grid.index(cell) + 1
                col = cell.index(letter) + 1
                cipher_text.append(f"{row},{col}")

    return " ".join(cipher_text)


def tap_decode(cipher_text: str):
    tap_codes = [tuple(map(int, tap.split(","))) for tap in cipher_text.split()]

    decoded_message = ""
    for tap in tap_codes:
        # Adjust to 0-based indexing
        row = tap[0] - 1
        col = tap[1] - 1

        # Ensure the row and column indices are within bounds
        row %= len(grid)
        col %= len(grid[row])

        decoded_message += grid[row][col]

    return decoded_message


def main():
    text = "DOG"
    cipher_text = "1,4 3,4 2,2"

    print(tap_code(text))
    print(tap_decode(cipher_text))


if __name__ == "__main__":
    main()
