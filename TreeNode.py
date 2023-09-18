from typing import Optional


class TreeNode:
    """树节点类"""
    def __init__(self, val: int):
        self.val: int = val                    # 节点值
        self.left: Optional[TreeNode] = None   # 左子节点引用
        self.right: Optional[TreeNode] = None  # 右子节点引用