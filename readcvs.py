import csv


with open("data.csv") as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    data_read = [row for row in reader]
n=len(data_read)
print("Département")
dep=input()
hosp=0
deces=0
for i in range(1,n):
    line=data_read[i][0].split(";")
    
    if line[0]==dep:
        hosp=hosp+int(line[2])
        deces=deces+int(line[4])
        
print(100*deces/hosp)
