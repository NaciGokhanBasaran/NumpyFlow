

class math_funcs:
  def sqrt(x):
        """
        x**1 =x
        x**0.5 = sqrt(x)

        """
      
      return x**0.5


  def absolute_value(x):
    """
    suppose x = 1
    then the absolute value is equal to 1 
    if x value is 0 or lower than 0  multiply x by -1 
    because -x * -z = +xz
    """
    
    if x > 0:
      return x
    else:
      return x*-1
