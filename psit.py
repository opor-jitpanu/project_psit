from nvd3 import stackedAreaChart
from year_2011 import year_2011_12, year_2011_11, year_2011_10, year_2011_09,\
     year_2011_08, year_2011_07, year_2011_06, year_2011_05, year_2011_04,\
     year_2011_03, year_2011_02, year_2011_01





def main():
    ######year 2011#####
    list_inj = []
    list_fata = []
    lis = year_2011_01()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2011_02()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2011_03()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2011_04()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2011_05()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2011_06()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2011_07()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2011_08()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2011_09()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2011_10()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2011_11()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2011_12()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    chart = stackedAreaChart(name='stackedAreaChart', height=400, width=400)
    xdata = [1,2,3,4,5,6,7,8,9,10,11,12,]
    ydata = list_inj
    ydata2 = list_fata
    extra_serie = {"tooltip": {"y_start": "There is ", "y_end": " min"}}
    chart.add_serie(name="INJURED", y=ydata, x=xdata, extra=extra_serie)
    chart.add_serie(name="FATALITIES", y=ydata2, x=xdata, extra=extra_serie)
    chart.buildhtml()
    text_file = open("year_2011.html", "w")
    text_file.write(chart.htmlcontent)
    text_file.close()
    ###end year 2011###
main()
    
