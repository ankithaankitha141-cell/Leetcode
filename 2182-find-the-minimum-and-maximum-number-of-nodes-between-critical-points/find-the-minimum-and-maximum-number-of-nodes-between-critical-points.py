# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        prev = head
        curr = head.next
        index = 1
        
        first_critical = -1
        last_critical = -1
        min_distance = float('inf')
        
        while curr.next:
            # Check if current node is a local maxima or local minima
            is_maxima = prev.val < curr.val and curr.val > curr.next.val
            is_minima = prev.val > curr.val and curr.val < curr.next.val
            
            if is_maxima or is_minima:
                if first_critical == -1:
                    first_critical = index
                else:
                    min_distance = min(min_distance, index - last_critical)
                
                last_critical = index
            
            prev = curr
            curr = curr.next
            index += 1
        
        # If fewer than 2 critical points were found
        if first_critical == -1 or first_critical == last_critical:
            return [-1, -1]
        
        max_distance = last_critical - first_critical
        return [min_distance, max_distance]