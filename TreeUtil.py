from collections import deque
from TreeNode import TreeNode


class TreeUtil:
    """树工具类"""
    def get_edge(self, root:TreeNode | None) -> list:
        lrlist = []
        if root is None:
            return lrlist
        if root.left is not None:
            lrlist.append((root.val,root.left.val))
            lrlist += self.get_edge(root.left)
        if root.right is not None:
            lrlist.append((root.val,root.right.val))
            lrlist += self.get_edge(root.right)
        return lrlist
    
    def serialize(self, root:TreeNode | None, flag = None):
        if not root: return "[]"
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                if flag :
                    res.append(node.val)
                else :    
                    res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else: res.append("null")
        if flag :
            return res
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        if data == "[]": return
        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if(i>=len(vals)):return root
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
            if(i>=len(vals)):return root
        return root
    
    def count_nodes(self,root:TreeNode | None) -> int:
        if root is None:
            return 0
        else:
            return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)
        
    def print_tree(self,root:TreeNode | None,flag=None ):
        if root is None:
            print("null")
        else:
            if flag is None:
                print(root.val)
                self.print_tree(root.left)
                self.print_tree(root.right)
                return
            if flag :
                self.print_tree(root.left,flag)
                print(root.val)
                self.print_tree(root.right,flag)
                return
            else :
                self.print_tree(root.left,flag)
                self.print_tree(root.right,flag)
                print(root.val)
                return