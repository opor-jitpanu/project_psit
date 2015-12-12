from nvd3 import stackedAreaChart
def year_2014_12():

    city = ['Bachodistrict', 'Bachodistrict', 'Bachodistrict', 'Kabangdistrict', 'Riang', 'Mayo', 'BannangSata', 'ThaKamcham', \
            'MuangYaladistrict', 'BanKhaoDin', 'BangoSato', 'Yupo', 'Unknown', 'Unknown', 'Sawo', 'PlongHoi']
    city_max = 'Bacho district'  ###
    la = '6.516944'  ###
    long = '101.651667'  ###
    fata = ['0', '0', '0', '0', '0', '1', '0', '0', '1', '1', '1', '0', '0', '0', '0', '0']
    inju = ['0', '0', '0', '0', '3', '0', '2', '0', '1', '0', '0', '0', '2', '0', '0', '0']
    
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [inj,fat,city_max,la,long]   
    return all_list

def year_2014_11():
    city = ['TanyongTalo', 'Waeng', 'RuamThaiPattana', 'SiSakhon', 'BanBluKa', 'KhokPhodistrict', 'Betongdistrict', 'Aiyoeweng', \
            'KhaoTum', 'BannangSatadistrict', 'Ruesodistrict', 'ChoengKhiri', 'Wat', 'SungaiPadidistrict', 'Talubo', 'Muangdistrict', 'TakBaidistrict', 'ThaMuang']
<<<<<<< HEAD
=======
    city_max =
    la =
    long = 
>>>>>>> origin/master
    fata = ['1', '0', '0', '2', '0', '1', '2', '1', '0', '0', '1', '0', '0', '0', '2', '1', '1', '2']
    inju = ['1', '2', '2', '0', '1', '0', '0', '1', '1', '0', '1', '1', '4', '0', '3', '0', '3', '7']
    city_max = ''
    la =
    long = 
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [inj,fat,city_max,la,long]
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
     all_list = [inj,fat,city_max,la,long]
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
    all_list = [inj,fat,city_max,la,long]
    return all_list

def year_2014_08():
    city = ['Ramandistrict', 'BangKri', 'Bangkok', 'BannangSatadistrict', 'SiSakhondistrict', 'Ramandistrict', \
            'MuangYaladistrict','BanRae', 'PituMudi', 'BannangSatadistrict', 'KaluwoNuea', 'Kabang', 'SaiBuridistrict', \
            'ThungYangDaengdistrict', 'TakBaidistrict', 'Yahadistrict', 'Mayodistrict', 'Wankra', 'BueRe', 'Yahadistrict']
    fata = ['1', '1', '1', '0', '1', '0', '0','0', '0', '0', '1', '2', '0', '0', '1', '2', '0', '0', '0', '2']
    inju = ['0', '2', '1', '1', '0', '0', '0','2', '2', '0', '2', '0', '1', '4', '0', '1', '3', '5', '1', '0']
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [inj,fat,city_max,la,long]
    return all_list
def year_2014_07():
    city = ['Rueso', 'TohBala', 'NongChikdistrict', 'Sukhirindistrict', 'LamMai', 'Betong', 'ThaKham', 'NaPradu', \
            'Panaredistrict','RusaMilae', 'TanyongMat', 'TanyongMat', 'TanyongMat', 'Unknown', 'ThungYangDaengdistrict', \
            'NamDam', 'BannangSatadistrict', 'TakBaidistrict', 'Juab', 'KrongPinangdistrict', 'Yaha', 'Waeng', 'Purong', \
            'Waengdistrict', 'SaiBuridistrict', 'ThanTodistrict', 'Ruesodistrict', 'Ramandistrict']
    fata = ['4', '1', '1', '1', '0', '3', '0', '2', '0','0', '0', '0', '0', '3', '0', '3', '0', \
            '1', '0', '3', '2', '0', '0', '0', '0', '1', '0', '0']
    inju = ['1', '5', '0', '3', '1', '35', '0', '8', '0','3', '0', '0', '0', '5', '0', '5', '1', '0', \
            '1', '1', '0', '5', '6', '1', '2', '1', '0', '1']
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [inj,fat,city_max,la,long]
    return all_list

