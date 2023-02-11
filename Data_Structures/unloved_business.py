#https://contest.yandex.ru/contest/23758/problems/C/

# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:  
        def __init__(self, value, next_item=None):  
            self.value = value  
            self.next_item = next_item


def print_linked_list(vertex):
    while vertex:
            print(vertex.value, end=" -> ")
            vertex = vertex.next_item
    print("None")


def get_node_by_index(node, index):
    while index:
            node = node.next_item
            index -= 1
    return node

# 1 - получить предыдущие дело которое стоит перед делом которое надо удалить index - 1
# 2 - получить следующие дело которое стоит после дела которое надо удалить index + 1
# 3 - указать в поле next_item предыдущего дела ссылку на ноду следующего дела
# 4 - обработаем когда подали idx = 0, просто возвращаем слудующие едл


def solution(node, idx):
    # обработаем случай когда надо удалить 0 индекс, то есть заменить голову
    if idx == 0:
        return node.next_item
    # получим предыдущую ноду
    previous_node = get_node_by_index(node, idx-1)
    # получим следующую ноду
    next_node = get_node_by_index(node, idx+1)
    # свяжем их
    previous_node.next_item = next_node
    return node


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    #result is node0 -> node2 -> node3


if __name__ == '__main__':
    test()
