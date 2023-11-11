# https://dimikoj.com/problems/4/divisor

def divisors(num):
    num = int(num)
    divs = []

    if num == 0:
        return [0]

    if num == 1:
        return [1]
    
    for i in range(1, num//2 +1):
        if not num%i:
            divs.append(i)

    divs.append(num)


    return divs


for T in range(int(input())):
    s = " ".join(map(str, divisors(input())))
    print(f"Case {T+1}: {s}")
    