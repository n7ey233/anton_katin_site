import requests

print('url')
id_telegi = '405347178'
text = 'text'
telega_token = '700264978:AAG6PdQSBamU5nREeT8c07fUzoz5EzNp6Pg'
url = "https://api.telegram.org/bot"+telega_token+"/sendMessage?chat_id="+id_telegi+"&text="+text
print(url)
#r = requests.get('https://api.telegram.org/bot700264978:AAG6PdQSBamU5nREeT8c07fUzoz5EzNp6Pg/sendMessage?chat_id=405347178&text=text')
r = requests.get(url)
print(r.text)