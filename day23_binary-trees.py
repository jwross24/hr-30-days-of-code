# A level-order traversal, also known as a breadth-first search, visits each
# level of a tree's nodes from left to right, top to bottom. You are given a
# pointer, root, pointing to the root of a binary search tree. Complete the
# levelOrder function provided in your editor so that it prints the level-
# order traversal of the binary search tree.


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, root):
        # Write your code here
        output = []
        queue = []
        if root is not None:
            # Enqueue current root
            queue.insert(0, root)

        # While there are nodes to process
        while len(queue) != 0:
            # Dequeue next node
            node = queue.pop()
            output.append(str(node.data))
            # Enqueue child elements from next level in order
            if node.left is not None:
                queue.insert(0, node.left)
            if node.right is not None:
                queue.insert(0, node.right)

        print(' '.join(output))


# Input handler
T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)
