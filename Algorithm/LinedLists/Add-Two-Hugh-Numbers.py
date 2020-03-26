"""

For a = [9876, 5432, 1999] and
b = [1, 8001], the output should be
addTwoHugeNumbers(a, b) = [9876, 5434, 0].

"with linked list"

Explanation: 987654321999 + 18001 = 987654340000.

"""

def addTwoHugeNumbers(a, b):
    if not a:
        return b
    if not b:
        return a

    def reverseList(node):
        c_node = node
        while c_node.next:
            temp = c_node.next
            c_node.next = c_node.next.next
            temp.next = node
            node = temp
        return node

    a_reverse = reverseList(a)
    b_reverse = reverseList(b)
    overflow = 0
    r_node = a_reverse
    while a_reverse and b_reverse:
        c_sum = a_reverse.val + b_reverse.val + overflow
        if c_sum > 9999:
            overflow = 1
            c_sum -= 10000
        else:
            overflow = 0

        a_reverse.val = c_sum
        pre_a = a_reverse
        a_reverse = a_reverse.next
        b_reverse = b_reverse.next


    if b_reverse:
        pre_a.next = b_reverse

    while overflow and a_reverse:
            c_sum = a_reverse.val + overflow
            if c_sum > 9999:
                overflow = 1
                c_sum -= 10000
            else:
                overflow = 0
            a_reverse.val = c_sum
            pre_a = a_reverse
            a_reverse = a_reverse.next

    if overflow:
        pre_a.next = ListNode(1)
    r_reverse = reverseList(r_node)
    return r_reverse

#test
from _LinkedLists import ListNode, print_node

lnode = ListNode(9876)
lnode.next = ListNode(5432)
lnode.next.next = ListNode(1999)


lnode2 = ListNode(1)
lnode2.next = ListNode(8001)
# lnode2.next.next = ListNode()



print_node(lnode)
print_node(lnode2)

print_node(addTwoHugeNumbers(lnode2, lnode))



lnode = ListNode(1)

lnode2 = ListNode(9999)
lnode2.next = ListNode(9999)
lnode2.next.next = ListNode(9999)
lnode2.next.next.next = ListNode(9999)
lnode2.next.next.next.next = ListNode(9999)

print_node(lnode)
print_node(lnode2)

print_node(addTwoHugeNumbers(lnode2, lnode))

lnode = ListNode(1)

lnode2 = ListNode(9998)
lnode2.next = ListNode(9999)
lnode2.next.next = ListNode(9999)
lnode2.next.next.next = ListNode(9999)
lnode2.next.next.next.next = ListNode(9999)

print_node(lnode)
print_node(lnode2)

print_node(addTwoHugeNumbers(lnode2, lnode))