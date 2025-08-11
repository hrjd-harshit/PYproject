import csv

with open('dataa.csv',mode='w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name','age'])
    writer.writerow(['Shardul','27'])
with open('dataa.csv',mode='r') as file:
    reader = csv.reader(file)
    for row in file :
        print(row)