def year_2012_12():
    city =['See Khiw district','Rangae','Krong Pinang','Unknown','Cho Airong','Cho Airong','Mayo','Rangae','Yaring','Yaring','Sungai Padi','Unknown','Sai Buri','Panare']
    fata = ['1','0','1','0','2','0','2','4','0','0','0','1','1','0']
    inju = ['0','1','0','0','5','6','0','4','0','2','1','0','0','0']
    target =['Government (General)','Government (General)','Police','Business','Government (General),Educational Institution','Military','Educational Institution','Business','Police','Business','Educational Institution','Educational Institution','Private Citizens & Property','Educational Institution']
    for i in inju:
        inj += int(i)
    return inj



def year_2012_11():
    city =['Bacho district','Bacho district','Bacho district']
    fata = ['0','0','0']
    inju = ['0','0','0']
    target =['Police,Police','Police','Private Citizens & Property']



def test():
    print("enter year or type all for all")
    year = input()
    if year == '2012':
        print('enter your mont or type all for all')
        mont = input()
        if mont == '12':
            inj = 99
            year_2014_12(inj)
            print(inj)
            
            
test()
    










