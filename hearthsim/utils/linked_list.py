from hearthsim.utils.constants import DEBUG

class LinkedListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

    def __repr__(self):
        return str(self.val)

class LinkedList:
    first = None
    last = None
    size = 0

    def add_node_before(self, target, new_node):
        if target is None:  # is last
            if self.first is None:
                self.first = new_node
            else:
                self.last.next = new_node
                new_node.prev = self.last
            self.last = new_node
        elif self.first == target:  # is first
            new_node.next = self.first
            self.first.prev = new_node
            self.first = new_node
        else:
            new_node.prev = target.prev
            new_node.next = target
            target.prev.next = new_node
            target.prev = new_node
        self.size += 1
        if DEBUG:
            self.check_size()

    def remove_node(self, node):
        if node.prev is None:  # is first
            self.first = node.next
        else:
            node.prev.next = node.next
        if node.next is None:  # is last
            self.last = node.prev
        else:
            node.next.prev = node.prev
        self.size -= 1
        if DEBUG:
            self.check_size()

    def check_size(self):
        node = self.first
        for i in range(self.size):
            node = node.next
        assert node is None

        node = self.last
        for i in range(self.size):
            node = node.prev
        assert node is None

    def __iter__(self):
        node = self.first
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        return ', '.join([str(node) for node in self])