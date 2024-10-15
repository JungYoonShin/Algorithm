class ListNode(object):
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory(object):
    def __init__(self, homepage):
        new_node = ListNode(homepage)
        self.current = new_node

    def visit(self, url):
        self.current.next = ListNode(val=url, prev=self.current)
        self.current = self.current.next
        return None

    def back(self, steps):
        for _ in range(steps):
            if self.current.prev is None:
                break
            self.current = self.current.prev
        return self.current.val

    def forward(self, steps):
        for _ in range(steps):
            if self.current.next is None:
                break
            self.current = self.current.next
        return self.current.val
