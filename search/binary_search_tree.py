class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, child_data):
        if child_data == self.data:
            return  # exit

        # add data in left subtree
        if child_data < self.data:
            # print(child_data, " go to LEFT SUBTREE of", self.data)

            if self.left:  # if self.left is not None (has Node, has leaf)
                self.left.add_child(child_data)
                # recurse it until self.left is None
            else:  # once/if self.left is None, create node (leaf)
                self.left = BinarySearchTree(child_data)
                # this feature will remove duplicates
                # print(child_data, "become node")

        # add data in right subtree
        else:
            # print(child_data, "go to RIGHT SUBTREE of", self.data)
            if self.right:  # if self.left is not None (has Node, has leaf)
                self.right.add_child(child_data)  # recursively
            else:
                self.right = BinarySearchTree(child_data)
                # print(child_data, "become node")

    def in_order_traversal(self):
        """
        This is DFS Algorithms implementation

        """
        elements = []

        # visit left subtree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit root
        elements.append(self.data)

        # visit right subtree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        """
        This is DFS Algorithms implementation

        """
        elements = []

        # visit left subtree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit right subtree
        if self.right:
            elements += self.right.in_order_traversal()

        # visit root
        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        """
        This is DFS Algorithms implementation

        """
        elements = []

        # visit root
        elements.append(self.data)

        # visit left subtree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit right subtree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        # base case
        if self.data == val:
            return True

        print(self.data)
        if val < self.data:  # if valtofind is less than the node, go to left
            # value might be in left subtree
            # sprint(f"Find {val} on LEFT SUBTREE of {self.data}")

            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:  # if valtofind is bigger than the node, go to right
            # value might be in right subtee
            # print(f"Find {val} on RIGHT SUBTREE of {self.data}")

            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()  # recursively going to to the left
        # the next left will be the self and continue till the last node

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def calculate_sum(self):
        """
        How recursion works here:

        ```
        For the particular node:
            - check if left leaf is not None:
                call recursively calculate_sum()
                    - which always "return" the [self.data] + None (left) + None(none)
                    - and "update" left_node_val value from 0 (when it started)
            - check if right leaf is not None:
                call recursively calculate_sum()
                    - which always "return" the [self.data] + None (right) + None(none)
                    - and "update" right_node_val value from 0 (when it started)
        ```

        - The quotation marks is used to bold the action that has been taken
        when the calculate_sum() is called recursively.

        """
        if self.left:
            left_node_val = self.left.calculate_sum()
        else:
            left_node_val = 0

        if self.right:
            right_node_val = self.right.calculate_sum()

        else:
            right_node_val = 0

        total = self.data + left_node_val + right_node_val  # action done for recursion
        print("Node", self.data)
        print(" |- LEFT", left_node_val)
        print(" |- RIGHT", right_node_val)
        print(
            "TOTAL NOW",
            f"{self.data} + {left_node_val} + {right_node_val} = {total}\n",
        )
        return total

    def delete(self, val, del_right=True):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)  # this is recursively call method

        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)  # this is recursively call method

        else:  # val == self.data
            if self.left is None and self.right is None:  # last leaf
                return None

            # if only 1 child
            if self.left is None:
                return self.right

            if self.right is None:
                return self.right

            # DELETION (method 1)
            if del_right:
                min_val = self.right.find_min()
                self.data = min_val
                self.right = self.right.delete(min_val)
            # DELETION (method 2)
            else:
                max_val = self.left.find_max()
                self.data = max_val
                self.left = self.left.delete(max_val)

        return self  # recursive will return this, that is why it can find the next left/right


def build_tree(elements):
    root = BinarySearchTree(elements[0])  # the first elem will be root

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 18, 4, 34]
    numbers_tree = build_tree(numbers)
    # print(numbers_tree.in_order_traversal())
    # print(numbers_tree.post_order_traversal())
    # print(numbers_tree.pre_order_traversal())

    # return ascending order and removing duplicate (like set)
    # print(numbers_tree.search(18))
    # print(numbers_tree.find_min())
    # print(numbers_tree.find_max())
    # print(numbers_tree.calculate_sum())
    numbers_tree.delete(34)
    numbers_tree.delete(20, del_right=False)
    print(numbers_tree.in_order_traversal())
