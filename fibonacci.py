def Fibonacci(max_num):
    firstNum = 0
    secondNum = 1
    print(secondNum)
    thirdNum = firstNum + secondNum
    print(thirdNum)
    while (thirdNum + secondNum) < max_num:
        firstNum = secondNum
        secondNum = thirdNum
        thirdNum = firstNum + secondNum
        print(thirdNum)
