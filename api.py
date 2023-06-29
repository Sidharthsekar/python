import requests

reponse = requests.get("https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY");

print(reponse.status_code);
print(reponse.json());
