# Definition for singly-linked list.
import math
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reversal(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev=None
        curr=head
        while curr:
            new_node=curr.next
            curr.next=prev
            prev=curr
            curr=new_node
        temp=prev
        i=0
        sum=0
        while temp is not None:
            sum+=(2**i)*temp.val
            i+=1
            temp=temp.next
        print(sum)
        return prev
        

        
            
            

            
            



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
    head = create_linked_list([1,0,1])
    sol = Solution()
    new_head = sol.reversal(head)
    # print_linked_list(new_head)