def year_2014_06():
    city = ['BanThaMuang', 'Unknown', 'TanyongMat', 'TanyongMat', 'BanTaba', 'Yamu', 'SiSakhon', \
            'Panaredistrict', 'BangKhao', 'Ramandistrict', 'ChangPhueak', 'ChangPhueak', 'ChangPhueak', \
            'Dusongyo', 'KhokPhodistrict', 'BannangSatadistrict', 'SaiBuridistrict', 'MoMawi', 'PlongHoi', \
            'MuangPattanidistrict', 'Kotabaru', 'Yala', 'Trobon', 'NongChikdistrict', 'Rangaedistrict', 'ThungYangDaengdistrict', \
            'ThungYangDaengdistrict']
    fata = ['1', '1', '0', '0', '2', '0', '2', '1', '0', '0', '1', '0', '0', '1', \
            '1', '0', '1', '0', '0', '0', '0', '1', '2', '1', '2', '0', '1']
    inju = ['1', '0', '0', '0', '2', '2', '5', '0', '2', '0', '0', '0', '1', '1', \
            '2', '2', '0', '2', '5', '2', '0', '0', '0', '0', '0', '0', '1']
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [inj,fat,city_max,la,long]
    return all_list

def year_2014_05():
    city = ['Yahadistrict', 'Yahadistrict', 'KhokPhodistrict', 'Bachodistrict', \
            'Mayodistrict', 'Ruesodistrict', 'Ruesodistrict', 'Bachodistrict', 'NongChikdistrict', 'ThaSap', 'KhokPhodistrict', \
            'BoThong', 'KampungNatKamis', 'BangoSato', 'BangoSato', 'SiSakhon', 'ThanTodistrict', 'MuangYaladistrict', 'NamDam', 'Bangkok', \
            'Bangkok', 'TanyongMat', 'Bukit', 'SungaiKolok', 'SungaiKolok', 'KamphaengSaendistrict', 'PathumThani', 'KrongPinangdistrict', \
            'MuangYaladistrict', 'TakBaidistrict', 'TakBaidistrict', 'ThanTodistrict', 'ThanToistrict', 'Yahadistrict', 'Patae', \
            'SungaiPadidistrict', 'SungaiPadidistrict', 'SungaiPadidistrict', 'SungaiPadidistrict', 'SungaiPadidistrict', \
            'SungaiPadidistrict', 'SungaiPadidistrict', 'SungaiKolokdistrict', 'SungaiKolokdistrict', 'SungaiKolokdistrict', \
            'SungaiKolok', 'SungaiKolok', 'SungaiKolok', 'Bangkok', 'Bangkok', 'Bangkok', 'Bangkok', 'Bangkok', 'Bangkok',\
            'Mayodistrict', 'HatYai', 'HatYai', 'HatYai', 'HatYai', 'HatYai', 'Bangkok']
    fata = ['0', '1', '0', '0', '1', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', \
            '2', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', \
            '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0','1', '0', '0', '0', '0', '0', '0']
    inju = ['0', '0', '10', '1', '0', '0', '0', '2', '0', '0', '0', '1', '3', '5', '3', '1', '0', '1', '3', \
            '10', '10', '0', '0', '0', '0', '0', '0', '0', '0', '0', '5', '0', '0', '0', '0', '0', '0', '0', \
            '0', '0', '0', '0', '9', '0', '0', '1', '0', '0', '0', '2', '0', '0', '0', '0','0', '0', '0', '0', '0', '5', '1']
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [inj,fat,city_max,la,long]
    return all_list

