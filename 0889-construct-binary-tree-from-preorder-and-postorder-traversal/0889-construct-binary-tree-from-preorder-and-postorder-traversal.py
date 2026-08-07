# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        pos = {}
        for i, val in enumerate(postorder):
            pos[val] = i

        def build(preStart, preEnd, postStart, postEnd):

            if preStart > preEnd:
                return None

            root = TreeNode(preorder[preStart])

            if preStart == preEnd:
                return root

            leftRoot = preorder[preStart + 1]
            index = pos[leftRoot]

            leftSize = index - postStart + 1

            root.left = build(
                preStart + 1,
                preStart + leftSize,
                postStart,
                index
            )

            root.right = build(
                preStart + leftSize + 1,
                preEnd,
                index + 1,
                postEnd - 1
            )

            return root

        return build(0, len(preorder) - 1, 0, len(postorder) - 1)