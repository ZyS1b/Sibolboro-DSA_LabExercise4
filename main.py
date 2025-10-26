class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        # insert a node at the beginning
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def insert_at_end(self, data):
        # insert a node at the end
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def search(self, data):
        # search for a node with matching data
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            else:
                current_node = current_node.next
        return False

    def remove_beginning(self):
        # remove the node at the beginning and return its data
        if not self.head:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return removed_data

    def remove_at_end(self):
        # remove the node at the end and return its data
        if not self.head:
            return None
        if self.head == self.tail:
            removed_data = self.head.data
            self.head = None
            self.tail = None
            return removed_data
        current = self.head
        while current.next != self.tail:
            current = current.next
        removed_data = self.tail.data
        current.next = None
        self.tail = current
        return removed_data

    def remove_at(self, data):
        # remove the first node with matching data and return it
        if not self.head:
            return None
        if self.head.data == data:
            return self.remove_beginning()
        current = self.head
        while current.next:
            if current.next.data == data:
                removed_data = current.next.data
                current.next = current.next.next
                if current.next is None:
                    self.tail = current
                return removed_data
            current = current.next
        return None


# sample run
sushi_preparation = LinkedList()
sushi_preparation.insert_at_end("prepare")
sushi_preparation.insert_at_end("roll")
sushi_preparation.insert_at_beginning("assemble")

print(sushi_preparation.remove_beginning())  # assemble
print(sushi_preparation.remove_at_end())     # roll
print(sushi_preparation.remove_at("prepare"))# prepare
print(sushi_preparation.remove_at("mixing")) # None
