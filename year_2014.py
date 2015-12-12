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
    all_list = [fat,inj,city_max,la,long] #######
    return all_list

def year_2014_11():
    city = ['TanyongTalo', 'Waeng', 'RuamThaiPattana', 'SiSakhon', 'BanBluKa', 'KhokPhodistrict', 'Betongdistrict', 'Aiyoeweng', \
            'KhaoTum', 'BannangSatadistrict', 'Ruesodistrict', 'ChoengKhiri', 'Wat', 'SungaiPadidistrict', 'Talubo', 'Muangdistrict', 'TakBaidistrict', 'ThaMuang']

    fata = ['1', '0', '0', '2', '0', '1', '2', '1', '0', '0', '1', '0', '0', '0', '2', '1', '1', '2']
    inju = ['1', '2', '2', '0', '1', '0', '0', '1', '1', '0', '1', '1', '4', '0', '3', '0', '3', '7']
    city_max = 'BannangSatadistrict'
    la = '6.266667'
    long = '101.264444'
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [fat,inj,city_max,la,long]
    return all_list

def year_2014_10():
     city = ['BanBuere', 'BanBluka', 'BanTalaKhosator', 'Samakkhi', 'Sawo', 'BangKhao', 'MuangPattanidistrict', 'MuangPattanidistrict', \
            'MuangPattanidistrict', 'MuangPattanidistrict', 'PuloPuyo', 'DonRak', 'Tabing', 'Ruesodistrict', 'Jakwa', 'SungaiKolokdistrict', 'Mayodistrict', \
            'ThungYangDaengdistrict', 'ThungYangDaengdistrict', 'ThungYangDaengdistrict', 'ThungYangDaengdistrict', 'ThungYangDaengdistrict', 'Ruesodistrict', 'NongChikdistrict', 'JohBoh', 'Unknown']
     fata = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0']
     inju = ['0', '0', '0', '0', '0', '0', '0', '2', '0', '0', '0', '0', '0', '0', '0', '4', '0', '0', '0', '0', '0', '0', '2', '0', '0', '6']
     city_max = 'ThungYangDaengdistrict'
     la = '6.6175'
     long = '101.425833'
     inj = 0
     fat = 0
     list_test = []
     for i in inju:
         inj += int(i)
     for j in fata:
         fat += int(j)
     all_list = [fat,inj,city_max,la,long]
     return all_list

def year_2014_09():
    city = ['Talopuyo', 'LanChang', 'MuangYaladistrict', 'Rueso', 'ThanTodistrict', 'Rangaedistrict', \
            'Thephadistrict', 'Yaringdistrict', 'KhokPhodistrict', 'KhokPhodistrict', 'Batong']
 
    fata = ['0', '1', '0', '1', '0', '0', '1', '0', '1', '2', '0']
    inju = ['2', '0', '1', '2', '0', '0', '0', '0', '5', '0', '0']
    city_max = 'KhokPhodistrict'
    la = '6.729444'
    long = '101.096111'
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [fat,inj,city_max,la,long]
    return all_list

def year_2014_08():
    city = ['Ramandistrict', 'BangKri', 'Bangkok', 'BannangSatadistrict', 'SiSakhondistrict', 'Ramandistrict', \
            'MuangYaladistrict','BanRae', 'PituMudi', 'BannangSatadistrict', 'KaluwoNuea', 'Kabang', 'SaiBuridistrict', \
            'ThungYangDaengdistrict', 'TakBaidistrict', 'Yahadistrict', 'Mayodistrict', 'Wankra', 'BueRe', 'Yahadistrict']
    fata = ['1', '1', '1', '0', '1', '0', '0','0', '0', '0', '1', '2', '0', '0', '1', '2', '0', '0', '0', '2']
    inju = ['0', '2', '1', '1', '0', '0', '0','2', '2', '0', '2', '0', '1', '4', '0', '1', '3', '5', '1', '0']
    city_max = 'BannangSatadistrict'
    la = '6.266667'
    long = '101.264444'
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [fat,inj,city_max,la,long]
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
    city_max = 'Ramandistrict'
    la = '6.478333'
    long = '101.424167'
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [fat,inj,city_max,la,long]
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
    city_max = 'ChangPhueak'
    la = '18.803232'
    long = '98.981062'
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [fat,inj,city_max,la,long]
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
    city_max = 'SungaiPadidistrict'
    la = '6.085278'
    long = '101.880278'
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [fat,inj,city_max,la,long]
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
    city_max = 'KholoTanyong'
    la = '6.844444, 101.178611'
    long = '6.844444, 101.178611'
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [fat,inj,city_max,la,long]
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
    city_max = 'BangSai'
    la = '14.212778'
    long = '100.498333'
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [fat,inj,city_max,la,long]
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
    city_max = 'Kabangdistrict'
    la = '6.4275'
    long = '101.019167'
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [fat,inj,city_max,la,long]
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
    city_max = 'Rangaedistrict'
    la = '6.296389'
    long = '101.728333'
    inj = 0
    fat = 0
    list_test = []
    for i in inju:
        inj += int(i)
    for j in fata:
        fat += int(j)
    all_list = [fat,inj,city_max,la,long]
    return all_list


    
