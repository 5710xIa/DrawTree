import networkx as nx
import matplotlib.pyplot as plt
from TreeNode import TreeNode
from TreeUtil import TreeUtil
from GetTreePos import get_pos

util = TreeUtil()

class DrawTree:

    def draw_tree(self, root:TreeNode | None):
        res = util.serialize(root,True)
        # 创建二叉树
        G = nx.DiGraph()
        i = 1
        for point in res:
            if point == "null": continue
            G.add_node(point)
            i += 1
        G.add_edges_from(util.get_edge(root))
        

        # 绘制二叉树
        # pos可以通过get_pos快速生成
        pos = get_pos(res)
        nx.draw(G,pos,with_labels=True)
        plt.show()