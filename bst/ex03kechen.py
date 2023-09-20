class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
    
    def __repr__(self) -> str:
        return str(self.value)

class Tree:
    def __init__(self) -> None:
        self.root = None

    def build_binary_tree(self, input_list):
        nodes = {}
        root = None

        for parent_value, child_value in input_list:
            parent_node = nodes.get(parent_value, None)
            child_node = nodes.get(child_value, None)
            if (not parent_node):
                parent_node = Node(parent_value)
                nodes[parent_value] = parent_node
            if (not child_node):
                child_node = Node(child_value)
                nodes[child_value] = child_node
            if (not parent_node.left):
                parent_node.left = child_node
            else:
                parent_node.right = child_node
            if (not root):
                root = parent_node
        return (root)
                    
    def topView(self):
        q = []
        q.append((self.root, 0))
        hori_distance = 0
        l_distance = 0
        r_distance = 0
        left = []
        right = []
        while (len(q) > 0):
            node, hori_distance = q[0]
            if (hori_distance < l_distance):
                left.append(node.value)
                l_distance = hori_distance
            elif (hori_distance > r_distance):
                right.append(node.value)
                r_distance = hori_distance
            if (node.left != None):
                q.append((node.left, hori_distance-1))
            if (node.right != None):
                q.append((node.right, hori_distance+1))
            q.pop(0)
        while (len(left) > 0):
            x = left.pop()
            print(x, end=" ")
        print(self.root.value, end=" ")
        for x in right:
            print(x, end=" ")

t= Tree()
inp = [i.split(" ") for i in input("Enter Input : ").split(",")]
t.root = t.build_binary_tree(inp)
print("Top view : ",end="")
t.topView()
print()