from utils import read_file_to_list


def hand_type(hand: str) -> int:
    card_counter = [0] * 13
    card_type = {"A":12, "K":11, "Q":10, "J":9, "T":8, "9":7, "8":6, "7":5, "6":4, "5":3, "4":2, "3":1, "2":0}
    for l in hand:
        card_counter[card_type[l]] += 1
    match max(card_counter):
        case 5:
            return 6
        case 4:
            return 5
        case 3:
            if 2 in card_counter:
                return 4
            else:
                return 3
        case 2:
            if card_counter.count(2) == 2:
                return 2
            else:
                return 1
        case _:
            return 0


def hand_type_with_joker(hand: str) -> int:
    card_counter = [0] * 12
    jokers = 0
    card_type = {"A":11, "K":10, "Q":9, "T":8, "9":7, "8":6, "7":5, "6":4, "5":3, "4":2, "3":1, "2":0}
    for l in hand:
        if l == "J":
            jokers += 1
        else:
            card_counter[card_type[l]] += 1
    card_counter[card_counter.index(max(card_counter))] += jokers
    
    match max(card_counter):
        case 5:
            return 6
        case 4:
            return 5
        case 3:
            if 2 in card_counter:
                return 4
            else:
                return 3
        case 2:
            if card_counter.count(2) == 2:
                return 2
            else:
                return 1
        case _:
            return 0

    

def hand_strength(hand: str) -> list:
    card_type = {"A":12, "K":11, "Q":10, "J":9, "T":8, "9":7, "8":6, "7":5, "6":4, "5":3, "4":2, "3":1, "2":0}
    strength = []

    strength.append(hand_type(hand[0]))

    for l in hand[0]:
        strength.append(card_type[l])

    return strength


def hand_strength_with_joker(hand: str) -> list:
    card_type = {"A":12, "K":11, "Q":10, "J":0, "T":9, "9":8, "8":7, "7":6, "6":5, "5":4, "4":3, "3":2, "2":1}
    strength = []

    strength.append(hand_type_with_joker(hand[0]))

    for l in hand[0]:
        strength.append(card_type[l])
        
    return strength


if __name__ == "__main__":
        
    puzzle_input = read_file_to_list("inputs/07/input.txt")
    hands = [line.split() for line in puzzle_input]
    hands.sort(key=hand_strength)

    winninngs = 0
    for rank, hand in enumerate(hands, start=1):
        winninngs += int(hand[1]) * (rank)

    print("part 1:",winninngs)

#----------------------------------------------------------------------------------------

    hands.sort(key=hand_strength_with_joker)

    winninngs = 0
    for rank, hand in enumerate(hands, start=1):
        winninngs += int(hand[1]) * (rank)
        
    print("part 2:",winninngs)