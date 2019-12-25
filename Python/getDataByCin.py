import requests

url = "compdatasandbox.96.lt/getDataByCin.php"

payload = {'cin': '{cin}',
'apiid': '{apiid}',
'apipass': '{apipassword}'}
files = [

]
headers= {}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))