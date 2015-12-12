from nvd3 import stackedAreaChart
import pygmaps

from nvd3 import multiBarChart
from year_2011 import year_2011_12, year_2011_11, year_2011_10, year_2011_09,\
     year_2011_08, year_2011_07, year_2011_06, year_2011_05, year_2011_04,\
     year_2011_03, year_2011_02, year_2011_01
from year_2013 import year_2013_12, year_2013_11, year_2013_10, year_2013_09,\
     year_2013_08, year_2013_07, year_2013_06, year_2013_05, year_2013_04,\
     year_2013_03, year_2013_02, year_2013_01
from year_2012 import year_2012_12, year_2012_11, year_2012_10, year_2012_09,\
     year_2012_08, year_2012_07, year_2012_06, year_2012_05, year_2012_04,\
     year_2012_03, year_2012_02, year_2012_01
from year_2014 import year_2014_12, year_2014_11, year_2014_10, year_2014_09,\
     year_2014_08, year_2014_07, year_2014_06, year_2014_05, year_2014_04,\
     year_2014_03, year_2014_02, year_2014_01
from year_2008 import year_2008_12, year_2008_11, year_2008_10, year_2008_09,\
     year_2008_08, year_2008_07, year_2008_06, year_2008_05, year_2008_04,\
     year_2008_03, year_2008_02, year_2008_01
from year_2010 import year_2010_12, year_2010_11, year_2010_10, year_2010_09,\
     year_2010_08, year_2010_07, year_2010_06, year_2010_05, year_2010_04,\
     year_2010_03, year_2010_02, year_2010_01



def main():
    mo = ['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE',\
          'JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
    ######year 2014#####
    list_inj = []
    list_fata = []
    list_la = []     ###
    list_long = []    ###
    lis = year_2014_01()
    fata = lis[0]
    inj = lis[1]
    la = lis[3]  ###
    long = lis[4] ###
    list_inj.append(inj)
    list_fata.append(fata)
    list_la.append(la)    ###
    list_long.append(long)  ###

    
    lis = year_2014_02()
    fata = lis[0]
    inj = lis[1]
    la = lis[3]  ###
    long = lis[4] ###
    list_inj.append(inj)
    list_fata.append(fata)
    list_la.append(la)    ###
    list_long.append(long)  ###
    
    lis = year_2014_03()
    fata = lis[0]
    inj = lis[1]
    la = lis[3]  ###
    long = lis[4] ###
    list_inj.append(inj)
    list_fata.append(fata)
    list_la.append(la)    ###
    list_long.append(long)  ###
    
    lis = year_2014_04()
    fata = lis[0]
    inj = lis[1]
 
    la = lis[3]  ###
    long = lis[4] ###
    list_inj.append(inj)
    list_fata.append(fata)
    list_la.append(la)    ###
    list_long.append(long)  ###
    
    lis = year_2014_05()
    fata = lis[0]
    inj = lis[1]

    la = lis[3]  ###
    long = lis[4] ###
    list_inj.append(inj)
    list_fata.append(fata)
    list_la.append(la)    ###
    list_long.append(long)  ###
    
    lis = year_2014_06()
    fata = lis[0]
    inj = lis[1]

    la = lis[3]  ###
    long = lis[4] ###
    list_inj.append(inj)
    list_fata.append(fata)
    list_la.append(la)    ###
    list_long.append(long)  ###
    
    lis = year_2014_07()
    fata = lis[0]
    inj = lis[1]

    la = lis[3]  ###
    long = lis[4] ###
    list_inj.append(inj)
    list_fata.append(fata)
    list_la.append(la)    ###
    list_long.append(long)  ###
    
    lis = year_2014_08()
    fata = lis[0]
    inj = lis[1]

    la = lis[3]  ###
    long = lis[4] ###
    list_inj.append(inj)
    list_fata.append(fata)
    list_la.append(la)    ###
    list_long.append(long)  ###
    
    lis = year_2014_09()
    fata = lis[0]
    inj = lis[1]

    la = lis[3]  ###
    long = lis[4] ###
    list_inj.append(inj)
    list_fata.append(fata)
    list_la.append(la)    ###
    list_long.append(long)  ###
    
    lis = year_2014_10()
    fata = lis[0]
    inj = lis[1]

    la = lis[3]  ###
    long = lis[4] ###
    list_inj.append(inj)
    list_fata.append(fata)
    list_la.append(la)    ###
    list_long.append(long)  ###
    
    lis = year_2014_11()
    fata = lis[0]
    inj = lis[1]
 
    la = lis[3]  ###
    long = lis[4] ###
    list_inj.append(inj)
    list_fata.append(fata)
    list_la.append(la)    ###
    list_long.append(long)  ###
    
    lis = year_2014_12()
    fata = lis[0]
    inj = lis[1]
  
    la = lis[3]  ###
    long = lis[4] ###
    list_inj.append(inj)
    list_fata.append(fata)
    list_la.append(la)    ###
    list_long.append(long)  ###
    
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
    ##end year 2013##

    #####year 2012#####
    list_inj = []
    list_fata = []
    lis = year_2012_01()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2012_02()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2012_03()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2012_04()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2012_05()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2012_06()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2012_07()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2012_08()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2012_09()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2012_10()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2012_11()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2012_12()
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
    
    text_file = open("year_2012.html", "w")
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
    #####year 2010#####
    list_inj = []
    list_fata = []
    lis = year_2010_01()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2010_02()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2010_03()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2010_04()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2010_05()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2010_06()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2010_07()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2010_08()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2010_09()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2010_10()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2010_11()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2010_12()
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
    
    text_file = open("year_2010.html", "w")
    text_file.write(chart.htmlcontent)
    text_file.close()
    
    ####year 2008#####
    list_inj = []
    list_fata = []
    lis = year_2008_01()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2008_02()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2008_03()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2008_04()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2008_05()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2008_06()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2008_07()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2008_08()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2008_09()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2008_10()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2008_11()
    fata = lis[0]
    inj = lis[1]
    list_inj.append(inj)
    list_fata.append(fata)
    lis = year_2008_12()
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
    
    text_file = open("year_2008.html", "w")
    text_file.write(chart.htmlcontent)
    text_file.close()


    ########################################################
    ########################################################
    ########################################################
                        ####plot map####

    ######year 2014#
    
    new_la = []
    new_long = []
    for i in list_la:
        num = float(i)
        new_la.append(num)
    for j in list_long:
        num2 = float(j)
        new_long.append(num2)
    print(new_la)
    print(new_long)
    mymap = pygmaps.maps(new_la[0], new_long[0], 24)
     
    path = [(new_la[1], new_long[1]),
            (new_la[2], new_long[2]),
            (new_la[3], new_long[3]),
            (new_la[4], new_long[4]),
            (new_la[5], new_long[5]),
            (new_la[6], new_long[6]),
            (new_la[7], new_long[7]),
            (new_la[8], new_long[8]),
            (new_la[9], new_long[9]),
            (new_la[10], new_long[10]),
            (new_la[11], new_long[11])]
 
    for point in path:
        mymap.addpoint(point[0], point[1])
 

    mymap.draw('./mymap_2014.html')

    #########END 2014##########
    
    
main()
    
