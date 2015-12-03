'''diginity'''
def digin():
    '''print total of number'''
    num = 5
    while num != 0:
        num = int(input())
        if num == 0:
            break
        str_num = str(num)
        summ = 0
        for i in str_num:
            summ += int(i)
        while summ > 9:
            str_num = str(summ)
            summ = 0
            for i in str_num:
                summ += int(i)
        print(summ)
digin()

