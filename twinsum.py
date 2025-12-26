# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        temp=head.next
        prev=head
        adv=head.next.next
        cric=[]
        node=2
        while temp.next is not None:
            if((temp.val>prev.val and temp.val>adv.val) or (temp.val<prev.val and temp.val<adv.val) ):
                cric.append(node)
                
            node+=1
            prev=temp
            temp=adv
            adv=adv.next
        if len(cric)<2:
            return [-1,-1]
       
        else:
            dist=list(cric)
            min1=min(dist)
            min2=max(dist)
            maxDistance=abs(min2-min1)
            print(cric)

            # minDistance=abs(cric[1]-cric[0])
            # for i in range(1,len(cric)-1):
            #     for j in range(i+1,len(cric)):
            #         if(abs(cric[i]-cric[j])<minDistance):
            #             minDistance=abs(cric[i]-cric[j])
            minDistance=cric[len(cric)//2]-cric[(len(cric)//2)-1]

        return [minDistance,maxDistance]
        


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
    head = create_linked_list([5,3,1,2,5,1,2])
    sol = Solution()
    new_head = sol.pairSum(head)
    # print_linked_list(new_head)
    print(new_head)


    



        