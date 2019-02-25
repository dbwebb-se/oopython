from node import Node
from errors import ValueTooBigError
class UnorderedList:
    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0
    
    def add(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
            # current = self.head
            # while current.next is not None:
            #     current = current.next
            # current.next = node
        self.size += 1

    def get(self, index):
        if index >= self.size:
            raise ValueTooBigError("index is to big for list: " + str(index))
        elif index < 0:
            raise IndexError("Index too small")
        if self.head is None:
            return False
        else:
            current = self.head
            counter = 0
            while counter < index:
                current = current.next
                counter += 1
            return current.data

if __name__ == "__main__":
    l = UnorderedList()
    l.add(5)
    l.add(7)
    l.add(2)
    l.add(8)# 3
    l.add(3)
    if 6 < l.size:
        print(l.get(6))
    else:
        print("Went wrong")

    try:
        print(l.get(-1))
    except ValueTooBigError as e:
        print(e)
    except IndexError as e:
        print(e)
    else:
    finally:
        
