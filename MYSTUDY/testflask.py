import requests
 
r = requests.get('https://api.github.com', auth=('user', 'pass'))

print requests.codes.ok
print r.status_code
print r.headers['content-type']