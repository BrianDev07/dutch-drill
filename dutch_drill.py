from random import choice
from os import system, name


def clear_console() -> None:
    system("cls") if name == "nt" else system("clear")


# This method separates the input text into a list, where each element
# is divided by ':'. This way, the element in index 0 is the Dutch sentence
# and any other elements after index 0 are the English translations.
def split_into_list(input_text: str) -> list:
    return input_text.split(':')


# Deletes punctuation marks and converts strings to lower case.
def simplify_answer(user_answer: str) -> str:
    return (user_answer
        .replace("?", "")
        .replace(",", "")
        .replace(".", "")
        .replace("!", "")
        .lower()
    )


# Opens the text file that contains all the sentences and returns a random one.
def pick_random_line() -> str:
    with open("sentences.txt", "r") as file:
        lines = file.readlines()

    return choice(lines)


# Checks if the translation is one of the possible ones given a sentence.
def check_if_valid(simplified_translations: list[str], answer: str) -> bool:
    return simplify_answer(answer) in simplified_translations


def main() -> None:
    streak: int = 0
    clear_console()

    while True:
        dutch_and_english: list = split_into_list(pick_random_line())  # holds sentences in both Dutch and English
        sentence_in_dutch: str = dutch_and_english[0]  # picks first element in the array
        translations: list = []
        simplified_translations: list = [] # translations with no punctuation

        for i in range(1, len(dutch_and_english) - 1):
            translations.append(dutch_and_english[i])   # saves translations, which start from index 1 of the list
            simplified_translations.append(simplify_answer(dutch_and_english[i]))

        print(f"Type this sentence in English (enter to skip):\n{sentence_in_dutch}")
        answer = input("\nAnswer: ")

        if check_if_valid(simplified_translations, answer):
            print("Correct!")
            streak += 1
        else:
            print(f"Incorrect!\nPossible answer: {choice(translations)}")
            streak = 0

        input("Press enter to continue...\n")
        clear_console()

        if streak % 5 == 0 and streak > 0:
            print(f"{streak} sentences in a row with no mistakes! Good job!")
            input()

        clear_console()


if __name__ == "__main__":
    main()
