# recursive way of witing factorial
def fact( n ):
    if type(n) == complex:
        raise Exception("Cannot calculate factorial for complex numbers")

    if ( n == 0 ):
        return 1.0
    elif ( n < 0 ):
        raise Exception("Cannot calculate factorial for negative numbers")
    return fact( n - 1)*n;

    #if ( n == 0 ):
    #return 1.0
    #return fact( n - 1)*n;
if __name__ == "__main__":
   for i in range(0, 10+1):
      #print(f"{i}! = {fact(i)}") 
      print("%d! = %g"%(i,fact(i)))
   #print("%d! = %g"%(-5,fact(-5)))
   i = 5 - 4j
   print("%d! = %g"%(i,fact(i)))
