# https://contest.yandex.ru/contest/23758/problems/E/
# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class DoubleConnectedNode:
        def __init__(self, value, next=None, prev=None):
            self.value = value
            self.next = next
            self.prev = prev


def print_linked_list(vertex):
    while vertex:
            print(vertex.value, end=" -> ")
            vertex = vertex.next
    print("None")

# логика следующая, необходимо next поменять местами с prev
# Original list: A <--> B <--> C <--> D
# Step 1:
# A <--> null  B <--> C <--> D
# Step 2:
# null <--> A <--> B  C <--> D
# Step 3:
# null <--> A <--> B <--> C  D <--> null
# Step 4:
# null <--> A <--> B <--> C <--> D <--> null
# Reversed list: D <--> C <--> B <--> A <--> null
# None A B C None

# A.next = None
# A.prev = B

# B.next = C
# B.prev = A

# C.prev = None
# C.next = B
# None C B A None


def solution(node):
    prev_node = None
    current_node = node
    next_node = None
    while current_node is not None:
        next_node = current_node.next  # B
        prev_node = current_node.prev  # None
        current_node.prev = next_node  # B
        current_node.next = prev_node  # None
        prev_node = current_node  # A
        current_node = next_node  # B
    return prev_node


def test():
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1

    node1.prev = node0
    node1.next = node2

    node2.prev = node1
    node2.next = node3

    node3.prev = node2
    new_head = solution(node0)
    assert new_head is node3
    assert node3.next is node2
    assert node2.next is node1
    assert node2.prev is node3
    assert node1.next is node0
    assert node1.prev is node2
    assert node0.prev is node1


if __name__ == '__main__':
    test()