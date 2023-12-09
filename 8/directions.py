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
    node = nodes_to_process["AAA"]
    while True:
        direction = command[i % len(command)]
        if direction == "R":
            node = nodes_to_process[node[2]]
        else:
            node = nodes_to_process[node[1]]
        i += 1

        if node[0] == "ZZZ":
            break
    print(f"part 1: {i}")

    i = 0
    nodes = [ nodes_to_process[x] for x in filter(lambda y: y[2] == "A", nodes_to_process) ]
    # nodes = [ nodes_to_process["AAA"] ]
    print(nodes)
    while True:
        direction = command[i % len(command)]
        if direction == "R":
            for j in range(len(nodes)):
                nodes[j] = nodes_to_process[nodes[j][2]]
        else:
            for j in range(len(nodes)):
                nodes[j] = nodes_to_process[nodes[j][1]]
        i += 1

        if all(loc[2] == 'Z' for (loc, _, _) in nodes):
            print(f"i: {i}, nodes: {[x[0] for x in nodes]}")
            break
        if (i % 10000000 == 0):
            print(f"i: {i}, nodes: {[x[0] for x in nodes]}")
    print(f"part 2: {i}")