def year_2014_04():
    city = ['SanKamphaengdistrict', 'Yingodistrict', 'SiSakhondistrict', 'WasukriBeach', 'Nonthaburi', \
            'Bangkok', 'Bangkok', 'LamLukKadistrict', 'ChangPhueak', 'LakSi', 'Trang', 'BannangSatadistrict', \
            'KholoTanyong', 'Bangkok', 'LatSawai', 'Bangkok', 'Bangkok', 'Bangkok', 'Yala', 'Yala', 'Yala', 'Yala', \
            'Yala', 'Yala', 'Yala', 'Yala', 'Bangkok', 'Bangkok', 'Tuyong', 'BanKasungNai', 'Nonthaburi']
    fata = ['0', '0', '1', '3', '0', '0', '1', '0', '0', '0', '1', '3', '1', '0', '0', '0',\
            '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '3', '1']
    inju = ['0', '0', '1', '15', '0', '0', '0', '0', '1', '0', '0', '1', '0', '0', '0', '1', '0',\
            '2', '0', '0', '0', '0', '6', '6', '6', '6', '2', '0', '0', '0', '4']
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [inj,fat,city_max,la,long]
    return all_list

def year_2014_03():
    city = ['NaPradu', 'Samakkhi', 'Riang', 'Bangkok', 'Nonthaburi', 'MaeSotdistrict', 'ChaengWattana', \
            'Phutthamonthon', 'ChangPhueakdistrict', 'Nonthaburi', 'Nonthaburi', 'Nonthaburi', 'DaTo', \
            'ChangWatdistrict', 'BangSai', 'BangSai', 'Saraphidistrict', 'ChiangMai', 'ChiangMai', 'Bangkok', \
            'KhaoTum', 'Baraho', 'Bangkok', 'Bangkok', 'Bangkok', 'Bangkok', 'KoChan', 'Ratapanyang', 'Bangkok', \
            'Bangkok', 'Yaha', 'Phutthamonthon', 'Waengdistrict', 'LuboYilai', 'Phutthamonthon', 'Bangkok', 'ChaengWattana', \
            'PalukaSamo', 'BanKhien', 'SungaiKolok', 'Paluru', 'Thanon', 'Yingo', 'Unknown', 'Paku', 'Nonthaburi', 'SungaiPadi', \
            'SungaiPadi', 'SungaiPadi', 'BannangStardistrict', 'Bangkok', 'TanyongMat', 'Banglang', 'Yingo', 'PakChong', 'KayuBokoh', \
            'SalaMai', 'Tanyonglimo']
    fata = ['0', '0', '2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', \
            '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '2', \
            '0', '0', '1', '0', '1', '1', '0', '0', '0', '0', '4', '0', '0', '0', '0', '0', '1', '0', '1', '0', '0', '1', \
            '0', '0', '2', '1', '0', '0', '0', '0']
    inju = ['0', '2', '3', '0', '0', '0', '0', '0', '3', '0', '0', '0', '1', '0', '0', '0', '0', '0', '4', '0', '0', '0', \
            '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '3', '0', '0', '3', '0', '2', '1', '1', '0', '1', \
            '0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '1']
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [inj,fat,city_max,la,long]
    return all_list

def year_2014_02():
    city = ['Piyamumang', 'SanamBinnam', 'Bangkok', 'Riko', 'BanlamohNok', 'Bangkok', 'Bangkok', 'BanNamYen', 'Ache', 'BanPulamong',\
            'BanKhlongTae', 'Bangkok', 'TakBaidistrict', 'Prakprue', 'Bangkok', 'TanyongMat', 'BannangSatadistrict', 'Kayuboko',\
            'Bangkok', 'Bangkok', 'Kabangdistrict', 'BanPulamong', 'KhaoSamingdistrict', 'Bangkok', 'Cho-airong', 'BannangSatadistrict',\
            'BannangSatadistrict', 'Rawaeng', 'Mayo', 'Tapoyo', 'Tapoyo', 'BannangSata', 'Ruesodistrict', 'TanyongMat', 'SaiBuridistrict',\
            'Bangkok', 'Bangkok', 'Klaengdistrict', 'Maelan', 'BanToTeeTae', 'Bangkok', 'BanNamsai', 'Ratapanyang', 'Bangkok', 'Chuap',\
            'PaseYawo', 'Yahadistrict', 'PalukSamo', 'Kabangdistrict', 'Riko', 'Bongo', 'Palukasamoh', 'KhokMo', 'PhayaPhu', 'MuangNan',\
            'Bangkok', 'Paklo', 'Paklo', 'Paklo']
    fata = ['0', '0', '0', '1', '0', '0', '0', '1', '0', '1', '3', '0', '0', '1', '0', '0', '2', '0', '0', '3', '3', '1', '2', '0', '0',\
            '0', '0', '3', '0', '0', '0', '0', '0', '2', '1', '0', '0', '0', '4', '1', '0', '1', '1', '0', '0', '2', '1', '0', '0', '0',\
            '1', '3', '0', '0', '0', '0', '3', '1', '0']
    inju = ['1', '0', '0', '1', '2', '0', '0', '0', '0', '0', '0', '2', '2', '3', '0', '0', '0', '0', '0', '21', '0', '0', '30', '6', '2',\
            '0', '2', '1', '0', '3', '0', '3', '0', '0', '0', '2', '0', '4', '6', '0', '6', '0', '0', '2', '2', '3', '2', '0', '0', '0', '0',\
            '2', '0', '0', '0', '7', '2', '3', '0']
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [inj,fat,city_max,la,long]
    return all_list

def year_2014_01():
    city = ['Bangkok', 'BanMaPring', 'Yahadistrict', 'Rueso', 'SiSakhondistrict', 'LamMai', 'Bangkok', 'Kawa', 'Rangaedistrict',\
            'Bangkok', 'MuangNarathiwatdistrict', 'Yarangdistrict', 'Panare', 'ThanTodistrict', 'UdonThaniMuangdistrict', 'ChiangMaidistrict',\
            'SiSakhondistrict', 'Rangaedistrict', 'MaruboOk', 'Unknown', 'Bangkok', 'Bangkok', 'Cha-amdistrict', 'Bangkok', 'Bangkok',\
            'Bangkok', 'Bangkok', 'Bangkok', 'Bangkok', 'Bangkok', 'SungaiKolokdistrict', 'Yahadistrict', 'Bangkok', 'BannangSatadistrict',\
            'NongChikdistrict', 'Unknown', 'Bangkok', 'LamMai', 'Bangkok', 'Bangkok', 'Bangkok', 'TakBaidistrict', 'LuboYilai', 'PaseYawo',\
            'Yahadistrict', 'Unknown', 'PituMudi', 'Mueangdistrict', 'DonRak', 'Kabang', 'Romsai']
    fata = ['0', '2', '0', '2', '1', '2', '0', '0', '3', '0', '0', '0', '2', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1',\
            '0', '0', '0', '0', '0', '0', '2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1', '1', '0', '0']
    inju = ['2', '0', '2', '1', '0', '0', '0', '0', '0', '1', '0', '1', '2', '3', '1', '0', '2', '3', '5', '1', '14', '14', '0', '2', '36',\
            '0', '0', '0', '0', '2', '1', '1', '0', '2', '0', '0', '0', '0', '1', '4', '4', '1', '1', '0', '0', '0', '1', '1', '0', '0', '1']
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [inj,fat,city_max,la,long]
    return all_list
def year_2011_12():
    city = ['Tathong', 'Ban Ton Phai', 'Raman', 'Ban Klang', 'Tambon Katong', 'Tambon Al Yer Weng'\
            , 'Unknown', 'Unknown', 'Ban Paror Pateh', 'Bacho', 'Unknown', 'Yarang', 'Payud'\
            , 'Unknown', 'Unknown', 'Unknown', 'Ban Buathong', 'Bangkok']
    fata = ['0', '0', '1', '0', '1', '0', '0', '0', '1', '0', '3', '0', '1', '0', '0', '0', '1', '0']
    inju = ['1', '2', '0', '1', '1', '1', '22', '0', '3', '0', '0', '1', '0', '0', '1', '1', '1', '0']
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [inj,fat,city_max,la,long]
    return all_list
    
def year_2011_11():
    
    
 
    city = ['Unknown', 'Ban Pungu', 'Manang Tayor', 'Tambon Wang Phraya' , 'Unknown', 'Unknown'\
            , 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Unknown', 'Pattani', 'Unknown'\
            , 'Pattani', 'Unknown', 'Ban Pileng', 'Palo Bata', 'Unknown', 'Unknown', 'Ban Kayumati']


 
    fata = ['1', '3', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'\
            , '2', '0', '0', '6', '0', '0']
    inju = ['0', '0', '1', '0', '9', '0', '0', '0', '0', '0', '0', '0', '1', '0'\
            , '0', '1', '6', '1', '5', '0']
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [inj,fat,city_max,la,long]
    return all_list

def year_2011_10():
    
    
 
    city = ['Takbai', 'Sungai Kolok', 'Narathiwat', 'Yala', 'Yala', 'Yala', 'Yala', 'Yala'\
            , 'Yala', 'Yala', 'Yala', 'Yala', 'Yala', 'Yala', 'Yala', 'Yala', 'Yala', 'Yala'\
            , 'Yala', 'Muang', 'Muang', 'Mayo', 'Panareh', 'Yala', 'Chanae']


 
    fata = ['0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'\
            , '2', '2', '3', '3', '3', '0', '1']
    inju = ['0', '0', '2', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3'\
            , '5', '3', '4', '1', '0', '1', '0']
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [inj,fat,city_max,la,long]
    return all_list

def year_2011_9():
    
    
 
    city = ['Bacho', 'Unknown', 'Sungai Kolok', 'Sungai Kolok', 'Sungai Kolok', 'Muang', 'Rusoh'] 


 
    fata = ['1', '2', '2', '1', '1', '0', '1']
    inju = ['0', '3', '40', '39', '39', '5', '0']
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [inj,fat,city_max,la,long]
    return all_list

def year_2011_8():
    
    
 
    city = ['Than To', 'Rusoh', 'Yala', 'Yala', 'Saiburi', 'Pattani', 'Yala', 'Ra-ngae', 'Nong Chik'\
            , 'Yala', 'Saiburi', 'Nong Chik']


 
    fata = ['0', '1', '0', '2', '1', '0', '1', '1', '1', '0', '2', '1']
    inju = ['4', '0', '0', '10', '0', '12', '0', '0', '0', '2', '0', '0']
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [inj,fat,city_max,la,long]
    return all_list

def year_2011_7():
    
    
 
    city = ['Rusoh', 'Ra-ngae', 'Muang', 'Yaling', 'Unknown', 'Raman', 'Raman', 'Muang', 'Ra-ngae'\
            , 'Ra-ngae', 'Muang', 'Bacho']


 
    fata = ['0', '0', '0', '0', '2', '3', '0', '0', '2', '1', '0']
    inju = ['1', '0', '7', '1', '11', '0', '10', '0', '0', '0', '0']
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [inj,fat,city_max,la,long]
    return all_list

def year_2011_6():
    
    
 
    city = ['Takbai', 'Bannang Sata', 'Raman', 'Yala', 'Yarang', 'Khok Pho', 'Sungai Pad', 'Cho I Rong'\
            , 'Cho I Rong', 'Takbai']


 
    fata = ['2', '1', '1', '1', '0', '1', '1', '1', '1', '0']
    inju = ['10', '0', '0', '1', '1', '0', '1', '5', '0', '0']
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [inj,fat,city_max,la,long]
    return all_list

def year_2011_5():
    
    
 
    city = ['Saiburi', 'Saiburi', 'Sungai Padi', 'Sungai Padi', 'Yala', 'Unknown', 'Ban Cho Ai Rong'\
            , 'Kapaw', 'Unknown', 'Pattani', 'Bannang Sata', 'Bannang Sata']


 
    fata = ['1', '1', '0', '0', '2', '2', '1', '4', '1', '0', '2', '4']
    inju = ['2', '0', '9', '0', '2', '0', '2', '7', '0', '0', '0', '15']
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [inj,fat,city_max,la,long]
    return all_list

def year_2011_4():
    
    
 
    city = ['Ra-ngae', 'Panareh', 'Sungai Padi', 'Rusoh', 'Bannang Sata', 'Janae', 'Muang', 'Nong Chik']


 
    fata = ['1', '0', '1', '0', '1', '2', '2', '1']
    inju = ['0', '0', '0', '1', '0', '0', '1', '0']
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [inj,fat,city_max,la,long]
    return all_list

def year_2011_3():
    
    
 
    city = ['Bannang Sata', 'Rusoh', 'Raman', 'Muang', 'Raman', 'Betong', 'Raman', 'Rusoh', 'Unknown'\
            , 'Unknown', 'Muang', 'Thungyangdaeng', 'Si Sakhon', 'Panareh', 'Khok Pho', 'Saiburi']


 
    fata = ['0', '1', '1', '1', '1', '1', '1', '2', '1', '1', '1', '1', '0', '1', '1', '0']
    inju = ['1', '0', '1', '0', '0', '1', '0', '3', '1', '0', '0', '0', '2', '1', '2', '1']
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [inj,fat,city_max,la,long]
    return all_list

def year_2011_2():
    
    
 
    city = ['Muang', 'Muang', 'Muang', 'Cho I Rong', 'Muang', 'Muang', 'Ra-ngae', 'Unknown', 'Yala'\
            , 'Muang', 'Yarang', 'Yarang', 'Panareh', 'Nong Chik', 'Muang', 'Muang', 'Muang', 'Muang'\
            , 'Muang', 'Muang', 'Muang']


 
    fata = ['1', '0', '0', '1', '0', '0', '1', '3', '1', '2', '0', '1', '5', '1', '0', '0', '0'\
            , '0', '0', '0', '0']
    inju = ['0', '0', '18', '1', '1', '18', '0', '0', '1', '0', '3', '0', '4', '1', '0', '0', '0'\
            , '0', '0', '0', '0']
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [inj,fat,city_max,la,long]
    return all_list

def year_2011_1():
    
    
 
    city = ['Muang', 'Pattani', 'Ra-ngae', 'Unknown', 'Muang', 'Panareh', 'Muang', 'Khok Pho', 'Muang'\
            , 'Unknown', 'Unknown', 'Sungai Kolok', 'Raman', 'Raman', 'Muang', 'Chanae', 'Unknown'\
            , 'Unknown', 'Narathiwat', 'Nam Phong', 'Ra-ngae']


 
    fata = ['1', '0', '0', '9', '1', '0', '1', '0', '1', '1', '2', '1', '0', '0', '1', '1', '2', '1'\
            , '1', '0', '1']
    inju = ['0', '5', '1', '2', '0', '1', '0', '2', '0', '0', '0', '0', '2', '1', '0', '0', '0', '0'\
            , '0', '0', '0']
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [inj,fat,city_max,la,long]
    return all_list
def test():
    print("enter year")
    year = input()
    if year == '2014':
        mo = ['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE',\
              'JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
        list_inj = []
        list_fata = []
        j = year_2014_12()
        inj = j[0]
        fata = j[1]
        list_inj.append(inj)
        list_fata.append(fata)
        
        j = year_2014_10()
        inj = j[0]
        fata = j[1]
        list_inj.append(inj)
        list_fata.append(fata)
        
        j = year_2014_11()
        inj = j[0]
        fata = j[1]
        list_inj.append(inj)
        list_fata.append(fata)
        
        j = year_2014_09()
        inj = j[0]
        fata = j[1]
        list_inj.append(inj)
        list_fata.append(fata)

        j = year_2014_08()
        inj = j[0]
        fata = j[1]
        list_inj.append(inj)
        list_fata.append(fata)

        j = year_2014_07()
        inj = j[0]
        fata = j[1]
        list_inj.append(inj)
        list_fata.append(fata)

        j = year_2014_06()
        inj = j[0]
        fata = j[1]
        list_inj.append(inj)
        list_fata.append(fata)

        j = year_2014_05()
        inj = j[0]
        fata = j[1]
        list_inj.append(inj)
        list_fata.append(fata)

        j = year_2014_04()
        inj = j[0]
        fata = j[1]
        list_inj.append(inj)
        list_fata.append(fata)

        j = year_2014_03()
        inj = j[0]
        fata = j[1]
        list_inj.append(inj)
        list_fata.append(fata)

        j = year_2014_02()
        inj = j[0]
        fata = j[1]
        list_inj.append(inj)
        list_fata.append(fata)

        j = year_2014_01()
        inj = j[0]
        fata = j[1]
        list_inj.append(inj)
        list_fata.append(fata)


        print(list_inj)
        print(list_fata)

        
        chart = stackedAreaChart(name='stackedAreaChart', height=400, width=400)

        xdata = [1,2,3,4,5,6,7,8,9,10,11,12,]
        ydata = list_inj
        ydata2 = list_fata

        extra_serie = {"tooltip": {"y_start": "There is ", "y_end": " min"}}
        chart.add_serie(name="inj", y=ydata, x=xdata, extra=extra_serie)
        chart.add_serie(name="fata", y=ydata2, x=xdata, extra=extra_serie)
        chart.buildhtml()


        text_file = open("year_2014.html", "w")
        text_file.write(chart.htmlcontent)
        text_file.close()

    elif year == '2011':
        mo = ['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE',\
              'JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
        list_inj = []
        list_fata = []
        j = year_2011_12()
        inj = j[0]
        fata = j[1]
        list_inj.append(inj)
        list_fata.append(fata)
        
        j = year_2011_10()
        inj = j[0]
        fata = j[1]
        list_inj.append(inj)
        list_fata.append(fata)
        
        j = year_2011_11()
        inj = j[0]
        fata = j[1]
        list_inj.append(inj)
        list_fata.append(fata)
        
        j = year_2011_9()
        inj = j[0]
        fata = j[1]
        list_inj.append(inj)
        list_fata.append(fata)

        j = year_2011_8()
        inj = j[0]
        fata = j[1]
        list_inj.append(inj)
        list_fata.append(fata)

        j = year_2011_7()
        inj = j[0]
        fata = j[1]
        list_inj.append(inj)
        list_fata.append(fata)

        j = year_2011_6()
        inj = j[0]
        fata = j[1]
        list_inj.append(inj)
        list_fata.append(fata)

        j = year_2011_5()
        inj = j[0]
        fata = j[1]
        list_inj.append(inj)
        list_fata.append(fata)

        j = year_2011_4()
        inj = j[0]
        fata = j[1]
        list_inj.append(inj)
        list_fata.append(fata)

        j = year_2011_3()
        inj = j[0]
        fata = j[1]
        list_inj.append(inj)
        list_fata.append(fata)

        j = year_2011_2()
        inj = j[0]
        fata = j[1]
        list_inj.append(inj)
        list_fata.append(fata)

        j = year_2011_1()
        inj = j[0]
        fata = j[1]
        list_inj.append(inj)
        list_fata.append(fata)


        print(list_inj)
        print(list_fata)

        
        chart = stackedAreaChart(name='stackedAreaChart', height=400, width=400)

        xdata = [1,2,3,4,5,6,7,8,9,10,11,12,]
        ydata = list_inj
        ydata2 = list_fata

        extra_serie = {"tooltip": {"y_start": "There is ", "y_end": " min"}}
        chart.add_serie(name="inj", y=ydata, x=xdata, extra=extra_serie)
        chart.add_serie(name="fata", y=ydata2, x=xdata, extra=extra_serie)
        chart.buildhtml()


        text_file = open("year_2011.html", "w")
        text_file.write(chart.htmlcontent)
        text_file.close()
test()
    
