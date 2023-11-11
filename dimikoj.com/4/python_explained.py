# https://dimikoj.com/problems/4/divisor

def divisors(num):
    """This function will return the list of divisors of number"""
    num = int(num) # lets convert the num as integer (we usually don't calculate divisors for floats and no way string)
    divs = [1] # since every number is divisible by 1, we'll just keep that

    if num == 0:
        return [] # 0 can't be devised by any number

    if num == 1:
        return [1] # returning it here to make sure the following codes doesn't run to save CPU cycles 
    
    for i in range(2, num//2 +1):
        """
        # Why starting from 2?
        >> Since all numbers (except 0) is divisible by 1, we added that by default in the list and not doing a calculation for that


        # WHY are we taking num//2 + 1?
            we knew from math that any number from 1 to that number should check if its divisible or not

        >> Heres where competitive programming comes.

        Explanation:
        Lets say we are gonna calculate for 6
        we know its 1 2 3 6
        as you can see except for 6, no other divisor got larger then the half of 6

        For a moment, lets think 6 is divisible by 4. Lets do the math, 
        6/4 = 1.5 (which is not a Integer)
        as we go higher we will get close to 1 yet not an integer until we reach 6
        so all the numbers between half of that and that number it self can't be divisible by that number

        So we will only examine for the num upto num//2 (why //, because we need integers)

        """
        if not num%i: # why not testing it with num % i == 0, because if its 0, its false which is a valid condition. if we check it again and again (0==0, also python checks is it True) so we will just use not 0 for condition. if there is a remainder, not will make it False (any number other than 0 is True)
            divs.append(i)

    divs.append(num) # Finally adding the number itself


    """
    # Why are we adding numbers in separate parts like adding the main number after the loop?
    >> its what optimization is. Making a real big algorithm with lots of conditions, lots of checks in it will only make it complex not efficient. So we divide segments of the problems and merge them together

    # Why testing 0 and 1 separately?
    >> like the above, if we just kick them out in the beginning, we won't have to call a range, a for loop, do lots of operations on them (and often break things). Also returning for 1 has another cause. The part below
    """


    return divs


for T in range(int(input())):
    num = input()
    divs = divisors(num) # its a list

    print(f"Case {T+1}:", *divs)

    """
    # WHAT *divs does is it exposes every item of the list to the function
    - ie:
        x = [1,2,3]
        print(*x)
        # --- is same as
        print(1,2,3)
        # --- or
        print(x[0], x[1], x[2])

    this works for list, dict, tuples
    """