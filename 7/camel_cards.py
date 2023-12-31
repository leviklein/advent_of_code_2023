import pathlib
from collections import Counter

SUIT_ORDER = ['c', 'd', 'h', 's']
# from phevaluator
rank_map = {
    "2": 0, "3": 1, "4": 2, "5": 3, "6": 4, "7": 5, "8": 6, "9": 7,
    "T": 8, "J": 9, "Q": 10, "K": 11, "A": 12,
}
kind_map = {
    "10": 6, "5": 6, "4": 5, "fh": 4, "3": 3, "2p": 2, "1p": 1, "1": 0
}
PROBLEM_2 = True

# from https://blog.boot.dev/computer-science/binary-search-tree-in-python/
class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals


class Hand:
    def __init__(self, line):
        self.hand = line[0]
        self.bid = int(line[1])
        self.val = self.get_hand_value()
        pass

    def get_hand_value(self):
        counter = Counter(self.hand)
        counts = sorted(list(counter.values()), reverse=True)

        if(PROBLEM_2):
            top_2 = counter.most_common(2)
            base = top_2[-1][1] if "J" in top_2[0] else counts[0]
            most = base + counter['J']
        else:
            most = counts[0]

        if most >= 4:
            return kind_map[str(most)]
        elif most == 3:
            if counts[1] == 2:
                return kind_map["fh"]
            else:
                return kind_map["3"]
        elif most == 2:
            if counts[1] == 2:
                return kind_map["2p"]
            else:
                return kind_map["1p"]
        else:
            return kind_map["1"]

    def __lt__(self, other):
        if self.val == other.val:
            for i in range(len(self.hand)):
                if rank_map[self.hand[i]] != rank_map[other.hand[i]]:
                    return rank_map[self.hand[i]] < rank_map[other.hand[i]]
                else:
                    continue

        return self.val < other.val

    # def __repr__(self):
    #     # display x and y instead of address
    #     # return f'Hand(val={self.val}, bid={self.bid})'
        # return self.hand


if __name__ == "__main__":
    script_path = str(pathlib.Path(__file__).parent.resolve()) + "/"

    f = open(script_path + "input.txt", "r")
    # f = open(script_path + "test_input.txt", "r")
    a = f.readline()

    bst = BSTNode()
    if (PROBLEM_2):
        rank_map["J"] = -1
    row = 1
    while a.strip():
        bst.insert(Hand(a.strip().split()))
        a = f.readline()
        row += 1

    answer = 0
    ordered = bst.inorder([])
    for i in range(len(ordered)):
        answer += ordered[i].bid*(i+1)
        pass

    print(f"answer: {answer}")
    pass