import requests

urll = "https://developers.google.com/custom-search/v1/using_rest";
urlll = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY";
auzurl = "https://learn-dev.api.auzmor.com/api/v1/organizations?subdomain=sport";
para = {
    'symbol':'NIFTY'
}
head = {
    'accept':'*/*',
    'host':'www.nseindia.com',
    'accept-encoding':'gzip, deflate, br',
    'connection':'keep-alive',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
print("Before")
res = requests.get(url=urlll,headers=head,timeout=10);
print("middle")
print(res.json());
print("After")