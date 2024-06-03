import random
import yaml


def get_sets(file_path):
    try:
        with open(file_path, "r") as file:
            contents = yaml.safe_load(file)
            if next(iter(contents.keys())) == "sets":
                return contents["sets"]
    except FileNotFoundError:
        print(
            "Error: could not locate YAML file, please ensure this file exists."
        )


def print_set_selection(sets):
    for count, item in enumerate(sets, start=1):
        title = item["title"]
        print(f"[{count}]: {title}")


def select_set(sets):
    while True:
        set_input = input("> ")
        try:
            set_number = int(set_input)
            if 1 <= set_number <= len(sets):
                return set_number - 1
            else:
                print(
                    "Invalid number, please select a number from the list above."
                )
        except ValueError:
            print("Invalid input, please enter a number from the list above.")


def main():
    yaml_file_path = "../acronym.yaml"
    sets = get_sets(yaml_file_path)

    if len(sets) > 1:
        print_set_options(sets)
        selected_set_index = select_set(sets)
        selected_set = sets[selected_set_index]
    else:
        selected_set_index = 0
        selected_set = sets[selected_set_index]

    acronyms = selected_set["acronyms"]
    title = selected_set["title"]
    print(title)

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

    print("You have finished the set.")


if __name__ == "__main__":
    main()
