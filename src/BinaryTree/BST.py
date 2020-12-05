class BSTNode:

    def __init__(self, key, val):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        #self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


# class BSTFind:  # промежуточный результат поиска
#
#     def __init__(self):
#         self.Node = None  # None если
#         # в дереве вообще нету узлов
#
#         self.NodeHasKey = False  # True если узел найден
#         self.ToLeft = False  # True, если родительскому узлу надо
#         # добавить новый узел левым потомком


class BST:

    def __init__(self, node):
        self.Root = node  # корень дерева, или None

    def _FindNodeByKey(self, node, key):
        # ищем в дереве узел и сопутствующую информацию по ключу
        if node is None:
            return None
        if key < node.NodeKey:
            return self._FindNodeByKey(node.LeftChild, key)
        elif key > node.NodeKey:
            return self._FindNodeByKey(node.RightChild, key)
        else:
            return node.NodeValue

    def FindNodeByKey(self, key):
        return self._FindNodeByKey(self.Root, key)

    def _AddKeyValue(self, node, key, val):
        # добавляем ключ-значение в дерево
        if node is None:
            return BSTNode(key, val)
        if key < node.NodeKey:
            node.LeftChild= self._AddKeyValue(node.LeftChild, key, val)
        elif key > node.NodeKey:
            node.RightChild= self._AddKeyValue(node.RightChild, key, val)
        else:
           #return False # если ключ уже есть
            node.NodeValue = val
        return node

    def AddKeyValue(self, key, val):
        #if self._AddKeyValue(self.Root, key, val):
        self.Root = self._AddKeyValue(self.Root, key, val)


    def delete_min(self):
        '''
        delete minimum key
        '''
        self.Root = self._delete_min(self.Root)

    def _delete_min(self, node):
        if node.LeftChild is None:
            return node.RightChild

        node.LeftChild = self._delete_min(node.LeftChild)
        return node


    def FinMinMax(self, FromNode, FindMax):
        # ищем максимальный/минимальный ключ в поддереве
        # возвращается объект типа BSTNode
        if FindMax:
            if FromNode.RightChild is None:
                return FromNode
            return self.FinMinMax(FromNode.LeftChild, FindMax)
        else:
            if FromNode.LeftChild is None:
                return FromNode
            return self.FinMinMax(FromNode.LeftChild, FindMax)

    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        self.Root = self._DeleteNodeByKey(self.Root, key)

    def _DeleteNodeByKey(self, node, key):
        # удаляем узел по ключу
        if key < node.NodeKey:
            node.LeftChild = self._DeleteNodeByKey(node.LeftChild, key)
        elif key > node.NodeKey:
            node.RightChild = self._DeleteNodeByKey(node.RightChild, key)
        elif key == node.NodeKey:
            if node.RightChild is None:
                return node.LeftChild

            if node.RightChild is None:
                return node.RightChild

            delete_node = node
            node = self.FinMinMax(node.RightChild, False)
            # specify node.left before node.right will cause delete node.left
            node.RightChild = self._delete_min(delete_node.RightChild)
            node.LeftChild = delete_node.LeftChild

        else:
            return False  # если узел не найден

    def _SumOfValues(self, node):
        sum=0
        sum_left=0
        sum_right=0
        if node is None:
            return 0  # количество узлов в дереве
        #print(node)
        sum+=node.NodeValue
        #print(sum)
        if node.RightChild:
            sum_right=self._SumOfValues(node.RightChild)
        if node.LeftChild:
            sum_left=self._SumOfValues(node.LeftChild)
        return sum + sum_left + sum_right

    def SumOfValues(self):
        return self._SumOfValues(self.Root)

    def _Count(self, node):
        sum=0
        sum_left=0
        sum_right=0
        if node is None:
            return 0  # количество узлов в дереве
        #print(node)
        sum+=1
        #print(sum)
        if node.RightChild:
            sum_right=self._Count(node.RightChild)
        if node.LeftChild:
            sum_left=self._Count(node.LeftChild)
        return sum + sum_left + sum_right

    def Count(self):
        return self._Count(self.Root)

if __name__ == '__main__':
    root_node=BSTNode('NewYork', 10)
    print(root_node)
    new_tree=BST(root_node)
    new_tree.AddKeyValue('London',123)
    print(new_tree.SumOfValues())
    new_tree.SumOfValues()
    print(new_tree.Count())
    new_tree.AddKeyValue('Moscow', 142)
    print(new_tree.SumOfValues())
    print(new_tree.Count())