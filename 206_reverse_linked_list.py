def reverse_list(head):
    if not head or not head.next:
        return head

    pre = head
    curr = head.next

    while curr:
        post = curr.next
        curr.next = pre

        pre = curr
        curr = post

    head.next = None
    return pre
