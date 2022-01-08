import random


def random_chose_word():
    words = ["saptamana", "ziua", "vaccin", "covid", "pacanea", "robot", "sarpe", "casa", "militar", "politist", "lautar", "ciocan", "cocean", "paznic", "brate", "ulei", "schita", "cartof", "salam", "gaina", "calculator", "extravagant", "exagerat"]
    word_chose = random.choice(words).upper()
    words = list(word_chose)
    print(f"Cuvantul este de {len(word_chose)} litere")
    return words


def hangman(words):
    unique = []
    used_letters = []
    lives = 7
    counter = 0
    while counter < lives:
        word_list = [letter if letter in unique else "_" for letter in words]
        if "_" not in word_list:
            print(f"Felicitari invocatorule! cuvantul era ", "".join(words))
            break
        else:
            print(f"Curent word is :", " ".join(word_list))

        guess = input("Guess the word: ").upper()
        if guess in used_letters:
            print("Deja ai folosit litera asta!")
        elif len(guess) < 2:
            for each in guess:
                if each in words:
                    unique.append(each)
                else:
                    used_letters.append(each)
                    counter += 1
                    print(f"You have {lives - counter} lives left")
                    print("Litera nu-i in cuvant!")
                    desene(counter)
        else:
            print("Doar litere!")

        if counter == lives:
            print("Ai depasit incercarile...ai pierdut")
            print("Cuvantul era ", "".join(words))


def desene(counter):
    if counter == 7:
        print("____")
        print("|  |")
        print("|  O")
        print("| \ /")
        print("|  |")
        print("| / \ ")
        print("| H A N G M A N")
        print("|____")
        print("! YOU LOSER !")

    if counter == 6:
        print("____")
        print("|  |")
        print("|  O")
        print("| \ /")
        print("|  |")
        print("| /  ")
        print("| H A N G M A ")
        print("|____")

    if counter == 5:
        print("____")
        print("|  |")
        print("|  O")
        print("| \ /")
        print("|  |")
        print("|   ")
        print("| H A N G M  ")
        print("|____")

    if counter == 4:
        print("____")
        print("|  |")
        print("|  O")
        print("| \ /")
        print("|  ")
        print("|   ")
        print("| H A N G   ")
        print("|____")

    if counter == 3:
        print("____")
        print("|  |")
        print("|  O")
        print("| \ ")
        print("|  ")
        print("|   ")
        print("| H A N   ")
        print("|____")

    if counter == 2:
        print("____")
        print("|  |")
        print("|  O")
        print("|  ")
        print("|  ")
        print("|   ")
        print("| H A    ")
        print("|____")

    if counter == 1:
        print("____")
        print("|  |")
        print("|  ")
        print("|  ")
        print("|  ")
        print("|   ")
        print("| H     ")
        print("|____")


hangman(random_chose_word())
