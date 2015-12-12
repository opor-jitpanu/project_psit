def main(word):
    date= []
    city = []
    per = []
    fat= []
    inj =[]
    tar = []
    while word != '0':
        lis = word.split()
        date.append(lis[1])
        city.append(lis[3])
        per.append(lis[4])
        fat.append(lis[5])
        inj.append(lis[6])
        tar.append(lis[7])
        
        word = input()
    print('---------------------')
    print(date)
    print('---------------------')
    print(city)
    print('---------------------')
    print(per)
    print('---------------------')
    print(fat)
    print('---------------------')
    print(inj)
    print('---------------------')
    print(tar)
    print('---------------------')
main(input())
