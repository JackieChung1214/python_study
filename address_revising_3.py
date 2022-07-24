import csv

with open('地址資料.csv') as infile:
    data=list(csv.DictReader(infile))
    for e in data:
        print(e['姓名'])