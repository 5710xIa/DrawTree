from typing import List, Optional

from TreeUtil import TreeUtil 
from TreeNode import TreeNode


class BuildTree:
    def buildTree_recursion(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        a = preorder[0]
        b = inorder.index(a)
        root = TreeNode(a)
        root.left = self.buildTree(preorder[1:b+1],inorder[:b])
        root.right = self.buildTree(preorder[b+1:],inorder[b+1:])
        return root
    
    def buildTree_iteration(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        inorderIndex = 0
        for i in range(1,len(preorder)):
            preorderVal = preorder[i]
            node = stack[-1]
            if node.val != inorder[inorderIndex] :
                node.left = TreeNode(preorderVal)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[inorderIndex]:
                    node = stack.pop()
                    inorderIndex += 1
                node.right = TreeNode(preorderVal)
                stack.append(node.right)
        return root
    
# s = BuildTree()
# preorder = [3, 9, 8, 5, 4, 10, 11, 12, 20, 15, 7]
# inorder = [4, 5, 8, 11, 10, 12, 9, 3, 15, 20, 7]
# t = TreeUtil()

# t.print_tree(s.buildTree_iteration(preorder,inorder))
