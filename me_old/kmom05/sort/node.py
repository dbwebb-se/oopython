# class Node():
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#     
# class UnorderedList():
#     def __init__(self):
#         self.head = None
#     
#     def lp(self):
#         current = self.head
#         while current != None:
#             print(current.data)
#             current = current.next
#     
#     def append(self, data):
#         new_node = Node(data)
#         current = self.head
#         if current is not None:
#             while current.next != None:
#                 current = current.next
#             current.next = new_node
#         else:
#             self.head = new_node
#     def remove(self, index):
#         current = self.head
#         previous = None
#         count = 0
#         while current is not None:
#             if count == index:
#                 if previous is not None:
#                     previous.next = current.next
#                     del current 
#                 else:
#                     self.head = current.next
#                 return True
# 
#             previous = current
#             current = current.next
#             count += 1
#         raise ValueTooBigError
# 
# class ValueTooBigError(Exception):
#     """ User-defined custom exception for index error"""
#     pass
# ul = UnorderedList()
# # ul.remove(1)
# ul.append(5)
# ul.remove(0)
# ul.append(7)
# ul.append(1)
# ul.remove(1)
# ul.lp()
class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value


c = Celsius(3)
print(c.to_fahrenheit())
c.temperature = 5
print(c.temperature)
