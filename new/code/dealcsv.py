# -*-coding:utf-8-*-
# _coding:utf-8_*_

import csv
import numpy

def getcsv():

    csvpath = '../data/csv/network.csv'
    csvpath_num = '../data/csv/network_num.csv'
    csv_file = csv.reader(open(csvpath,'r'))
    my_matrix = numpy.loadtxt(open(csvpath_num, "rb"), delimiter=",", skiprows=0)
    print (my_matrix)
    # for i in csv_file:
    #     print (i)


if __name__ == '__main__':

    getcsv()