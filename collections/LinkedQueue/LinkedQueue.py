class Link:
    def __init__(self, elem):
        self.elem = elem
        self.next = None
        self.prev = None

# queue of interconnected links
class LinkedQueue:
    # first & last as nulls
    def __init__(self):
        self.first = None
        self.last = self.first
        self.size = 0
    # if last isnt null, add to end, else add as first
    def enQueue(self, item):
        tmp = Link(item)
        if(self.last != None):
            self.last.next = tmp
        else:
            self.first = tmp
        self.last = tmp
        self.size+=1
    
    # grab elem from first in queue and step first to next link
    def deQueue(self):
        if(self.isEmpty()):
            raise Exception

        tmp = self.first.elem
        self.first = self.first.next

        if(self.first == None):
            self.last = None

        self.size-=1
        return tmp

    # return elem of first in queue
    def front(self):
        if(self.isEmpty()):
            raise Exception

        return self.first.elem
    
    # is the queue empty
    def isEmpty(self):
        return self.size == 0