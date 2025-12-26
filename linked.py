# Definition for singly-linked list.
class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        trav = head
        while trav.next is not None:
            first = trav
            second = trav.next
            n = min(first.val, second.val)
            gcd = 0
            for i in range(1, n + 1):
                if (first.val % i) == 0 and (second.val % i) == 0:
                    gcd = i
            gcdNode = ListNode(gcd)
            first.next = gcdNode
            gcdNode.next = second
            trav = second
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
    head = create_linked_list([18, 6, 10, 3])
    sol = Solution()
    new_head = sol.insertGreatestCommonDivisors(head)
    print_linked_list(new_head)
