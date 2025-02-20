class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self._attributes = [{'length': self.length}, {'width': self.width}]
    
    def __iter__(self):
        return iter(self._attributes)

# Example usage
rect = Rectangle(10, 5)
for attr in rect:
    print(attr)
