def year_2012_12():
    city =['See Khiw district','Rangae','Krong Pinang','Unknown','Cho Airong','Cho Airong','Mayo','Rangae','Yaring','Yaring','Sungai Padi','Unknown','Sai Buri','Panare']
    fata = ['1','0','1','0','2','0','2','4','0','0','0','1','1','0']
    inju = ['0','1','0','0','5','6','0','4','0','2','1','0','0','0']
    target =['Government (General)','Government (General)','Police','Business','Government (General),Educational Institution','Military','Educational Institution','Business','Police','Business','Educational Institution','Educational Institution','Private Citizens & Property','Educational Institution']
    for i in inju:
        inj += int(i)
    return inj



def year_2012_11():
    city =['Mai Kaen','Panare','Yarang','Bannang Sata','Nong Chik','Khok Pho','Rueso','Rueso','Rueso','Rueso','Mueang Yala','Unknown','Chanae district','Sungai Padi','Yaha','Takua Thung','Yarang','Khok Pho','Rueso','Rueso','Sungai Padi','Chanae','Chanae','Yarang','Mayo','Rueso','Rueso']
    fata = ['1','0','1','0','1','0','0','0','0','3','1','1','1','1','1','1','0','0','0','3','1','0','0','0','1','3','0']
    inju = ['5','0','0','3','0','2','3','0','0','36','33','0','0','0','0','0','0','6','7','0','0','0','0','1','0','Unkown','8']
    target =['Educational Institution','Police','Government (General)','Military','Educational Institution','Military','Military,Private Citizens & Property','Religious Figures/Institutions','Military','Transportation','Military','Military,Private Citizens & Property','Business','Government (General)','Government (General)','Religious Figures/Institutions','Government (General)','Educational Institution','Police,Private Citizens & Property','Private Citizens & Property','Police,Private Citizens & Property','Business','Private Citizens & Property','Poilce','Educational Institution','Private Citizens & Property','Police,Private Citizens & Property','Educational Institution']



def year_2012_10():
    city =['Mai Kaen','Panare','Yarang','Bannang Sata','','','','','','','','','','','','','','','','','','','']
    fata = ['1','0','1','0','','','','','','','','','','','','','','','']
    inju = ['5','0','0','3','','','','','','','','','','','','','','','']
    target =['Educational Institution','Police','Government (General)','','','','','','','','','','','','','','','']





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
    










