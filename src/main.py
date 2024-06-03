import random

acronyms = {
    "DNS": "Domain Name Service",
    "ISP": "Internet Service Provider",
    "NAT": "Network Address Translation",
}


def main():
    while True:
        (acronym, acronym_phrase) = random.choice(list(acronyms.items()))

        user_input = input(f"{acronym}: ")

        if user_input.lower().strip() == acronym_phrase.lower():
            print("You go, girl!")


if __name__ == "__main__":
    main()
