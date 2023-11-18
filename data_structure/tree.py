"""
TREE Algorithm
- using node
"""
from typing import Union


class TreeNode:
    def __init__(self, data):
        self.data = data  # original answer clue: divide `data` into 2 instance attr: name, designation
        self.children = []
        self.parent = None

    def add_child(self, child: object):
        """
        NOTE
        - Be clear that child is a node which has `None` as parent by default.
        - Then, explicitly, this method will tell the child that, "I" (the instance)
        is your parents.
        - For root, because no one added it as child, hence the parent is None.
        - For ancestor, because root instances added it as child, the parent
        become root (self, or itself).
        - For leaf, because ancestor instances added it as child, the parent
        become ancestor (self, or itself)

        Example:
        >>> Wolf = TreeNode("Wolf")
        >>> Dog = TreeNode("Dog")
        >>> Wolf.add_child(Dog)

        - Here Wolf - as instance has add_child method.
        - When Wolf `added_child`, the default value of the Dog will change to
        `self` that refer to the Wolf as instance.
        - Hence Wolf become the parent of the Dog.

        """
        child.parent = self  # NOTE: NOT CLEAR WHAT HAPPENED HERE
        # parent become object (self) ?
        self.children.append(child)

    def get_level(self):
        """
        - Get the level of particular node.
        - `while p` will implicitly checked whether the p is None or not.
        - if p is None, it iteration is exited.
        - if p is not None (an Object), iteration is executed.
            - As iteration execute, level will be incremented by 1.
            - And; - parent will be updated with the Node parent (that has been allocated for particular memory)
            - Iteration continued,
        """
        level = 0
        p = self.parent
        # print(level, p)
        while p:  # while p is not None, as p is None it wil not be iterated
            """
            - for root, level - 1, self.parent - None
            -
            """
            level += 1
            p = p.parent
        # print("break", p, level)
        return level

    def print_tree(self, show_info: Union[str, bool] = False, level: int = False):
        if self.get_level() > level:
            return
            # NOTE: level become the limiter, if get_level() is bigger than level,
            # continue, else it will exit the code withput running the next line.
            # simply - an exit line.

        # if show_info == "name":
        #     self.data = self.data[: self.data.find("(")]
        # elif show_info == "designation":
        #     self.data = self.data[self.data.find("(") :]
        # elif show_info == "both":
        #     self.data = self.data

        space = " " * self.get_level() * 3
        if self.get_level() == 0:
            print("|-", self.data)
        else:
            print(space + "|-", self.data)  # recursed this

        if self.children:
            for child in self.children:
                child.print_tree(show_info, level)  # recursion


def build_product_tree():
    # root = TreeNode("Electronics")

    # laptop = TreeNode("Laptop")
    # laptop.add_child(TreeNode("Mac"))
    # laptop.add_child(TreeNode("HP"))
    # laptop.add_child(TreeNode("Acer"))

    # phone = TreeNode("Smartphone")
    # phone.add_child(TreeNode("Samsung"))
    # phone.add_child(TreeNode("Xiomi"))
    # phone.add_child(TreeNode("Iphone"))
    # root.add_child(laptop)
    # root.add_child(phone)

    ceo = TreeNode("Jacky (CEO)")
    cto = TreeNode("Micky (CTO)")
    infra = TreeNode("Vishwa (Infrastructure Head)")

    infra.add_child(TreeNode("Jarjit (App Manager)"))
    infra.add_child(TreeNode("Meimei (App Head)"))

    ceo.add_child(cto)
    ceo.add_child(infra)

    return ceo


def build_country_tree():
    global_root = TreeNode("Global")
    india = TreeNode("India")
    gujarat = TreeNode("Gujarat")
    karnataka = TreeNode("Karnataka")
    india.add_child(gujarat)
    india.add_child(karnataka)
    gujarat.add_child(child=TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))
    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))

    usa = TreeNode("USA")
    new_j = TreeNode("New Jersey")
    calf = TreeNode("California")
    usa.add_child(new_j)
    usa.add_child(calf)
    new_j.add_child(TreeNode("Princeton"))
    new_j.add_child(TreeNode("Trenton"))
    calf.add_child(TreeNode("San Francisco"))
    calf.add_child(TreeNode("Mountain View"))
    calf.add_child(TreeNode("Palo Alto"))

    global_root.add_child(india)
    global_root.add_child(usa)

    return global_root


# EXERISCE


if __name__ == "__main__":
    # Q 1
    # root = build_product_tree()
    # print(root.get_level())
    # root.print_tree(show_info="name")
    # root.print_tree(show_info="designation")
    # root.print_tree(show_info="both")

    # Q 2
    country = build_country_tree()
    country.print_tree(level=1)

    pass
