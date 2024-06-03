import random
import yaml


def main():
    with open("../acronym.yaml", "r") as file:
        contents = yaml.safe_load(file)

    sets = contents["sets"]

    for count, item in enumerate(sets, start=1):
        title = item["title"]
        print(f"[{count}]: {title}")
        acronyms = item["acronyms"]

    while True:
        set_input = input("> ")

        try:
            set_number = int(set_input)
            if 1 <= set_number <= len(sets):
                break
            else:
                print(
                    "Invalid number, please select a number from the list above."
                )
        except ValueError:
            print("Invalid input, please enter a number from the list above.")

    selected_set = sets[set_number - 1]

    acronyms = selected_set["acronyms"]
    title = selected_set["title"]
    print(title)

    total_acronyms = len(acronyms)
    remaining_acronyms = total_acronyms

    while len(acronyms) > 0:
        (acronym, acronym_phrase) = random.choice(list(acronyms.items()))

        while True:
            user_input = (
                input(f"({remaining_acronyms}/{total_acronyms}) {acronym}: ")
                .lower()
                .strip()
            )

            if user_input == acronym_phrase.lower():
                acronyms.pop(acronym)
                remaining_acronyms -= 1
                break
            else:
                print("Incorrect, try again!")

        print("You have finished the set.")


if __name__ == "__main__":
    main()
