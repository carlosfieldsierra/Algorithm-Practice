class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

    def __repr__(self):
        ret = ""
        curr = self
        while curr != None:
            ret += f"{curr.val} -> "
            curr = curr.next
        return ret

def make(arr):
    

    head = Node(arr[0])
    curr = head
    for i in range(1,len(arr)):
        node = Node(arr[i])
        curr.next = node
        curr = node


    return head 

def ListNode(val):
    return Node(val)

def mergeTwoLists(list1,list2):
    dummy  = ListNode(None)
    tail = dummy
    while list1 and list2:
        if list1.val  > list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    if list2:
        tail.next = list2

    return None if not tail.next else tail.next


def Main():
    ans = mergeTwoLists(list1 = make([1,2,4]), list2 = make([1,3,4]))
    print(ans)

if __name__ == "__main__":
    Main()
