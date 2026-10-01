def count_pairs(word):
    upper_pairs = 0
    lower_pairs = 0
    for i in range(len(word) - 1):
        if word[i].isupper() and word[i + 1].isupper():
            upper_pairs += 1
        elif word[i].islower() and word[i + 1].islower():
            lower_pairs += 1
    return upper_pairs, lower_pairs


def count_letters(word):
    letters = 0
    for ch in word:
        if ch.isalpha():
            letters += 1
    return letters


def main():
    word = input("Enter a word: ")
    upper_pairs, lower_pairs = count_pairs(word)
    print("Lowercase pairs:", lower_pairs)
    print("Uppercase pairs:", upper_pairs)
    print("Total letters:", count_letters(word))


main()
