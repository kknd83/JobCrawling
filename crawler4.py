import csv

#https://woolbro.tistory.com/35?category=818995

# csv파일 읽어오기 
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)

    print(reader)
    print(type(reader))
    print(dir(reader))




# 딜리미터가 , 가 아닌경우 
with open('./resource/sample2.csv', 'r') as f:
    reader = csv.reader(f, delimiter = '|')

    for txt in reader:
        print(txt)

#딕셔너리 형태로 읽어오기 
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)
    for c in reader:
        print(c)


#딕셔너리 상세출력하기 
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)
    for c in reader:
        for k, v in c.items():
            print(k,v)
        print("#################")