from nvd3 import stackedAreaChart
from nvd3 import multiBarChart
from year_2011 import year_2011_12, year_2011_11, year_2011_10, year_2011_09,\
     year_2011_08, year_2011_07, year_2011_06, year_2011_05, year_2011_04,\
     year_2011_03, year_2011_02, year_2011_01
from year_2013 import year_2013_12, year_2013_11, year_2013_10, year_2013_09,\
     year_2013_08, year_2013_07, year_2013_06, year_2013_05, year_2013_04,\
     year_2013_03, year_2013_02, year_2013_01
from year_2014 import year_2014_12, year_2014_11, year_2014_10, year_2014_09,\
     year_2014_08, year_2014_07, year_2014_06, year_2014_05, year_2014_04,\
     year_2014_03, year_2014_02, year_2014_01





def main():
    mo = ['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE',\
          'JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    ######year 2014#####
    list_inj = []
    list_fata = []
    lis = year_2014_01()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2014_02()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2014_03()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2014_04()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2014_05()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2014_06()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2014_07()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2014_08()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2014_09()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2014_10()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2014_11()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2014_12()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    
    chart = multiBarChart(width=500, height=400, x_axis_format=None)
    xdata = mo
    ydata1 = list_inj
    ydata2 = list_fata

    chart.add_serie(name="INJURED", y=ydata1, x=xdata)
    chart.add_serie(name="FATALITIES", y=ydata2, x=xdata)
    chart.buildhtml()
    
    text_file = open("year_2014.html", "w")
    text_file.write(chart.htmlcontent)
    text_file.close()
    ##end year 2014##

    #####year 2013#####
    list_inj = []
    list_fata = []
    lis = year_2013_01()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2013_02()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2013_03()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2013_04()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2013_05()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2013_06()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2013_07()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2013_08()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2013_09()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2013_10()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2013_11()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2013_12()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    
    chart = multiBarChart(width=500, height=400, x_axis_format=None)
    xdata = mo
    ydata1 = list_inj
    ydata2 = list_fata

    chart.add_serie(name="INJURED", y=ydata1, x=xdata)
    chart.add_serie(name="FATALITIES", y=ydata2, x=xdata)
    chart.buildhtml()
    
    text_file = open("year_2013.html", "w")
    text_file.write(chart.htmlcontent)
    text_file.close()
    
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
    
    chart = multiBarChart(width=500, height=400, x_axis_format=None)
    xdata = mo
    ydata1 = list_inj
    ydata2 = list_fata

    chart.add_serie(name="INJURED", y=ydata1, x=xdata)
    chart.add_serie(name="FATALITIES", y=ydata2, x=xdata)
    chart.buildhtml()
    
    text_file = open("year_2011.html", "w")
    text_file.write(chart.htmlcontent)
    text_file.close()
    ###end year 2011###
main()
    
