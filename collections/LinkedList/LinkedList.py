class Link:
    def __init__(self, elem):
        self.elem = elem
        self.next = None
        self.prev = None

# list of interconnected links
class LinkedList:

    # head: first link in chain; rear: last link in chain
    def __init__(self):
        self.head = Link('head')
        self.rear = self.head
        self.size = 0

    # add a new link with an element to the rear
    def add(self, elem):
        self.rear.next = Link(elem)
        self.rear.next.prev = self.rear
        self.rear = self.rear.next
        self.size+=1

    # remove an element (first occurence) 
    def remove(self, elem):
        trav = self.head.next
        while trav != None:
            if trav.elem == elem:
                trav.prev.next = trav.next
                break
            trav = trav.next

    def contains(self, elem):
        trav = self.head.next
        while trav != None:
            if trav.elem == elem:
                return True
            trav = trav.next
        return False
    # step through links printing their elem
    def print(self):
        # traverse
        trav = self.head.next
        while trav != None:
            print(trav.elem),
            trav = trav.next