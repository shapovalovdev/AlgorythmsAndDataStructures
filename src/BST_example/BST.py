class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left =  None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            #add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            #add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        #visit left tree
        if self.left:
            elements += self.left.in_order_traversal()



        # visit base node
        elements.append(self.data)
        # visit right tree

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self,val):
        if self.data == val:
            return True
        if val< self.data:
            #val might be in left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val >self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements


    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        #print(left_sum)
        right_sum = self.right.calculate_sum() if self.right else 0
        #print(right_sum)
        return self.data + left_sum + right_sum

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.right

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [17,4,1,20,9,23,18,34]
    numbers_tree=build_tree(numbers)

    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(18))
    print(numbers_tree.search(21))
    print(numbers_tree.calculate_sum())
    numbers_tree.delete(20)
    print(numbers_tree.pre_order_traversal())