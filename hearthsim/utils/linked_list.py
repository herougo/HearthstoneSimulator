from hearthsim.utils.constants import DEBUG

class LinkedListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

    def __repr__(self):
        return str(self.val)

class LinkedList:
    def __init__(self):
        self._first = None
        self._last = None
        self._size = 0

    def add_node_before(self, target, new_node):
        if target is None:  # is last
            if self._first is None:
                self._first = new_node
            else:
                self._last.next = new_node
                new_node.prev = self._last
            self._last = new_node
        elif self._first == target:  # is first
            new_node.next = self._first
            self._first.prev = new_node
            self._first = new_node
        else:
            new_node.prev = target.prev
            new_node.next = target
            target.prev.next = new_node
            target.prev = new_node
        self._size += 1
        if DEBUG:
            self.check_size()

    def remove_node(self, node):
        if node.prev is None:  # is first
            self._first = node.next
        else:
            node.prev.next = node.next
        if node.next is None:  # is last
            self._last = node.prev
        else:
            node.next.prev = node.prev
        self._size -= 1
        if DEBUG:
            self.check_size()

    def check_size(self):
        node = self._first
        for i in range(self._size):
            node = node.next
        assert node is None

        node = self._last
        for i in range(self._size):
            node = node.prev
        assert node is None

    def __iter__(self):
        node = self._first
        while node is not None:
            yield node
            node = node.next

    def __len__(self):
        return self._size

    def __repr__(self):
        return ', '.join([str(node) for node in self])