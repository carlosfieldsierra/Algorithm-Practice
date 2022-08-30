
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


def makeLinkedList(arr):
    

    head = Node(arr[0])
    curr = head
    for i in range(1,len(arr)):
        node = Node(arr[i])
        curr.next = node
        curr = node


    return head 

def isPalindrome(head):
    # rev records the first half, need to set the same structure as fast, slow, hence later we have rev.next
    rev = None
    # initially slow and fast are the same, starting from head
    slow = fast = head
    while fast and fast.next:
        # fast traverses faster and moves to the end of the list if the length is odd
        fast = fast.next.next
        
        # take it as a tuple being assigned (rev, rev.next, slow) = (slow, rev, slow.next), hence the re-assignment of slow would not affect rev (rev = slow)
        rev, rev.next, slow = slow, rev, slow.next
        
        print(f"slow",slow)
        print(f"fast",fast)
        print(f"rev",rev)
        print("-"*10)

    if fast:
       # fast is at the end, move slow one step further for comparison(cross middle one)
        slow = slow.next
    # compare the reversed first half with the second half
    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next
    
    # if equivalent then rev become None, return True; otherwise return False 
    return not rev




def Main():
    head = makeLinkedList([1,2,3])
    print(head)
    print("\n======\n")
    isPalindrome(head)
    

if __name__ == "__main__":
    Main()