def sqrt(number):
    def absolute(a):
        if (a <= 0): return (-1 * a)
        else: return (a)
        
    def avg(a,b):
        return ((a+b)/2)
    
    def iterate(guess):
        newGuess = avg(guess, number/guess)
        
        changeP = absolute(1 - (newGuess / guess))
        if (changeP < 0.0000001): # arbitrary threshold value
            print (newGuess)
            
        else: iterate(newGuess)

    iterate(1)