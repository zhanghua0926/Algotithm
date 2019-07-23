

class TreeNode:
    # 初始化，data,left,right都为TreeNode类型
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # 层次遍历
    def levelTraversing(self):
        queue = [self]
        l = []

        while queue:
            current = queue.pop(0)
            l.append(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return l

    # 分层打印
    def printLevel(self):
        currentLevel = [self]
        val = []

        while currentLevel:
            val.append([c.data for c in currentLevel])
            nextLevel = []
            for i in currentLevel:
                if i.left:
                    nextLevel.append(i.left)
                if i.right:
                    nextLevel.append(i.right)
            
            currentLevel = nextLevel
        
        return val

    def __str__(self):
        string = self.printLevel()
        return '%s'%string



#Tree结构               0
#                 1           2
#              3    4      5     6
#             7 8  9 10  11 12 13 14
tree = TreeNode(0,
            TreeNode(1,
                TreeNode(3,
                    TreeNode(7),
                    TreeNode(8)),
                TreeNode(4,
                    TreeNode(9),
                    TreeNode(10))),
            TreeNode(2,
                TreeNode(5,
                    TreeNode(11),
                    TreeNode(12)),
                TreeNode(6,
                    TreeNode(13),
                    TreeNode(14)))
)


#Tree2结构              0
#                   1      2
#                 3      5   6
#                7 8   11 12
tree2 = TreeNode(0,
            TreeNode(1,
                TreeNode(3,
                    TreeNode(7),
                    TreeNode(8))),
            TreeNode(2,
                TreeNode(5,
                    TreeNode(11),
                    TreeNode(12)),
                TreeNode(6))
)

print(tree)
print(tree2)
