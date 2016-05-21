import requests

proxy_info = {
    'http': '165.225.96.34:9480',
    'https': '165.225.96.34:9480',
}

req = requests.get('http://google.com', proxies=proxy_info)
print req.content