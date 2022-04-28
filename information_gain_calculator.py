import math
from fractions import Fraction

def log2_calculator(value):
    # math.log(target, base)
    output = math.log(value, 2)
    return output

def target_entropy():
    x = float(Fraction(input("Input 1st value: ")))
    y = float(Fraction(input("Input 2nd value: ")))
    a = log2_calculator(x)
    b = log2_calculator(y)
    result = -(x*a)-(y*b)
    return result

def entropy_branch():
    p = int(input("Input number of possibilities: "))

    previous_output = 0
    counter = 0
    while (counter < p):
        x = float(Fraction(input("Input possibility fraction: ")))
        y = target_entropy()
        current_output = x*y
        following_output = previous_output + current_output
        previous_output = following_output
        counter = counter + 1
    return following_output

def information_gain():
    gain = target_entropy() - entropy_branch()
    return gain

def main():
    print(information_gain())

if __name__ == "__main__":
    main()