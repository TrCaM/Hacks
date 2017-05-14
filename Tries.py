# """ Node is defined as
class node:
    def __init__(self, data, parent):
        self.data = data
        self.parents = parent
        self.children = []
        self.count =1
# """

def add(word, root):
    ls = list(word)
    i=0
    origin = root
    while i<len(word):
        y=i
        for n in root.children:
            if n.data== ls[i]:
                root = n
                root.count +=1
                y+=1
                break
        if (y>i):
            i=y
            continue
        else:
            new_node = node(ls[i], root)
            root.children.append(new_node)
            root = new_node
            i+= 1
    root = origin

def find(prefix, root):
    ls =list(prefix)
    i=0
    while i<len(prefix):
        y=i
        for node in root.children:
            if node.data== ls[i]:
                root = node
                y+=1
                break
        if (y>i):
            i =y
            continue
        else:
            return 0
    return root.count

n = int(input().strip())
root = node('*', None)

for a0 in range(n):
    op, contact = input().strip().split(' ')
    if (op == "add"):
        add(contact, root)
    else:
        print(find(contact, root))
