import csv

data = [
    [1,2,3],
    [4,5,6,],
    [7,8,9],
    [10,11,12],
    [13,14,15],
    [16,17,18],
    [19,20,21]
]

with open('./resource/sample3.csv', 'w', newline='') as f:
    makewrite = csv.writer(f)
    makewrite.writerows(data)
    #for value in data:
    #    makewrite.writerow(value)