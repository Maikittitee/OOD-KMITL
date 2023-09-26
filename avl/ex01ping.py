class Node:
    def __init__(self, data, freq, left=None, right=None):
        self.freq = freq
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class Huffman:
    def __init__(self):
        self.root = None

    def insert(self, node, data, freq):
        if node is None:
            return Node(data, freq)
        elif freq < node.freq:
            node.left = self.insert(node.left, data, freq)
        elif freq == node.freq:
            if data < node.data:
                node.left = self.insert(node.left, data, freq)
            else:
                node.right = self.insert(node.right, data, freq)
        else:
            node.right = self.insert(node.right, data, freq)
        return node

    def inorder(self, node):
        if node is None:
            return []

        return (
            self.inorder(node.right)
            + [Node(node.data, node.freq)]
            + self.inorder(node.left)
        )

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print("     " * level, node)
            self.print_tree(node.left, level + 1)

    def print_code(self, node, code=""):
        s = ""
        if node is not None:
            s = self.print_code(node.right, code + "1")
            if node.data != "*":
                s += f"'{node.data}': '{code}'"
            a = self.print_code(node.left, code + "0")
            if a != "":
                s += ", " + a
        return s

    def search(self, node, data, code=""):
        if node is None:
            return None
        elif node.data == data:
            return code
        if node:
            s = self.search(node.right, data, code + "1")
            if s:
                return s
            s = self.search(node.left, data, code + "0")
            if s:
                return s


if __name__ == "__main__":
    inp = list(input("Enter Input : "))
    s = set(inp)

    h = Huffman()

    for i in s:
        h.root = h.insert(h.root, i, inp.count(i))

    data = h.inorder(h.root)
    
    temp = [data.pop()]

    while len(data) != 0 or len(temp) != 1:
        if len(temp) > 1:
            if data == [] or (data[-1].freq >= temp[0].freq + temp[1].freq):
                a, b = temp.pop(0), temp.pop(0)
                temp.append(Node("*", a.freq + b.freq, a, b))
            else:
                temp.append(data.pop())
        else:
            temp.append(data.pop())

    print("{" + f'{h.print_code(temp[0], "")}' + "}")
    h.print_tree(temp[0])
    print("Encoded! : ", end="")
    for key in inp:
        print(h.search(temp[0], key, ""), end="")