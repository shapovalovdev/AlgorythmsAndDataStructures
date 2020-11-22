class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:

    def __init__(self, root):
        self.Root = root  # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        # ваш код добавления нового дочернего узла существующему ParentNode
        NewChild.Parent = ParentNode
        ParentNode.Children.append(NewChild) #добавляем в

    def DeleteNode(self, NodeToDelete):
        if NodeToDelete is self.Root:
            return None

        NodeToDelete.Parent.Children.remove(NodeToDelete)  # ваш код удаления существующего узла NodeToDelete
        NodeToDelete.Children=[]
    def PrintAllNodes(self):

        print(self.Root.NodeValue)

        if self.Root.Children:
            for child in self.Root.Children:
               child_tree=SimpleTree(child)
               child_tree.PrintAllNodes()


    def GetAllNodes(self):
        # ваш код выдачи всех узлов дерева в определённом порядке
        result=set()
        result.add(self.Root)
        if self.Root.Children:
            result.update(self.Root.Children)
            for node in self.Root.Children:
                node_tree=SimpleTree(node)
                result.update(node_tree.GetAllNodes())
        #result.append(self.Root)
        return list(result)


    def FindNodesByValue(self, val):
        # ваш код поиска узлов по значению
        result=[]

        if self.Root.NodeValue == val:
            result.append(self.Root)
        if self.Root.Children:
            for node in self.Root.Children:
                nodetree=SimpleTree(node)
                result.extend(nodetree.FindNodesByValue(val))
        return result

    def MoveNode(self, OriginalNode, NewParent):
        # ваш код перемещения узла вместе с его поддеревом --
        # в качестве дочернего для узла NewParent
        OriginalNode.Parent.Children.remove(OriginalNode)
        OriginalNodeTree=SimpleTree(OriginalNode)
        OriginalNodeTree.Root.Parent=NewParent
        self.AddChild(NewParent,OriginalNode)

    def Count(self):
        # количество всех узлов в дереве
        # ваш код выдачи всех узлов дерева в определённом порядке
        result = 0
        if self.Root:
            result+=1
        if self.Root.Children:
            for node in self.Root.Children:


                node_tree = SimpleTree(node)

                result += node_tree.Count()
        return result


    def LeafCount(self): 
        # количество листьев в дереве
        result = 0
        if self.Root and not self.Root.Children:
            result += 1
        if self.Root.Children:
            for node in self.Root.Children:
                # print(node.NodeValue)
                node_tree = SimpleTree(node)

                result += node_tree.LeafCount()
        return result

# if __name__ == '__main__':
#     root=SimpleTreeNode('i am root!', None)
#     root2 = SimpleTreeNode('i am leafe1!', None)
#     tree=SimpleTree(root)
#     leaf1 = SimpleTreeNode('i am leafe1!', None)
#     leaf2 = SimpleTreeNode('i am leafe1!', None)
#     leaf3 = SimpleTreeNode('i am leafe1!', None)
#     leaf4 = SimpleTreeNode('i am leafe1!', None)
#     leaf5 = SimpleTreeNode('i am leafe1!', None)
#     tree.AddChild(root,leaf1)
#     tree.AddChild(root, leaf2)
#     tree.AddChild(leaf2,leaf3)
#     tree.AddChild(leaf1, leaf4)
#     tree.AddChild(leaf4, leaf5)
#     # print(tree.Root.Children)
#     # for node in tree.Root.Children:
#     #     print(node.NodeValue)
#     # print(leaf2.Parent.NodeValue)
#
#     tree.PrintAllNodes()
#     print(tree.GetAllNodes())
#     print('I am leafe wehre are you')
#     print(tree.FindNodesByValue('i am leafe1!'))
#     print(tree.Count())
#     print(tree.LeafCount())
#
#     tree.DeleteNode(leaf3)
#
#     tree.PrintAllNodes()
#     print(tree.GetAllNodes())
#
#     print(tree.FindNodesByValue('i am leafe1!'))
#     print(tree.Count())
#     print(tree.LeafCount())
#
#     tree2=SimpleTree(root2)
#
#     print(tree2.GetAllNodes())
#     tree.MoveNode(leaf5,root)
#
#     tree.PrintAllNodes()