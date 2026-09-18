class Rectangle:
    def __init__(self,height,width):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side,side)
        self._side = side
   
    @property
    def side(self):
        return self._side

    def __str__(self):
        return f"Square(side={self.side})"
    
