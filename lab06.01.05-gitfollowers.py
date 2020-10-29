import requests
import json
from xlwt import *

url = "https://api.github.com/users/andrewbeattycourseware/followers"
response = requests.get(url)
data = response.json()
print(data)


# 2 output the cars individually
for follower in data:     
    print(follower)

#Get the file name for the new file to write
filename = 'githubusers.json'
with open(filename, 'w') as f:
    json.dump(data, f, indent=4)

# 4 write to excel file
w = Workbook()
ws = w.add_sheet('followers')
row = 0;
ws.write(row,0,"login")
ws.write(row,1,"id")
ws.write(row,2,"node_id")
ws.write(row,3,"avatar_url")
ws.write(row,4,"gravatar_id")
ws.write(row,5,"url")
ws.write(row,6,"avatar_url")
ws.write(row,7,"html_url")
ws.write(row,8,"followers_url")
ws.write(row,9,"following_url")
ws.write(row,10,"gists_url")
ws.write(row,11,"starred_url")
ws.write(row,12,"subscriptions_url")
ws.write(row,13,"organizations_url")
ws.write(row,14,"repos_url")
ws.write(row,15,"events_url")
ws.write(row,16,"received_events_url")
ws.write(row,17,"type")
ws.write(row,18,"site_admin")
row += 1
for follower in data:
    ws.write(row,0,follower["login"])
    ws.write(row,1,follower["id"])
    ws.write(row,2,follower["node_id"])
    ws.write(row,3,follower["avatar_url"])
    ws.write(row,4,follower["gravatar_id"])
    ws.write(row,5,follower["url"])
    ws.write(row,6,follower["avatar_url"])
    ws.write(row,7,follower["html_url"])
    ws.write(row,8,follower["followers_url"])
    ws.write(row,9,follower["following_url"])
    ws.write(row,10,follower["gists_url"])
    ws.write(row,11,follower["starred_url"])
    ws.write(row,12,follower["subscriptions_url"])
    ws.write(row,13,follower["organizations_url"])
    ws.write(row,14,follower["repos_url"])
    ws.write(row,15,follower["events_url"])
    ws.write(row,16,follower["received_events_url"])
    ws.write(row,17,follower["type"])
    ws.write(row,18,follower["site_admin"])
    row += 1
w.save('followers.xls')

