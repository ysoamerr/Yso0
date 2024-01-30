import requests

chat_id = "6581896306"
urlp = "https://t.me/elhyba"
url = f"https://api.telegram.org/bot6509131661:AAHhM0h48eChiMRhrtG62jQs2hSQmR73g-0/getChat?chat_id={chat_id}"

req = requests.get(url).json()
print(req)
