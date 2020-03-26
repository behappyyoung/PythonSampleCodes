"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.


"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# print node
def print_node(head_node):
    c_node = head_node
    print_str = ''
    while c_node is not None:
        print_str += '->' + c_node.val
        c_node = c_node.next
    print(print_str)

########################

def reverse_link_list_from_to(head_node, m, n):
    if m == n:
        return head_node


    c_node = head_node

    m_node = head_node
    count = 0
    while count < n:
        count += 1
        print_node(head_node)
        print(m, n, count, m_node.val, c_node.val)
        if m <= count <=n:
            next_node = c_node.next
            if next_node:
                c_node.next = next_node.next
                if m == 1:
                    next_node.next = head_node
                    head_node = next_node
                else:
                    next_node.next = m_node.next
                    m_node.next = next_node
                count +=1
            else:
                c_node.next = None

        else:
            m_node = c_node
            c_node = c_node.next
        print_node(head_node)

    return head_node

#test

lnode = ListNode('1')
lnode.next = ListNode('2')
lnode.next.next = ListNode('3')
lnode.next.next.next = ListNode('4')
lnode.next.next.next.next = ListNode('5')
lnode.next.next.next.next.next = ListNode('6')
# print_node(lnode)
# print_node(reverse_link_list_from_to(lnode, 3, 3))
lnode = ListNode('1')
lnode.next = ListNode('2')
lnode.next.next = ListNode('3')
lnode.next.next.next = ListNode('4')
lnode.next.next.next.next = ListNode('5')
lnode.next.next.next.next.next = ListNode('6')
# print_node(reverse_link_list_from_to(lnode, 3, 4))
lnode = ListNode('1')
lnode.next = ListNode('2')
lnode.next.next = ListNode('3')
lnode.next.next.next = ListNode('4')
lnode.next.next.next.next = ListNode('5')
lnode.next.next.next.next.next = ListNode('6')
# print_node(reverse_link_list_from_to(lnode, 5, 6))
lnode = ListNode('1')
lnode.next = ListNode('2')
lnode.next.next = ListNode('3')
lnode.next.next.next = ListNode('4')
lnode.next.next.next.next = ListNode('5')
lnode.next.next.next.next.next = ListNode('6')
print_node(reverse_link_list_from_to(lnode, 1, 3))