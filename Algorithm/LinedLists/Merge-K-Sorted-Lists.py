"""
Merge k sorted linked lists and return it as one sorted list.

For example,
1 -> 10 -> 20
4 -> 11 -> 13
3 -> 8 -> 9

1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20

merge_k_sorted_lists => time limit exceeded

"""

def merge_k_sorted_lists(A):
    if not A:
        return A
    def merge_two(main, sub):
        done = False
        return_node = main
        while sub and not done:
            if not main.next:
                    main.next = sub
                    done = True
            if sub.val < main.next.val:
                    temp = sub
                    sub = sub.next
                    temp.next = main.next
                    main.next = temp

            main = main.next
        return return_node


    return_node = A[0]

    for i in range(1, len(A)):
        if return_node.val < A[i].val:
            return_node = merge_two(return_node, A[i])
        else:
            return_node = merge_two(A[i], return_node)

    return return_node


def merge_k_sorted_lists_s(A):
    if not A:
        return A
    def merge_two(main, sub):
        done = False
        return_node = main
        while sub and not done:
            if not main.next:
                    main.next = sub
                    done = True
            if sub.val < main.next.val:
                    temp = sub
                    sub = sub.next
                    temp.next = main.next
                    main.next = temp

            main = main.next
        return return_node


    l = 0
    r = len(A) - 1
    print(A)
    while r != 0:
        while l < r:
            if A[l].val < A[r].val:
                A[l] = merge_two(A[l], A[r])
            else:
                A[l] = merge_two(A[r], A[l])

            if r - l == 2:
                l = l
                r -= 1
            else:
                l += 1
                r -= 1

        r = l-1
        l = 0

    return A[0]

#test

from _LinkedLists import ListNode, print_node

lnode = ListNode(3)
lnode.next = ListNode(8)
lnode.next.next = ListNode(9)
lnode.next.next.next = ListNode(12)
lnode.next.next.next.next = ListNode(20)

lnode2 = ListNode(1)
lnode2.next = ListNode(4)
lnode2.next.next = ListNode(10)
lnode2.next.next.next = ListNode(30)

lnode3 = ListNode(13)
lnode3.next = ListNode(80)

print_node(lnode)
print_node(lnode2)
print_node(lnode3)

a = [lnode, lnode2, lnode3]

print_node(merge_k_sorted_lists_s(a))


lnode = ListNode(3)
lnode.next = ListNode(8)
lnode.next.next = ListNode(9)
lnode.next.next.next = ListNode(12)
lnode.next.next.next.next = ListNode(30)

lnode2 = ListNode(1)
lnode2.next = ListNode(8)
lnode2.next.next = ListNode(10)
lnode2.next.next.next = ListNode(30)
