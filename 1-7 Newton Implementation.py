# - - utility functions - - 

# absolute value
def absolute(number):
  if (number <= 0): return (-1 * number)
  else: return (number)

# average
def avg(a, b):
  return ((a+b)/2)

# - - main methods - - 
def sqrt(number):
  iterate(1,number) # begin iterative sequence immediately

def iterate(guess, number):
  newGuess = avg(guess, number / guess) # Newton's method

  # if guess is changing only a small amount, high confidence, give that guess
  changePercentile = absolute(1 - newGuess / guess)
  if (changePercentile < 0.000001): 
    print(newGuess, changePercentile)

  # otherwise, iterate again
  else: iterate(newGuess, number)
