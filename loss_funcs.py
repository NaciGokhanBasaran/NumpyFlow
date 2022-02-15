from math_funcs import absolute_value,sqrt
 
    
class loss_funcs:
        
    

  def ME(y,y_head ,print_value = False):
    
     """
    MEAN ERROR
    y:real value
    y_head:predicted_value

    equalize loss to 0

    for each iteration:

       calculate an error value (y -y_head)
       add error value to loss

    divide 1 by loss
    example:
           y = [1.1,2.2,3.3]
           y_head = [1,2,3]

           error 1 = 0.1
           loss = 0.1

           error 2 = 0.2
           loss = 0.3

           error 3 = 0.3
           loss = 0.6

           result =1/0.6
    """

    if len(y) != len(y_head):
      raise IndexError("The y_head value must be equal to y value")
    else:
      loss = 0
      for i in range(len(y)):
        error =(y[i] -y_head[i]) 
        loss+=error
        i+=1
    if print_value ==True:
        print(loss)
        
    return 1/loss

  def MAE(y,y_head,print_value = False):
    """

    """
    if len(y) != len(y_head):
      raise IndexError("The y_head value must be equal to y value")
    else:
      loss = 0
      for i in range(len(y)):
        error = absolute_value(y[i]-y_head[i])
        loss+=error
        i+=1
      if print_value ==True:
          print(loss)
          
      return 1/loss
    
    
    
  def MSE(y,y_head,print_value = False):
    """
    y:real value
    y_head:predicted_value

    equalize loss to 0

    for each iteration:

       calculate an error value (y - y_head)**2
       add error value to loss

    divide 1 by loss
    
    """
    if len(y) != len(y_head):
      raise IndexError("The y_head value must be equal to y value")
      
      
    else:
      loss = 0
      for i in range(len(y)):
        error =(y[i] - y_head[i])**2
        loss+=error
        i+=1
        
      if print_value ==True:
          print(loss)
          
      return 1/loss

    
    
  def RMSE(y,y_head,print_value = False):
     """
    
    
    """
    if len(y) != len(y_head):
      raise IndexError("The y_head value must be equal to y value")
      
    else:
      
      loss = 0
      for i in range(len(y)):
        error =(y[i] - y_head[i])**2
        loss+=error
        i+=1
        
    if print_value ==True:
        print(loss)
            
    return sqrt(1/loss)
  def MAPE(y,y_head,print_value = False):
    """


    """
    if len(y) != len(y_head):
      raise IndexError("The y_head value must be equal to y value")
      
    else:
      
      loss = 0
      for i in range(len(y)):
        error = absolute_value(((y[i] - y_head[i])/y[i]))
        loss+=error
        i+=1
           
    if print_value ==True:
        print(loss)
            
    return 100/loss
