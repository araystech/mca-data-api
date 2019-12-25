import requests

url = "compdatasandbox.96.lt/getDinByName.php"

payload = {'name': '{director_name}',
'apiid': '{apiid}',
'apipass': '{apipassword}'}
files = [

]
headers = {
  'Content-Type': 'multipart/form-data; boundary=--------------------------520251517599687495464727'
}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))
