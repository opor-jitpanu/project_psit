def year_2013_12():
    
    city = ['Bangkok', 'PanareDistrict', 'Bangkok', 'Baro', 'Unknown', 'Unknown', 'Unknown', 'TakBaiDistrict', 'Praiwan', 'ThanToDistrict', 'ThaSap', 'BanBannangKuwae', 'Danok', 'Danok', 'Phuket', 'Danok', 'Sadao', 'PadangBesar', 'Bangkok', 'ManangDalam', 'TaloDueRaman', 'RangaeDistrict', 'BanDonRak', 'MaiKaenDistrict', 'Lahan', 'PlongHoi', 'Lahan', 'Bangkok', 'Bangkok', 'NongChik', 'Bangkok', 'ChangPhuak', 'ChangPhuak', ] 
    fata = ['0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '2', '0', '0', '0', '1', '0', '0', '1', '0', '0', '4', '0', '0', '0', '4', '0', '0', '0', ]
    inju = ['5', '0', '4', '1', '0', '0', '3', '2', '0', '4', '2', '3', '0', '0', '0', '25', '0', '0', '0', '0', '0', '2', '0', '2', '8', '9', '2', '1', '0', '2', '0', '3', '0', ]
 
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [inj,fat]
    return all_list

def year_2013_11():
 
    city = ['MueangYala', 'Tanyongmat', 'Thepa', 'Tha Muang', 'Bangkok', 'KhlongManing', 'Thepa', 'Thepa', 'Thepa', 'Thepa', 'SaiBuri', 'Unknown', 'RuesoNarathiwat', 'MarueboTok', 'MaiKaen', 'Kholo', 'Waeng', 'SungaiKolok', 'Tapoyo', 'Rueso', 'TanyongDalo', 'Rueso', 'Kapo', 'MueangNarathiwatDistrict', 'Rangae', 'KampungPohonSetar', 'MueangNarathiwat', 'MueangNarathiwat', 'RuesoNarathiwat', 'RuesoNarathiwat', 'Trobon', 'MueangPattaniDistrict', 'Napradu', 'ManangYong', 'TohDeng', 'BannangSataDistrict', 'Unknown', 'BangSapha', ] 
    fata = ['1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '4', '3', '0', '0', '0', '1', '0', '0', '1', '1', '1', '1', '2', '0', '0', '0', '0', '0', '1', '2', '0', '1', '1', '1', '0', '0', ]
    inju = ['5', '1', '0', '4', '3', '2', '0', '0', '0', '0', '2', '4', '0', '0', '3', '0', '12', '0', '1', '5', '0', '2', '1', '0', '6', '1', '4', '4', '1', '1', '0', '0', '1', '0', '0', '0', '2', '0', ]
 
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [inj,fat]
    return all_list

def year_2013_10():
    
    city = [] 
    fata = []
    inju = []
 
     inj = 0
     fat = 0
     list_test = []
     for i in inju:
         inj += int(i)
     for j in fata:
         fat += int(j)
     all_list = [inj,fat]
     return all_list

def year_2013_09():

    city = [] 
    fata = []
    inju = []
 
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [inj,fat]
    return all_list
    
def test():
    print("enter year")
    year = input()
    if year == '2013':
        print('enter your mont')
        mont = input()
        if mont == '12':
            j = year_2013_12()
            inj = j[0]
            fata = j[1]
            print('all in jur in mont =', inj)
            print('all fata in mont =', fata)
        elif mont == '10':
            j = year_2013_10()
            inj = j[0]
            fata = j[1]
            print('all in jur in mont =', inj)
            print('all fata in mont =', fata)
        elif mont == '11':
            j = year_2013_11()
            inj = j[0]
            fata = j[1]
            print('all in jur in mont =', inj)
            print('all fata in mont =', fata)
        elif mont == '09':
            j = year_2013_09()
            inj = j[0]
            fata = j[1]
            print('all in jur in mont =', inj)
            print('all fata in mont =', fata)
test()
    
