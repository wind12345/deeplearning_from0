import and_function
import nand_function
import or_function

def XOR(x1,x2):
  s1 = nand_function.NAND(x1,x2)
  s2 = or_function.OR(x1,x2)
  y = and_function.AND(s1,s2)
  return y
print(XOR(1,0))
