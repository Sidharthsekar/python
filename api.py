import requests

print("sds")

#reponse = requests.get("https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY");

print("sds")
#print(reponse.status_code);
print("sds")
#print(reponse.json());
print("sds")
URL = "https://www.nseindia.com/api/option-chain-indices"
 
# location given here
location = "NIFTY"
 
# defining a params dict for the parameters to be sent to the API
PARAMS = {'symbol':location}
headers = {'host': 'www.nseindia.com'}
print("before req")
# sending get request and saving the response as response object
#r = requests.get(url = URL, params = PARAMS)
k = requests.get("https://www.nseindia.com/json/option-chain/option-chain.json",headers=headers);
print("after req")
# extracting data in json format
data = k.json()
print(data);