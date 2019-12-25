import requests

url = "compdatasandbox.96.lt/requestDownloadFile.php"

payload = {'cin': 'U15549KA2012PTC067294',
'apiid': 'mNp7yu3RthRs',
'apipass': 'legaldesk@123'}
files = [

]
headers = {
  'Content-Type': 'multipart/form-data; boundary=--------------------------735944852158856520680472'
}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))
