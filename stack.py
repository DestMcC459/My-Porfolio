"""
Python Data Structures - A Game-Based Approach
Stack class
Robin Andrews - https://compucademy.net/
"""





class Stack:
    def __init__ (self):
        self.items = []
    def is_empty():
        return not self.items
    def push(self, item): 
        self.items.append()
    def pop(self):
        return self.items.pop()
    def peek(self): 
        return self[-1]
    def size(self):
        return len(self.items)
    def __str__(self): 
        return str(self.items)

if __name__ == "__main__": 