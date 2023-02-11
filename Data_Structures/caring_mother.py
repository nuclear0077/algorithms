# https://contest.yandex.ru/contest/23758/problems/D/

# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item

# бежим в цикле по значениям ноды и проверяем
# есть ли дело == elem return i инкрементим i += 1


def solution(node, elem):
    i = 0
    while node:
        if node.value == elem:
            return i
        node = node.next_item
        i += 1
    return -1


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    idx = solution(node0, "node2")
    assert idx == 2


if __name__ == '__main__':
    test()
