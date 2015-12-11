def year_2012_12():
    city =['See Khiw district','Rangae','Krong Pinang','Unknown','Cho Airong','Cho Airong','Mayo','Rangae','Yaring','Yaring','Sungai Padi','Unknown','Sai Buri','Panare']
    fata = ['1','0','1','0','2','0','2','4','0','0','0','1','1','0']
    inju = ['0','1','0','0','5','6','0','4','0','2','1','0','0','0']
    for i in inju:
        inj += int(i)
    return inj



def year_2012_11():
    city =['Mai Kaen','Panare','Yarang','Bannang Sata','Nong Chik','Khok Pho','Rueso','Rueso','Rueso','Rueso','Mueang Yala','Unknown','Chanae district','Sungai Padi','Yaha','Takua Thung','Yarang','Khok Pho','Rueso','Rueso','Sungai Padi','Chanae','Chanae','Yarang','Mayo','Rueso','Rueso']
    fata = ['1','0','1','0','1','0','0','0','0','3','1','1','1','1','1','1','0','0','0','3','1','0','0','0','1','3','0']
    inju = ['5','0','0','3','0','2','3','0','0','36','33','0','0','0','0','0','0','6','7','0','0','0','0','1','0','0','8']


def year_2012_10():
    city =['Yaha','Sai Buri','Sai Buri','Yarang','Bang Por','Sai Buri','Si Sakhon','Rueso','Bare Tai','Bare Tai','Khosit','Tak Bai district','Tak Bai district','Tak Bai district','Tak Bai district','Tak Bai district','Rangae','Krong Pinang','Kabang','','','','']
    fata = ['2','0','2','1','0','0','0','1','1','0','0','0','0','1','0','0','0','1','0']
    inju = ['1','0','4','0','1','9','0','0','5','3','0','1','0','1','1','1','0','0','1']


def year_2012_09():
    city =['Yaha','Sai Buri','Sai Buri','Yarang','Bang Por','Sai Buri','Si Sakhon','Rueso','Bare Tai','Bare Tai','Khosit','Tak Bai district','Tak Bai district','Tak Bai district','Tak Bai district','Tak Bai district','Rangae','Krong Pinang','Kabang','','','','']
    fata = ['2','0','2','1','0','0','0','1','1','0','0','0','0','1','0','0','0','1','0']
    inju = ['1','0','4','0','1','9','0','0','5','3','0','1','0','1','1','1','0','0','1']





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
    










