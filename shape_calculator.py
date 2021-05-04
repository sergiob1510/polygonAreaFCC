class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    area = self.width * self.height
    return (area)
  
  def get_perimeter(self):
    perimeter = 2 * self.width + 2 * self.height
    return (perimeter)
  
  def get_diagonal(self):
    diagonal = ( self.width ** 2 +  self.height ** 2) ** .5 
    return (diagonal)

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return("Too big for picture.")
    else:
      return( ( ("*" * self.width)+ "\n" ) * self.height)

  def get_amount_inside(self, shape):
    amount_inside = self.get_area() // shape.get_area()
    if amount_inside > 0:
      return (amount_inside)
    else:
      return (0)

  def __str__(self):
    return(("Rectangle(width={0}, height={1})").format(self.width, self.height))

class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side

  def set_side(self, side):
    self.width = side
    self.height = side

  def __str__(self):
    return(("Square(side={0})").format(self.width) )