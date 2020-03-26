"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Try solving it using constant additional space.

Input :

                  ______
                 |     |
                 \/    |
        1 -> 2 -> 3 -> 4

Return the node corresponding to node 3.


"""


def detect_cycle(head_node):
    d ={}
    while head_node is not None:
        if head_node in d:
            return head_node
        else:
            d[head_node] = True
        head_node = head_node.next

    return None


# only tell cycle or not
def detect_cycle_pp(head_node):
    slow_node = head_node
    fast_node = head_node.next
    while slow_node != fast_node:
        if slow_node is None or fast_node is None:
            return False
        if fast_node.next is None or fast_node.next.next is None:
            return False
        slow_node = slow_node.next
        fast_node = fast_node.next.next
        print(slow_node.val, fast_node.val)
    return True

#test
from _LinkedLists import ListNode, print_node

lnode = ListNode(1)
cycle_node = ListNode(2)
lnode.next = cycle_node
lnode.next.next = ListNode(4)
lnode.next.next.next = ListNode(5)
lnode.next.next.next.next = cycle_node

# print_node(lnode)
# return_node = detect_cycle(lnode)
# if return_node:
#     print(return_node.val)
print(detect_cycle_pp(lnode))


