import re
import pathlib


# from https://blog.boot.dev/computer-science/binary-search-tree-in-python/
class BTNode:
    def __init__(self, val=None, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

    def insert(self, val, left, right):
        if not self.val:
            self.val = val
            self.left = BTNode(left)
            self.right = BTNode(right)
            return

        if self.val == val:
            self.left = BTNode(left)
            self.right = BTNode(right)
            return

        print(val, left, right)
        self.get_node(val).insert(val, left, right)
        return

        val_node = self.get_node(val)
        val_node.left = self.get_node(left)
        val_node.right = self.get_node(right)
        # if val < self.val:
        #     if self.left:
        #         self.left.insert(val)
        #         return
        #     self.left = BSTNode(val)
        #     return

        # if self.right:
        #     self.right.insert(val)
        #     return
        # self.right = BSTNode(val)

    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)

        if self.right == None:
            return False
        return self.right.exists(val)

    def get_node(self, val):
        if (self == None):
            return BTNode(val)

        if val == self.val:
            return self

        if self.left == None:
            return None
        res1 = self.left.get_node(val)
        if res1:
            return res1

        if self.right == None:
            return None
        res2 = self.right.get_node(val)
        if res2:
            return res2

    def __str__(self):
        return f"{self.val}"

    def __repr__(self):
        return f"{self.val}"

    def __eq__(self, other):
        if other == None:
            return False
        return self.val == other.val

    def __hash__(self):
        return hash(self.val)

    # def ifNodeExists(node, key):
    #     if (node == None):
    #         return False

    #     if (node.data == key):
    #         return True

    #     """ then recur on left subtree """
    #     res1 = ifNodeExists(node.left, key)
    #     # node found, no need to look further
    #     if res1:
    #         return True

    #     """ node is not found in left,
    #     so recur on right subtree """
    #     res2 = ifNodeExists(node.right, key)

    #     return res2


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

def process_input(line):
    line = re.findall("\w+", a)
    nodes_to_process[line[0]] =  line
    # TREE.insert(*line)
    pass

def build_tree():
    AAA = nodes_to_process["AAA"]
    TREE.insert(*AAA)
    node = TREE.get_node("AAA")
    while len(nodes_to_process):
        if node.left.val in nodes_to_process:
            TREE.insert(*(nodes_to_process.pop(node.left.val)))
            node = TREE.get_node(node.left.val)
        elif node.right.val in nodes_to_process:
            TREE.insert(*(nodes_to_process.pop(node.right.val)))
            node = TREE.get_node(node.right.val)
        else:
            node = TREE.get_node("AAA")
        pass


def fractionToDecimal(numr, denr):

    # Initialize result
    res = ""
    # Create a map to store already seen
    # remainders. Remainder is used as key
    # and its position in result is stored
    # as value. Note that we need position
    # for cases like 1/6.  In this case,
    # the recurring sequence doesn't start
    # from first remainder.
    mp = {}
    # Find first remainder
    rem = numr % denr
    # Keep finding remainder until either
    # remainder becomes 0 or repeats
    while ((rem != 0) and (rem not in mp)):
        # Store this remainder
        mp[rem] = len(res)
        # Multiply remainder with 10
        rem = rem * 10
        # Append rem / denr to result
        res_part = rem // denr
        res += str(res_part)
        # Update remainder
        rem = rem % denr
    if (rem == 0):
        return ""
    else:
        return res[mp[rem]:]


from itertools import groupby

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


import datetime as dt

def print_every_n_seconds(t, seconds, line):
    delta = dt.datetime.now()-t
    if delta.seconds >= seconds:
        print(line)
    return delta.seconds >= seconds

if __name__ == "__main__":
    script_path = str(pathlib.Path(__file__).parent.resolve()) + "/"

    f = open(script_path + "input.txt", "r")
    # f = open(script_path + "test_input.txt", "r")
    a = f.readline()

    TREE = BTNode()
    nodes_to_process = set()
    nodes_to_process = {}

    row = 1
    while a:
        if row == 1:
            command = a.strip()

        elif a.strip():
            process_input(a.strip())

        a = f.readline()
        row += 1

    pass

    # build_tree()

    # i = 0
    # node = TREE.get_node("AAA")
    # while True:
    #     direction = command[i % len(command)]
    #     if direction == "R":
    #         node = TREE.get_node(node.right.val)
    #     else:
    #         node = TREE.get_node(node.left.val)
    #     i += 1

    #     if node.val == "ZZZ":
    #         break

    i = 0
    part1_sequence = []
    node = nodes_to_process["AAA"]
    while True:
        direction = command[i % len(command)]
        part1_sequence.append(direction + node[0])
        if direction == "R":
            node = nodes_to_process[node[2]]
        else:
            node = nodes_to_process[node[1]]
        i += 1

        if node[0] == "ZZZ":
            break
    print(f"part 1: {i}")

    nodes = [ nodes_to_process[x] for x in filter(lambda y: y[2] == "A", nodes_to_process) ]

    # nodes = [ nodes_to_process["AAA"] ]
    REPEATS = []
    print(nodes)
    for start_node in nodes:
        i = 0
        sequence = []
        mp = {}
        node = start_node
        direction = command[i % len(command)]
        while (str(i%len(command)) +direction + node[0] not in mp):
            mp[str(i%len(command)) +direction + node[0]] = len(sequence)
            sequence.append(str(i%len(command)) +direction + node[0])
            if direction == "R":
                node = nodes_to_process[node[2]]
            else:
                node = nodes_to_process[node[1]]
            i += 1
            direction = command[i % len(command)]


        REPEATS.append(sequence)
        # print(sequence)
        # print(sequence[mp[str(i%len(command)) +direction + node[0]]:])
        for x in filter(lambda y: y[3] == "A", sequence):
            print(f"NUMBER OF ZZZZ: {x}")

    PERIODS = []
    for node in REPEATS:
        print(f"NODE: {node[0]}")
        for x in filter(lambda y: y[-1] == "Z", node):
                print(f"NUMBER OF {node[0]}: {x}")
                print(len(node))
                print(node.index(x))
                PERIODS.append(node.index(x))

    # node = nodes[n]
    for search_node in nodes:
        i = 0
        n = 0
        node = search_node
        while True:
            direction = command[i % len(command)]
            part1_sequence.append(direction + node[0])
            if direction == "R":
                node = nodes_to_process[node[2]]
            else:
                node = nodes_to_process[node[1]]
            i += 1

            if node[0][-1] == "Z":
                print(f"found Z!!: {i}")

                if i % PERIODS[nodes.index(search_node)] == 0:
                    print(f"i:{i}, {node[0]}")
                    n += 1
                    if n == 5:
                        break

        # if node[0] == "NGZ":
        #     break


    print(f"PERIODS: {PERIODS}")

    # PERIODS = [20777, 19199, 18673, 16043, 12361, 15517]
    x = 20777
    t = dt.datetime.now()

    i = 481301439091495400000
    while True:
        t = dt.datetime.now() if print_every_n_seconds(t, 60, x*i) else t
        i += 1
        answer = True
        for test in PERIODS[1:]:
            if x*i % test:
                answer = False
                break
        if answer:
            break


    print("DAY 8 DONE???")
    print(x*i)
    print(i)