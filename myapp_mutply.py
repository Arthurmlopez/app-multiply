def mutiply(num1,num2):
  if is_number(num1) and is_number(num2):
   return float(num1) * float(num2)
  else:
   return None
  
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

