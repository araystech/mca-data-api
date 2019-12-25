import requests

url = "compdatasandbox.96.lt/getCinParcing.php"

payload = {'srn': '{srn}',
'cin': '{cin}',
'apiid': '{apiid}',
'apipass': '{apipassword}'}
files = [

]
headers = {
  'Content-Type': 'multipart/form-data; boundary=--------------------------776887819849444122523606'
}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))
