import re
import pathlib
from phevaluator import Card, evaluate_cards



class Hand:
    def __init__(self, line):
        self.hand = line[0]
        self.bid = line[1]
        self.val = self.get_hand_value()
    
    def get_hand_value(self):
        cards = []
        for i in self.hand:
            # add dynamic suit adder
            cards.append(i + "d")
        return evaluate_cards(*cards)
            



if __name__ == "__main__":
    script_path = str(pathlib.Path(__file__).parent.resolve()) + "/"

    f = open(script_path + "input.txt", "r")
    f = open(script_path + "test_input.txt", "r")
    a = f.readline()

    row = 1
    while a.strip():
        print(Hand(a.strip().split()))

        a = f.readline()
        row += 1