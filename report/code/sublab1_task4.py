points = {
    "AEIOULNSTR": 1,
    "DG": 2,
    "BCMP": 3,
    "FHVWY": 4,
    "K": 5,
    "JX": 6,
    "QZ": 10,
}


def word_score(word):
    total = 0
    for ch in word.upper():
        for letters, value in points.items():
            if ch in letters:
                total += value
    return total


def main():
    word = input("Enter a word: ")
    print("Word score:", word_score(word))


main()
