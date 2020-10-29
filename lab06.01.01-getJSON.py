import requests
import json
from xlwt import *

url = "http://127.0.0.1:5000/cars"

response = requests.get(url)
data = response.json()

# 1 output the data to the cmd line
print(data)

# 2 output the cars individually
for car in data["cars"]:     
    print(car)
    
# 3 save these cars to a file called f?
# filename = 'cars.json'
# if filename: 
#     with open(filename, 'w') as f:
#         json.dump(data, f, indent=4)

# # 4 write to excel file
# w = Workbook()
# ws = w.add_sheet('cars')
# row = 0;
# ws.write(row,0,"reg")
# ws.write(row,1,"make")
# ws.write(row,2,"model")
# ws.write(row,3,"price")
# row += 1
# for car in data["cars"]:
#  ws.write(row,0, car["reg"])
#  ws.write(row,1,car["make"])
#  ws.write(row,2,car["model"])
#  ws.write(row,3,car["price"])
#  row += 1
# w.save('cars.xls')

    


