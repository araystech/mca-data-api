import requests

url = "compdatasandbox.96.lt/getRequestGeneratedSRN.php"

payload = {'cin': '{cin}',
'apiid': '{apiid}',
'apipass': '{apipassword}'}
files = [

]
headers = {
  'Content-Type': 'multipart/form-data; boundary=--------------------------173907185680701695118222'
}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))
