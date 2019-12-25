import requests

url = "compdatasandbox.96.lt/getCinByName.php"

payload = {'name': 'L',
'apiid': 'mNp7yu3RthRs',
'apipass': 'legaldesk@123'}
files = [

]
headers= {}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))