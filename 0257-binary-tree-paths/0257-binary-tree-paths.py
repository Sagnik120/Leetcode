# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        path = []

        def dfs(node):
            if not node:
                return

            path.append(str(node.val))

            # Leaf node
            if not node.left and not node.right:
                ans.append("->".join(path))
            else:
                dfs(node.left)
                dfs(node.right)

            path.pop()   # Backtrack

        dfs(root)
        return ans