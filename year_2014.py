def year_2014_12():
    
    
 
    city = ['Bachodistrict', 'Bachodistrict', 'Bachodistrict', 'Kabangdistrict', 'Riang', 'Mayo', 'BannangSata', 'ThaKamcham', \
            'MuangYaladistrict', 'BanKhaoDin', 'BangoSato', 'Yupo', 'Unknown', 'Unknown', 'Sawo', 'PlongHoi']
 
    fata = ['0', '0', '0', '0', '0', '1', '0', '0', '1', '1', '1', '0', '0', '0', '0', '0']
    inju = ['0', '0', '0', '0', '3', '0', '2', '0', '1', '0', '0', '0', '2', '0', '0', '0']
 
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [inj,fat]
    return all_list

def year_2014_11():
 
    city = ['TanyongTalo', 'Waeng', 'RuamThaiPattana', 'SiSakhon', 'BanBluKa', 'KhokPhodistrict', 'Betongdistrict', 'Aiyoeweng', \
            'KhaoTum', 'BannangSatadistrict', 'Ruesodistrict', 'ChoengKhiri', 'Wat', 'SungaiPadidistrict', 'Talubo', 'Muangdistrict', 'TakBaidistrict', 'ThaMuang']
 
    fata = ['1', '0', '0', '2', '0', '1', '2', '1', '0', '0', '1', '0', '0', '0', '2', '1', '1', '2']
    inju = ['1', '2', '2', '0', '1', '0', '0', '1', '1', '0', '1', '1', '4', '0', '3', '0', '3', '7']
 
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [inj,fat]
    return all_list

def year_2014_10():
     city = ['BanBuere', 'BanBluka', 'BanTalaKhosator', 'Samakkhi', 'Sawo', 'BangKhao', 'MuangPattanidistrict', 'MuangPattanidistrict', \
            'MuangPattanidistrict', 'MuangPattanidistrict', 'PuloPuyo', 'DonRak', 'Tabing', 'Ruesodistrict', 'Jakwa', 'SungaiKolokdistrict', 'Mayodistrict', \
            'ThungYangDaengdistrict', 'ThungYangDaengdistrict', 'ThungYangDaengdistrict', 'ThungYangDaengdistrict', 'ThungYangDaengdistrict', 'Ruesodistrict', 'NongChikdistrict', 'JohBoh', 'Unknown']
     fata = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0']
     inju = ['0', '0', '0', '0', '0', '0', '0', '2', '0', '0', '0', '0', '0', '0', '0', '4', '0', '0', '0', '0', '0', '0', '2', '0', '0', '6']
 
     inj = 0
     fat = 0
     list_test = []
     for i in inju:
         inj += int(i)
     for j in fata:
         fat += int(j)
     all_list = [inj,fat]
     return all_list

def year_2014_09():

    city = ['Talopuyo', 'LanChang', 'MuangYaladistrict', 'Rueso', 'ThanTodistrict', 'Rangaedistrict', \
            'Thephadistrict', 'Yaringdistrict', 'KhokPhodistrict', 'KhokPhodistrict', 'Batong']
 
    fata = ['0', '1', '0', '1', '0', '0', '1', '0', '1', '2', '0']
    inju = ['2', '0', '1', '2', '0', '0', '0', '0', '5', '0', '0']
 
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
    if year == '2014':
        print('enter your mont')
        mont = input()
        if mont == '12':
            j = year_2014_12()
            inj = j[0]
            fata = j[1]
            print('all in jur in mont =', inj)
            print('all fata in mont =', fata)
        elif mont == '10':
            j = year_2014_10()
            inj = j[0]
            fata = j[1]
            print('all in jur in mont =', inj)
            print('all fata in mont =', fata)
        elif mont == '11':
            j = year_2014_11()
            inj = j[0]
            fata = j[1]
            print('all in jur in mont =', inj)
            print('all fata in mont =', fata)
        elif mont == '09':
            j = year_2014_09()
            inj = j[0]
            fata = j[1]
            print('all in jur in mont =', inj)
            print('all fata in mont =', fata)
test()
    
