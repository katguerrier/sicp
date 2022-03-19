# recursive factorial process
# The recursive factorial process is intuitive but computationally more intensive and will hit against recursion depth limits.
def recFactorial(n):
    if (n > 1):
      return (n * factorial(n-1))
    else:
        return 1
    
# iterative factorial process
# The iterative factorial process has only the product, counter, and endpoint to keep in memory at any given time. 
def iterFactorial(n):
    product = 1
    for c in range(1,n+1):
        product *= c
    return product