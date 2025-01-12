

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
  def hasCycle(self, head: Optional[ListNode]) -> bool: 
    if head is None or head.next is None:
      return False

    first_node = head
    second_node = head.next
    
    while first_node != second_node:
      if second_node.next is None or second_node.next.next is None:
        return False
      first_node = first_node.next
      second_node = second_node.next.next
    
    return True

solution = Solution()
root = ListNode(3)
root.next = ListNode(2)
root.next.next = ListNode(0)
root.next.next.next= ListNode(-4)
root.next.next.next.next = root.next
print(solution.hasCycle(root))
    