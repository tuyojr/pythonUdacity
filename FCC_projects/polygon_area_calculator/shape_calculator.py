class Rectangle:

    # this method initializes width and height when the rectangle object is created
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # this method sets a new width
    def set_width(self, new_width):
        self.width = new_width
      
    # this method sets a new height
    def set_height(self, new_height):
        self.height = new_height

    # this method calculate the area of the rectangle
    def get_area(self):
        area = self.width * self.height
        return area

    # this method calculates the perimeter of the rectangle
    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    # this method calculates the diagonal of the rectangle
    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return diagonal

    # this method checks if width or height is larger than 50
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        line_width = '*' * self.width + '\n'
        picture = line_width * self.height

        return picture

    # this method checks how many times a shape can fit into the rectangle
    def get_amount_inside(self, figure):
        height_space = self.height // figure.height
        width_space = self.width // figure.width

        inside_space = height_space * width_space
        return inside_space

    # this is a method that returns a string expression of the rectangle width and height
    def __repr__(self):
        string = "Rectangle(width={}, height={})".format(self.width, self.height)
        return string

# Square class which is a subclass of Rectangle
class Square(Rectangle):

    # this method initializes length of the sides when the square object is created
    def __init__(self, side):
        self.width = side
        self.height = side

    # this method can be used to set the new length of the side
    def set_side(self, side):
        self.width = side
        self.height = side

    # this is a method that returns a string expression of the square sides
    def __repr__(self):
        string = "Square(side={})".format(self.width)
        return string