import requests

url = "compdatasandbox.96.lt/getCinTracking.php"

payload = {'cin': '{cin}',
'apiid': '{apiid}',
'apipass': '{apipassword}'}
files = [

]
headers = {
  'Content-Type': 'multipart/form-data; boundary=--------------------------142007429853131240758984'
}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))
