from utils import read_file_to_list

class Scratchcard:
    card_list = []
    def __init__(self, line: str) -> None:
        self.id = int(line[5:8])

        self.winning_numbers = line[10:39].split()
        self.your_numbers = line[41:].split()
        self.card_amount = 1
        Scratchcard.card_list.append(self)
    

    def calculate_wins(self):
        number_of_winning_numbers = 0
        for i in self.your_numbers:
            if i in self.winning_numbers:
                number_of_winning_numbers += 1
        return number_of_winning_numbers


    def points(self):
        number_of_winning_numbers = self.calculate_wins()
        if number_of_winning_numbers > 0:
            return 2 ** (number_of_winning_numbers-1)
        else:
            return 0
        
    
    def win_more_scratchcards(self):
        wins = self.calculate_wins()
        for i in range(wins):
            Scratchcard.card_list[self.id + i].increase_card_amount(self.card_amount)
        return self.card_amount
    

    def increase_card_amount(self, amt):
        self.card_amount += amt

                

def total_points(scratchcard) -> int:
    points = [card.points() for card in scratchcard]
    output = sum(points)
    return output


def process_cards():
    total_cards = 0
    for card in Scratchcard.card_list:
        total_cards += card.win_more_scratchcards()
        # print(f"after processing {card.id} cards, you now have {total_cards} total scratchcards")
    print("part 2:", total_cards)

if __name__ == "__main__":
    cards = read_file_to_list("inputs/04/input.txt")
    all_scratchcards = [Scratchcard(card) for card in cards]
    print("part 1:", total_points(all_scratchcards))
    process_cards()