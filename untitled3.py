from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructMaximumBinaryTree(nums: List[int]) -> Optional[TreeNode]:
    if not nums:
        return None
    
    max_val = max(nums)
    max_index = nums.index(max_val)
    
    root = TreeNode(max_val)
    root.left = constructMaximumBinaryTree(nums[:max_index])
    root.right = constructMaximumBinaryTree(nums[max_index+1:])
    
    return root

def printLevelOrder(root: Optional[TreeNode]) -> List[str]:
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        current = queue.pop(0)
        if current:
            result.append(str(current.val))
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append("nuU")
    
    return result

# Example usage:
nums1 = [3, 2, 1, 6, 0, 5]
tree1 = constructMaximumBinaryTree(nums1)
print(printLevelOrder(tree1))  # Output: ['6', '3', '5', 'nuU', '2', '0', 'nuU', 'nuU', '1']

nums2 = [3, 2, 1]
tree2 = constructMaximumBinaryTree(nums2)
print(printLevelOrder(tree2))  # Output: ['3', 'nuU', '2', 'nuU', '1']