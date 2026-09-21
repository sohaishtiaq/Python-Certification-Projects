class Rectangle:
    def __init__(self,width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def set_width(self,new_width):
        self._width = new_width

    def set_height(self,new_height):
        self._height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        image = ''
        for i in range( self.height):
            image += '*' * self.width
            image += '\n' 
        return image

    def get_amount_inside(self,shape):
        fit_width = self.width // shape.width
        fit_height = self.height // shape.height
        return fit_width * fit_height      

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side,side)
        self._side = side
   
    @property
    def side(self):
        return self._width

    def set_side(self, new_side):
        self._width = new_side
        self._height = new_side

    def set_width(self, new_side):
        self.set_side(new_side)

    def set_height(self, new_side):
        self.set_side(new_side)

    def get_picture(self):
        if self.side > 50:
            return 'Too big for picture.'
        image = ''
        for i in range(self.side):
            image += '*' * self.side
            image += '\n' 
        return image

    def __str__(self):
        return f"Square(side={self.side})"
