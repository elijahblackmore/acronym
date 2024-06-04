import random
import yaml


def get_sets():
    yaml_file_path = "../acronym.yaml"

    try:
        with open(yaml_file_path, "r") as file:
            contents = yaml.safe_load(file)
            if next(iter(contents.keys())) == "sets":
                return contents["sets"]
    except FileNotFoundError:
        print(
            "Error: could not locate YAML file, please ensure this file exists."
        )


def print_set_options(sets):
    if len(sets) == 1:
        return

    for count, item in enumerate(sets, start=1):
        title = item["title"]
        print(f"[{count}]: {title}")


def select_set(sets):
    set_index = 0

    if len(sets) == 1:
        return set_index

    while True:
        set_input = input("> ")
        try:
            set_index = int(set_input)
            if 1 <= set_index <= len(sets):
                return set_index - 1
            else:
                print(
                    "Invalid number, please select a number from the list above."
                )
        except ValueError:
            print("Invalid input, please enter a number from the list above.")


def play_set(sets_count, set):
    title = set["title"]
    print(title)
    acronyms = set["acronyms"]
    acronyms_copy = dict(acronyms)
    total_acronyms = len(acronyms)
    current_acronym_index = 1

    while len(acronyms) > 0:
        (acronym, acronym_phrase) = random.choice(list(acronyms.items()))
        while True:
            user_input = (
                input(
                    f"({current_acronym_index}/{total_acronyms}) {acronym}: "
                )
                .lower()
                .strip()
            )

            if user_input == acronym_phrase.lower():
                acronyms.pop(acronym)
                current_acronym_index += 1
                break
            else:
                print("Incorrect, try again!")

    set["acronyms"] = acronyms_copy
    prompt(sets_count, set)


def prompt(sets_count, selected_set):
    options = []

    if sets_count > 1:
        options = [
            "Back to set selection menu",
            "Replay current set",
            "Exit",
        ]
    else:
        options = ["Replay current set", "Exit"]

    for index, option in enumerate(options, start=1):
        print(f"[{index}]: {option}")

    while True:
        set_input = input("> ")

        try:
            set_index = int(set_input) - 1
            if options[set_index] == "Back to set selection menu":
                main()
            elif options[set_index] == "Replay current set":
                # print(selected_set)
                play_set(sets_count, selected_set)
            else:
                quit()

        except ValueError:
            print("Invalid input, please enter a number from the list above.")


def main():
    sets = get_sets()
    sets_count = len(sets)

    print_set_options(sets)
    selected_set_index = select_set(sets)
    selected_set = sets[selected_set_index]

    play_set(sets_count, selected_set)


if __name__ == "__main__":
    main()
