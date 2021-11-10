import random


def card_select():
    name = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    suit = [" of Spades", " of Clubs", " of Hearts", " of Diamonds"]
    random_name = random.choice(name)
    random_suit = random.choice(suit)
    result = f"{random_name}{random_suit}"
    return result


def points(hand):
    first_ace = False
    ace = False
    values = []
    puncte = []
    total = 0
    for i in hand:
        values.append(i)

    for each in values:
        card = each.split(" of")[0]
        puncte.append(card)
    try:
        if puncte[0] == "Ace" and puncte[1] == "Ace":
            first_ace = True
            total = 12
    except IndexError:
        pass
    else:
        for x in puncte:
            if x == "King":
                total += 10
            elif x == "Queen":
                total += 10
            elif x == "Jack":
                total += 10
            elif x == "Ace":
                total += 11
            else:
                total += int(x)

    if not first_ace and "Ace" in puncte:
        ace = True
    if ace and total > 21:
        total -= 10

    return total


def user():
    user_hand = []
    user_hand.append(card_select())
    user_hand.append(card_select())
    user_points = int(points(user_hand))
    print(f"Your hand: {user_hand} \nYour Score: {user_points}")
    print()
    while True:
        if user_points == 21:
            break
        elif user_points < 21:
            cmd = input("[H]it or [S]tay: ").upper()
            if cmd == "H":
                user_hand.append(card_select())
                user_points = points(user_hand)
                print(f" Your hand: {user_hand} \n Your Score: {user_points}")
            elif cmd == "S":
                print()
                break
            else:
                print("Invalid Command. Try only H or S")
        else:
            break

    return user_points


def cp(user_score):
    user_play = False
    if user_score < 21:
        user_play = True
    cp_hand = []
    cp_hand.append(first_cp_card)
    cp_points = int(points(cp_hand))

    if user_play:
        while cp_points < 17:
            cp_hand.append(card_select())
            cp_points = points(cp_hand)
            if cp_points > user_score:
                break

    return cp_points, cp_hand


def main(cp_card):
    print(f"CP Hand: {cp_card}")
    print()
    user_score = user()
    cp_points, cp_hand = cp(user_score)
    if user_score <= 21:
        print(f"CP Hand: {cp_hand}, SCORE: {cp_points}")
        if cp_points > 21:
            print("CP lose! score mai mare de 21")
        elif cp_points > user_score:
            print("CP WIN")
        elif cp_points < user_score:
            print("Player WIN")
        else:
            print("TIE")
    else:
        print("!! BUSTED !!, Your score is too high !")


first_cp_card = card_select()
main(first_cp_card)
