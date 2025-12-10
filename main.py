"""
HW04 — Forest Watchtower (Balanced Tree Check)

Implement TreeNode and is_balanced(root) to check if a binary tree is height-balanced.
"""

class TreeNode:
    """
    Simple binary tree node: value, left, right.
    """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_balanced(root):
    """
    Return True if the binary tree rooted at `root` is height-balanced.
    Empty tree is balanced.
    """

    def check(node):
        # returns (is_balanced, height)
        if node is None:
            return True, 0

        left_bal, left_h = check(node.left)
        if not left_bal:
            return False, 0

        right_bal, right_h = check(node.right)
        if not right_bal:
            return False, 0

        # balance condition
        if abs(left_h - right_h) > 1:
            return False, 0

        # height of current node
        return True, 1 + max(left_h, right_h)

    balanced, _ = check(root)
    return balanced
