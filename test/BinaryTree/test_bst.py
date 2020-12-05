import pytest
from src.BinaryTree.BST import BSTNode, BST

class TestBSTTree():
    def test_search_tree(self):
        root_node = BSTNode('Russia', 10)
        new_tree = BST(root_node)
        new_tree.AddKeyValue('London', 123)
