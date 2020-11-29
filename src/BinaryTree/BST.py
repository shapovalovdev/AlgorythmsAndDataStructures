"""
Теперь вернёмся к удалению узла с двумя потомками. Проблема в том, что нельзя просто взять и заменить узел одним его потомком, потому что тут возможны конфликтные ситуации, связанные с упорядоченностью ключей. Не будем углубляться в эту ситуацию, воспользуемся следующим правилом: удаляемый узел надо заменить так называемым узлом-преемником, ключ которого -- наименьший из всех ключей, которые больше ключа удаляемого узла.
Иными словами, нам надо взять правого потомка удаляемого узла, и далее спускаться по всем левым потомкам. Если мы находим лист, то его и надо поместить вместо удаляемого узла. Если мы находим узел, у которого есть только правый потомок, то преемником берём этот узел, а вместо него помещаем его правого потомка.

Реализуйте:
- метод поиска (тест: проверяем поиск отсутствующего ключа в двух вариантах (запрошенный ключ добавляем либо левому, либо правому потомку) и поиск присутствующего ключа);
- метод добавления нового узла, задаём добавляемый ключ и соответствующее ему значение (тесты: проверяем исходное отсутствие узла по такому ключу в дереве и его наличие после добавления,
 в двух вариантах -- левым или правым узлом родителя, а также попытку добавления ключа, которое уже имеется в дереве, в таком случае ничего с деревом не делаем);
- поиск максимального и минимального ключей, начиная с заданного узла (тест, 4 варианта: поиск начиная с корня и поиск начиная с поддерева, ищем максимальный и минимальный ключ);
- метод удаления узла по его ключу (тест: проверяем исходное наличие узла у родителя и его отсутствие после удаления).

"""


class BSTNode:

    def __init__(self, key, val, parent):
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

    def AddKeyValue(self, key, val):
        self.Root = self._AddKeyValue(self.Root, key,val)

    def _AddKeyValue(self, node, key, val):
        # добавляем ключ-значение в дерево
        if node is None:
            return BSTNode(key,val)
        if key < node.NodeKey:
            node.LeftChild= self._AddKeyValue(node.LeftChild, key, val)
        elif key > node.NodeKey:
            node.RightChild= self._AddKeyValue(node.RightChild, key, val)
        else:
           node.NodeValue = val
        return False  # если ключ уже есть


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

    def Count(self):
        return 0  # количество узлов в дереве

if __name__ == '__main__':
    BST.Root=BSTNode('Russia', 10, None)