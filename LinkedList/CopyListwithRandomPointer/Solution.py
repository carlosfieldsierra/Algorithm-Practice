class Node:
    pass

class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        # One to One map
        oldToCopy = {None:None}
        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            cur = cur.next 
        
        # Connect pointers
        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]

        return oldToCopy[head]


