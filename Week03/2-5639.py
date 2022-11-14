import sys

sys.setrecursionlimit(10**5)


class Node:
    def __init__(self, name):      
        self.name = name
        self.left_child = None
        self.right_child = None
        return
   

    def adopt_left(self, left):     # 최대 2명의 아이를 입양 받을 수 있다.
        self.left_child = left
        return

    def adopt_right(self, right):
        self.right_child = right
        return


def make_tree(parent, child): 

    if child < parent.name:
        if not parent.left_child:
            parent.adopt_left(Node(child))
        # 왼쪽에 이미 아이를 입양 받았을 때는 자신의 아이의 아이로 즉, 손자로 입양 한다.
        else:
            make_tree(parent.left_child, child)

    elif child > parent.name:
        if not parent.right_child:
            parent.adopt_right(Node(child))
        else:
        # 오른쪽에 이미 아이를 입양 받았을 때는 자신의 아이의 아이로 즉, 손자로 입양 한다.
            make_tree(parent.right_child, child)

    return

def post_trav(parent):
    if parent.left_child:
        post_trav(parent.left_child)
    if parent.right_child:
        post_trav(parent.right_child)
    print(parent.name)

    return

tree = list()

while True:
    try:
        tree.append(int(input()))
    except:
        break

root = Node(tree[0])         # 뿌리 생성 

for i in range(1, len(tree)):

    make_tree(root, tree[i]) #부모이름, 아이이름
    
post_trav(root)