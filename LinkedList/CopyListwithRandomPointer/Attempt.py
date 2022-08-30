class Node:
    pass

class Solution:
    def copyRandomList(self, head):
        if not head: 
            return None

        hashMap = {None:None}
        dummy = Node(0)
        tail = dummy
        curr = head
        while curr:
            tail.next = Node(curr.val)
            tail = tail.next 
            hashMap[curr] = tail
            curr = curr.next


        currOne = head
        currTwo = dummy.next

        while currOne and currTwo:
            randomNode = hashMap[currOne.random]
            currTwo.random = randomNode

        return dummy.next 