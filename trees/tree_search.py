# https://contest.yandex.ru/contest/26207/problems/E/

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def solution(root):
    def helper(node, min_val, max_val):
        if node is None:
            return True
        if node.value < min_val or node.value > max_val:
            return False
        return (helper(node.left, min_val, node.value - 1) and
                helper(node.right, node.value + 1, max_val))

    return helper(root, float('-inf'), float('inf'))

def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)
    
    assert solution(node5)
    node2.value = 5
    assert not solution(node5)

if __name__ == '__main__':
    test()
