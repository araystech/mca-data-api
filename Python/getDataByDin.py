import requests

url = "compdatasandbox.96.lt/getDataByDin.php"

payload = {'din': '{din}',
'apiid': '{apiid}',
'apipass': '{apipassword}'}
files = [

]
headers = {
  'Content-Type': 'multipart/form-data; boundary=--------------------------087833671212675113630524'
}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))
