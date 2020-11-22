import pytest
from AlgorithmsAndDataStructuresLearning.src.SimpleTree.simple_tree import SimpleTree, SimpleTreeNode

class TestSimpleTree():

    @pytest.fixture(scope='session')
    def tree(self):
        root=SimpleTreeNode('i am root!', None)
        tree=SimpleTree(root)
        leaf1 = SimpleTreeNode('i am leafe1!', None)
        leaf2 = SimpleTreeNode('i am leafe2!', None)
        leaf3 = SimpleTreeNode('i am leafe3!', None)
        leaf4 = SimpleTreeNode('i am leafe4!', None)
        leaf5 = SimpleTreeNode('i am leafe5!', None)
        tree.AddChild(root,leaf1)
        tree.AddChild(root, leaf2)
        tree.AddChild(leaf2,leaf3)
        tree.AddChild(leaf1, leaf4)
        tree.AddChild(leaf4, leaf5)
        return tree, root,leaf2
        # print(tree.Root.Children)
        # for node in tree.Root.Children:
        #     print(node.NodeValue)
        # print(leaf2.Parent.NodeValue)

        # tree.PrintAllNodes()
        # print(tree.GetAllNodes())
        # print('I am leafe wehre are you')
        # print(tree.FindNodesByValue('i am leafe1!'))
        # print(tree.Count())
        # print(tree.LeafCount())
        #
        # tree.DeleteNode(leaf3)
        #
        # tree.PrintAllNodes()
        # print(tree.GetAllNodes())
        #
        # print(tree.FindNodesByValue('i am leafe1!'))
        # print(tree.Count())
        # print(tree.LeafCount())
        #
        # tree2=SimpleTree(root2)
        #
        # print(tree2.GetAllNodes())
        # tree.MoveNode(leaf5,root)
        #
        # tree.PrintAllNodes()


    def test_count_nodes(self, tree):

        tree[0].PrintAllNodes()
        assert tree[0].Count() == 6
    def test_leaf_count(self, tree):
        assert tree[0].LeafCount() == 2
    def test_count_after_move(self, tree):
        leaf6 = SimpleTreeNode('i am leafe6!', None)
        leaf7 = SimpleTreeNode('i am leafe7!', None)
        leaf8 = SimpleTreeNode('i am leafe8!', None)
        tree[0].AddChild(tree[1],leaf6)
        tree[0].AddChild(leaf6,leaf7)
        tree[0].AddChild(leaf6,leaf8)
        tree[0].PrintAllNodes()
        #assert tree[0].Count() == 9

        tree[0].MoveNode(leaf6,tree[2])
        tree[0].PrintAllNodes()
        assert tree[0].Count() == 9
        assert tree[0].LeafCount() == 4

