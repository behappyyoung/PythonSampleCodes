"""

Given a singly linked list, determine if its a palindrome.
Return 1 or 0 denoting if its a palindrome or not, respectively.


List 1-->2-->1 is a palindrome.
List 1-->2-->3 is not a palindrome.

Expected solution is linear in time and constant in space

isPalindrome => extra space / too slow

isPalindrome_s => two pointer / without extra space - just S(1)

"""

def isPalindrome_s(head_node):
    c_node = head_node
    if c_node.next is None:
        return True
    fast_node = c_node.next.next
    while fast_node and fast_node.next:
        fast_node = fast_node.next.next
        next_node = c_node.next
        c_node.next = next_node.next
        next_node.next = head_node
        head_node = next_node

    c_node = c_node.next
    if fast_node: # odd number
        head_node = head_node.next

    while c_node:
        if c_node.val == head_node.val:
            c_node = c_node.next
            head_node = head_node.next
        else:
            return False
    return True


def isPalindrome(head_node):
    c_node = head_node
    node_length = 0
    while c_node is not None:
        node_length += 1
        c_node = c_node.next

    c_node = head_node
    arr = []
    for i in range(0, node_length//2):
        arr.append(c_node.val)
        c_node = c_node.next

    if node_length % 2 != 0:
        c_node = c_node.next

    for i in range(0, node_length//2):
        c_arr = arr.pop()
        print(c_arr, c_node.val)
        if c_arr != c_node.val:
            return 0
        c_node = c_node.next

    return 1


#test
from _LinkedLists import ListNode, print_node

# lnode = ListNode('a')
# lnode.next = ListNode('b')
# lnode.next.next = ListNode('b')
# lnode.next.next.next = ListNode('a')
#
# print(palindrome_list_str(lnode))
#
# # A : [ 1 -> 2 -> 1 ]
# lnode = ListNode('1')
# lnode.next = ListNode('2')
# lnode.next.next = ListNode('1')
# lnode.next.next.next = ListNode('2')
# lnode.next.next.next.next = ListNode('1')
# print(isPalindrome_s(lnode))
#
# lnode = ListNode('10')
# lnode.next = ListNode('7')
# lnode.next.next = ListNode('10')


lnode = ListNode('1')
lnode.next = ListNode('1000000000')
lnode.next.next = ListNode('-1000000000')
lnode.next.next.next = ListNode('-1000000000')
lnode.next.next.next.next = ListNode('1000000000')
lnode.next.next.next.next.next = ListNode('1')

print_node(lnode)
print(isPalindrome(lnode))
print(isPalindrome_s(lnode))