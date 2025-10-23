# Definition for singly-linked list.
import math
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
   def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        original=None
        temp=head
        while temp is not None:
            curr=temp.next
            while curr is not None:
                if(curr.val>temp.val):
                    if(original is None):
                        original=curr
                    else:
                        original.next=curr
                    
                    temp=curr

                    
                    curr=temp.next
                elif(curr.val==temp.val):
                    if(original is None):
                        original=temp
                        original.next=curr
                    else:
                        original.next=curr
                    
                    temp=curr

                    
                    curr=temp.next

                else:
                    curr=curr.next
            temp=temp.next
        return original
        



        
        

        
            
            

            
            



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
    head = create_linked_list([5,2,13,3,8])
    sol = Solution()
    new_head = sol.removenode(head)
    print_linked_list(new_head)
