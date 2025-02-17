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



if __name__ == "__main__":
    # n = int(input("Input n : "))
    # r = int(input("Input r : "))
    # print(f"{n}C{r} = {nCr(n, r)}")
    print(dec_oct_repetition(400))

#========================================================================================================================