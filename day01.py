import random

def is_even(n)->bool:
    """
    짝수 판정 함수
    """

# 어떤수와 1을 and operation을 하면 어떤 수가 홀수일 경우 뒤에 1만 남고, 어떤 수가 짝수일 경우 0만 나온다
    return not n & 1
def factorial(number) -> int:
    result = 1
    for i in range(1, number+1):
        result = result * i
    return result
def nCr(n, r) -> int:
    '''
    조합 함수
    :param n:
    :param r:
    :return:
    '''
    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)
    return int(numerator / denominator)
def dec_oct_recursion(n):
    if n == 0:
        return ""
    else:
        return dec_oct_recursion(n // 8) + str(n%8)
def dec_oct_repetition(n):
    if n == 0:
        return ""
    else:
        numList = []
        result = ""
        while(True):
            numList.append(n%8)
            if(n // 8 == 0):
                break
            n  = n // 8
        for i in range(len(numList)-1, -1, -1):
            result = result + str(numList[i])

        return result
def totalAdd(n):
    result = 0
    if n == 0:
        return 0
    for i in range(1,n+1):
        result += i
    return result
def guess_number():
    answer = random.randint(1, 100)
    chance = 7

    while chance != 0:
        guess = int(input("Input guess number : "))
        if guess == answer:
            print(f'You win. Answer is {answer}')
            break
        elif guess > answer:
            chance = chance - 1
            print(f'{guess} is bigger. Chance left : {chance}')
        else:
            chance = chance - 1
            print(f'{guess} is lower. Chance left : {chance}')
    else:
        print(f'You lost. Answer is {answer}')
def print_poly(f_x,t_x) -> str:
    poly_expression = "f(x) = "

    for i in range(len(f_x)):
        coefficient = f_x[i]
        term = t_x[i]

        if coefficient >= 0 and i != 0:
            poly_expression = poly_expression + "+"
        poly_expression = poly_expression + f'{coefficient}x^{term} '

    return poly_expression
def calculation_poly(x_value, f_x, t_x) -> int:
    return_value = 0

    for i in range(len(f_x)):
        coefficient = f_x[i]
        return_value += coefficient * pow(x_value, t_x[i])

    return return_value

fibo_memo = [0,1]
def fibonacci_recursion(n)->int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif len(fibo_memo) > n:
        return fibo_memo[n]
    else:
        fibo_memo.append(fibonacci_recursion(n-2) + fibonacci_recursion(n-1))
        return fibonacci_recursion(n-2) + fibonacci_recursion(n-1)

if __name__ == "__main__":
    {
        # n = int(input("Input n : "))
        # r = int(input("Input r : "))
        # print(f"{n}C{r} = {nCr(n, r)}")

        # print(dec_oct_repetition(400))

        # n = int(input("Input n : "))
        # print(totalAdd(n)) # 시간복잡도 : n
        # print(n*(n+1) // 2) # 시간복잡도 : 1
    }
    {
        # fx = [2, 5, -9, 11]
        # tx = [20, 7, 2, 0]
        # print(print_poly(fx,tx))
        # print(calculation_poly(int(input("x 값 : ")), fx,tx))
    }

    print(fibonacci_recursion(7))
#========================================================================================================================