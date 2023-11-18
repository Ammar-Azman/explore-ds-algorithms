# ------------- LINKED LIST
# There is issue in list that linked list try to solve
# Data stored in Node
# Element has link to memeory that pointed to next element
# Benefit
# - No need to allocate space during iteration
# Insertion (deletion) easera

# ------------- DOUBLE LINKED LIST
# link to next element and link to the previous element
# Due to the double link between element, we can traversed on backward direction


# Jargon
# - traversed
class Jajaja:
    def __init__(self, kurkur=None, kakaka=None):
        self.kurkur = kurkur
        self.kakaka = kakaka


class Node:
    def __init__(self, data=None, next=None):
        self.data = data  # int, str
        self.next = next  # pointer to the next element # referece to suceeding node


class LinkedList:
    def __init__(self):
        self.head = None  # point to the head of linked list - HEAD - the first node of the linked list

    def insert_at_begining(self, data):
        """
        INSERT AT BEGINNING
        """
        node = Node(data, self.head)
        self.head = node  # head become node which has value
        # NOTE: in linter head has accessed to node through line 37
        #  imagine a growing snake with a head that always move forward and forward

    def insert_at_last(self, data):
        """
        INSERT AT LAST
        """
        if self.head == None:  # if linked list is blank
            self.head = Node(
                data, None
            )  # hence it become the HEAD node (instatiate the Node)
            return

        #  if linked list is not blank
        itr = self.head  #  which means head already instantiate
        while itr.next:  # iterate until it false (last)
            # print("data", itr.data, "pointer", itr.next)
            itr = itr.next

        # when last elem
        itr.next = Node(
            data, None
        )  # the next pointer will become the Node, with None next pointer

    def insert_values(self, data_list):
        # NOTE: Cannot handle if there is no value instatiated (yet)
        # self.head = None # this line will override the previous data
        for data in data_list:
            self.insert_at_last(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception(f"Invalid index: len {self.get_length()}")

        if index == 0:
            self.head == self.head.next  # next one to head become head
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:  # stop before the particular index to do the thing
                itr.next = itr.next.next  # skip on particular index
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        """INSERTING BETWEEN INDEX"""
        if index < 0 or index >= self.get_length():
            raise Exception(f"Invalid index: len {self.get_length()}")

        if index == 0:
            self.insert_at_begining(data)

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)  # sneaking in between
                itr.next = node
                break
            itr = itr.next
            count += 1

    def print(self) -> str:
        if self.head is None:
            print("Linked list is empty")

        itr = self.head  # accessing head
        llstr = ""
        while itr:  # while itr has value (not None)
            llstr += str(itr.data) + "-->"
            # print("data", itr.data, "pointer", itr.next)
            itr = itr.next

        print(llstr)

    # EXERSICE
    def insert_after_value(self, data_to_find, data_to_insert):
        if self.head is None:
            return

        if self.head.data == data_to_find:  # how can head access data is possible
            self.head.next = Node(data_to_insert, self.head)
            return

        itr = self.head
        while itr:
            if itr.data == data_to_find:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head == self.head.next
            return
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(21)
    ll.insert_at_last(79)
    ll.insert_values(["hello", "world"])
    ll.remove_at(3)
    ll.insert_at(1, "Ammar")
    ll.insert_after_value("Ammar", "Safuan")
    ll.remove_by_value("Safuan")
    ll.print()
