def getLength(number):
    Length = 0
    while number != 0:
        Length += 1
        number = number // 10    #关键，整数除法去掉最右边的一位
    return Length
