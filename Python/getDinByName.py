import requests

url = "compdatasandbox.96.lt/getDinByName.php"

payload = {'name': 'sa',
'apiid': 'mNp7yu3RthRs',
'apipass': 'legaldesk@123'}
files = [

]
headers = {
  'Content-Type': 'multipart/form-data; boundary=--------------------------520251517599687495464727'
}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))
