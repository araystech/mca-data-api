import requests

url = "compdatasandbox.96.lt/getCinParcing.php"

payload = {'srn': '123',
'cin': 'U15549KA2012PTC067294',
'apiid': 'mNp7yu3RthRs',
'apipass': 'legaldesk@123'}
files = [

]
headers = {
  'Content-Type': 'multipart/form-data; boundary=--------------------------776887819849444122523606'
}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))
