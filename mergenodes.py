# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp=head.next
        sum=0
        newlist=[]
        while temp is not None:
            if(temp.val != 0):
                sum+=temp.val
            if(temp.val == 0):
                newlist.append(sum)
                sum=0
            temp=temp.next
        head=ListNode(newlist[0])
        curr=head
        for value in newlist[1:]:
            curr.next=ListNode(value)
            curr=curr.next
        return head
            
            

            
            



# ---------- Example Test (you can modify this for your own input) ----------

# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

# Helper function to print linked list
def print_linked_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)


# Example usage
if __name__ == "__main__":
    head = create_linked_list([0,3,1,0,4,5,2,0])
    sol = Solution()
    new_head = sol.mergeNodes(head)
    print_linked_list(new_head)
