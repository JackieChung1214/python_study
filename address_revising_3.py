import csv

#注意編碼為utf-8-sig
with open('地址資料.csv',"r",encoding="utf-8-sig") as infile:
    data=list(csv.DictReader(infile))
    #print(data)
    for e in data:
        print('原始資料:', e['姓名'], e['縣市'], e['住址'])
        if e['縣市'][0]=="台":
            e['縣市']="臺"+e['縣市'][1:]
        if "F" in e['住址']:
            e['住址']=e['住址'].replace("F","樓")
        if "臺中市" in e['縣市'] and "中港路" in e['住址'] :
            e['住址']=e['住址'].replace("中港路","臺灣大道")

        print('變更資料:', e['姓名'], e['縣市'], e['住址'])

#寫入檔案
with open('新地址資料.csv','w',newline="") as outfile:
    writer=csv.DictWriter(outfile,fieldnames=data[0].keys())
    writer.writeheader()
    for e in data:
        #writerow()與writerows()不同
        writer.writerow(e)