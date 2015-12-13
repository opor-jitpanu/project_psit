def year_2014():
    dict_city = {}
    city = ['Bachodistrict', 'Bachodistrict', 'Bachodistrict', 'Kabangdistrict', 'Riang', 'Mayo', 'BannangSata', 'ThaKamcham', \
            'MuangYaladistrict', 'BanKhaoDin', 'BangoSato', 'Yupo', 'Unknown', 'Unknown', 'Sawo', 'PlongHoi',\
            'TanyongTalo', 'Waeng', 'RuamThaiPattana', 'SiSakhon', 'BanBluKa', 'KhokPhodistrict', 'Betongdistrict', 'Aiyoeweng', \
            'KhaoTum', 'BannangSatadistrict', 'Ruesodistrict', 'ChoengKhiri', 'Wat', 'SungaiPadidistrict', 'Talubo', 'Muangdistrict', 'TakBaidistrict', 'ThaMuang',\
            'BanBuere', 'BanBluka', 'BanTalaKhosator', 'Samakkhi', 'Sawo', 'BangKhao', 'MuangPattanidistrict', 'MuangPattanidistrict', \
            'MuangPattanidistrict', 'MuangPattanidistrict', 'PuloPuyo', 'DonRak', 'Tabing', 'Ruesodistrict', 'Jakwa', 'SungaiKolokdistrict', 'Mayodistrict', \
            'ThungYangDaengdistrict', 'ThungYangDaengdistrict', 'ThungYangDaengdistrict', 'ThungYangDaengdistrict', 'ThungYangDaengdistrict', 'Ruesodistrict', 'NongChikdistrict', 'JohBoh', 'Unknown',\
            'Talopuyo', 'LanChang', 'MuangYaladistrict', 'Rueso', 'ThanTodistrict', 'Rangaedistrict', \
            'Thephadistrict', 'Yaringdistrict', 'KhokPhodistrict', 'KhokPhodistrict', 'Batong',\
            'Ramandistrict', 'BangKri', 'Bangkok', 'BannangSatadistrict', 'SiSakhondistrict', 'Ramandistrict', \
            'MuangYaladistrict','BanRae', 'PituMudi', 'BannangSatadistrict', 'KaluwoNuea', 'Kabang', 'SaiBuridistrict', \
            'ThungYangDaengdistrict', 'TakBaidistrict', 'Yahadistrict', 'Mayodistrict', 'Wankra', 'BueRe', 'Yahadistrict',\
            'Rueso', 'TohBala', 'NongChikdistrict', 'Sukhirindistrict', 'LamMai', 'Betong', 'ThaKham', 'NaPradu', \
            'Panaredistrict','RusaMilae', 'TanyongMat', 'TanyongMat', 'TanyongMat', 'Unknown', 'ThungYangDaengdistrict', \
            'NamDam', 'BannangSatadistrict', 'TakBaidistrict', 'Juab', 'KrongPinangdistrict', 'Yaha', 'Waeng', 'Purong', \
            'Waengdistrict', 'SaiBuridistrict', 'ThanTodistrict', 'Ruesodistrict', 'Ramandistrict',\
            'BanThaMuang', 'Unknown', 'TanyongMat', 'TanyongMat', 'BanTaba', 'Yamu', 'SiSakhon', \
            'Panaredistrict', 'BangKhao', 'Ramandistrict', 'ChangPhueak', 'ChangPhueak', 'ChangPhueak', \
            'Dusongyo', 'KhokPhodistrict', 'BannangSatadistrict', 'SaiBuridistrict', 'MoMawi', 'PlongHoi', \
            'MuangPattanidistrict', 'Kotabaru', 'Yala', 'Trobon', 'NongChikdistrict', 'Rangaedistrict', 'ThungYangDaengdistrict', \
            'ThungYangDaengdistrict',\
            'Yahadistrict', 'Yahadistrict', 'KhokPhodistrict', 'Bachodistrict', \
            'Mayodistrict', 'Ruesodistrict', 'Ruesodistrict', 'Bachodistrict', 'NongChikdistrict', 'ThaSap', 'KhokPhodistrict', \
            'BoThong', 'KampungNatKamis', 'BangoSato', 'BangoSato', 'SiSakhon', 'ThanTodistrict', 'MuangYaladistrict', 'NamDam', 'Bangkok', \
            'Bangkok', 'TanyongMat', 'Bukit', 'SungaiKolok', 'SungaiKolok', 'KamphaengSaendistrict', 'PathumThani', 'KrongPinangdistrict', \
            'MuangYaladistrict', 'TakBaidistrict', 'TakBaidistrict', 'ThanTodistrict', 'ThanToistrict', 'Yahadistrict', 'Patae', \
            'SungaiPadidistrict', 'SungaiPadidistrict', 'SungaiPadidistrict', 'SungaiPadidistrict', 'SungaiPadidistrict', \
            'SungaiPadidistrict', 'SungaiPadidistrict', 'SungaiKolokdistrict', 'SungaiKolokdistrict', 'SungaiKolokdistrict', \
            'SungaiKolok', 'SungaiKolok', 'SungaiKolok', 'Bangkok', 'Bangkok', 'Bangkok', 'Bangkok', 'Bangkok', 'Bangkok',\
            'Mayodistrict', 'HatYai', 'HatYai', 'HatYai', 'HatYai', 'HatYai', 'Bangkok',\
            'SanKamphaengdistrict', 'Yingodistrict', 'SiSakhondistrict', 'WasukriBeach', 'Nonthaburi', \
            'Bangkok', 'Bangkok', 'LamLukKadistrict', 'ChangPhueak', 'LakSi', 'Trang', 'BannangSatadistrict', \
            'KholoTanyong', 'Bangkok', 'LatSawai', 'Bangkok', 'Bangkok', 'Bangkok', 'Yala', 'Yala', 'Yala', 'Yala', \
            'Yala', 'Yala', 'Yala', 'Yala', 'Bangkok', 'Bangkok', 'Tuyong', 'BanKasungNai', 'Nonthaburi',\
            'NaPradu', 'Samakkhi', 'Riang', 'Bangkok', 'Nonthaburi', 'MaeSotdistrict', 'ChaengWattana', \
            'Phutthamonthon', 'ChangPhueakdistrict', 'Nonthaburi', 'Nonthaburi', 'Nonthaburi', 'DaTo', \
            'ChangWatdistrict', 'BangSai', 'BangSai', 'Saraphidistrict', 'ChiangMai', 'ChiangMai', 'Bangkok', \
            'KhaoTum', 'Baraho', 'Bangkok', 'Bangkok', 'Bangkok', 'Bangkok', 'KoChan', 'Ratapanyang', 'Bangkok', \
            'Bangkok', 'Yaha', 'Phutthamonthon', 'Waengdistrict', 'LuboYilai', 'Phutthamonthon', 'Bangkok', 'ChaengWattana', \
            'PalukaSamo', 'BanKhien', 'SungaiKolok', 'Paluru', 'Thanon', 'Yingo', 'Unknown', 'Paku', 'Nonthaburi', 'SungaiPadi', \
            'SungaiPadi', 'SungaiPadi', 'BannangStardistrict', 'Bangkok', 'TanyongMat', 'Banglang', 'Yingo', 'PakChong', 'KayuBokoh', \
            'SalaMai', 'Tanyonglimo',\
            'Piyamumang', 'SanamBinnam', 'Bangkok', 'Riko', 'BanlamohNok', 'Bangkok', 'Bangkok', 'BanNamYen', 'Ache', 'BanPulamong',\
            'BanKhlongTae', 'Bangkok', 'TakBaidistrict', 'Prakprue', 'Bangkok', 'TanyongMat', 'BannangSatadistrict', 'Kayuboko',\
            'Bangkok', 'Bangkok', 'Kabangdistrict', 'BanPulamong', 'KhaoSamingdistrict', 'Bangkok', 'Cho-airong', 'BannangSatadistrict',\
            'BannangSatadistrict', 'Rawaeng', 'Mayo', 'Tapoyo', 'Tapoyo', 'BannangSata', 'Ruesodistrict', 'TanyongMat', 'SaiBuridistrict',\
            'Bangkok', 'Bangkok', 'Klaengdistrict', 'Maelan', 'BanToTeeTae', 'Bangkok', 'BanNamsai', 'Ratapanyang', 'Bangkok', 'Chuap',\
            'PaseYawo', 'Yahadistrict', 'PalukSamo', 'Kabangdistrict', 'Riko', 'Bongo', 'Palukasamoh', 'KhokMo', 'PhayaPhu', 'MuangNan',\
            'Bangkok', 'Paklo', 'Paklo', 'Paklo',\
            'Bangkok', 'BanMaPring', 'Yahadistrict', 'Rueso', 'SiSakhondistrict', 'LamMai', 'Bangkok', 'Kawa', 'Rangaedistrict',\
            'Bangkok', 'MuangNarathiwatdistrict', 'Yarangdistrict', 'Panare', 'ThanTodistrict', 'UdonThaniMuangdistrict', 'ChiangMaidistrict',\
            'SiSakhondistrict', 'Rangaedistrict', 'MaruboOk', 'Unknown', 'Bangkok', 'Bangkok', 'Cha-amdistrict', 'Bangkok', 'Bangkok',\
            'Bangkok', 'Bangkok', 'Bangkok', 'Bangkok', 'Bangkok', 'SungaiKolokdistrict', 'Yahadistrict', 'Bangkok', 'BannangSatadistrict',\
            'NongChikdistrict', 'Unknown', 'Bangkok', 'LamMai', 'Bangkok', 'Bangkok', 'Bangkok', 'TakBaidistrict', 'LuboYilai', 'PaseYawo',\
            'Yahadistrict', 'Unknown', 'PituMudi', 'Mueangdistrict', 'DonRak', 'Kabang', 'Romsai']
    for i in city:
        if i not in dict_city:
            dict_city[i] = 1
        else:
            dict_city[i] += 1
    city = 'yala'
    la = '6.5399500'
    long = '101.2812800'
    list_all = [city,la,long]
    return list_all
        
