def cbrt(number):
    iterate(1) # begin iterative sequence with initial approximation of 1

    def absolute(a):
        if (a <= 0): return (-1 * a)
        else: return a
    def approximation (g):
        return (((number / (g*g)) + (2*g))/3)
    def iterate(g):
        newGuess = approximation(g)
    
        changeP = absolute (1 - newGuess / g)
        if (changeP < 0.00000001):
            print(newGuess)
        else: iterate(newGuess)