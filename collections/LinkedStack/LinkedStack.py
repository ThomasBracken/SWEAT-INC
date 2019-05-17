class Link:
    def __init__(self, elem):
        self.elem = elem
        self.next = None
        self.prev = None

class LinkedStack:
    # null stack
    def __init__(self):
        self.head = None
    # add new link to top of stack
    def push(self, item):
        tmp = Link(item)
        tmp.next = self.head
        self.head = tmp
    # grab top of stack elem and remove link
    def pop(self):
        if(self.isEmpty()):
            raise Exception
        
        tmp = self.head.elem
        self.head = self.head.next
        return tmp
    # return top of stack elem
    def top(self):
        if(self.isEmpty()):
            raise Exception
        return self.head.elem
    # head is null once last elem is popped off stack
    def isEmpty(self):
        return self.head == None