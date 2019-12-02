#3 2019/11/30 Medium

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return self.val


def main():
    node = Node(20, Node(8, Node(4), Node(12, Node(10), Node(14))))
    #node = Node(20, None, Node(8, None, Node(10, None, Node(5))))

    s = serialize(node)
    print(s)
    n, num = deserialize(s)
    print(serialize(n))

def serialize(node):
    if (node == None):
        return "-1"
    else:
        return str(node.val) + " " + serialize(node.left) + " " + serialize(node.right)



def deserialize(s):
    array = s.split(' ')
    #print(array)
    if (array[0] == "-1"):
        return None, 1
    else:
        node = Node(array[0])
        node.left, numleft = deserialize(' '.join(array[1:]))
        node.right, numright = deserialize(' '.join(array[1+numleft:]))
    return node, numleft + numright + 1


main()
