import requests

url = "compdatasandbox.96.lt/getCinByName.php"

payload = {'name': '{company_name}',
'apiid': '{apiid}',
'apipass': '{apipassword}'}
files = [

]
headers= {}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))