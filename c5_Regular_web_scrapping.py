import requests
url="http://www.iitkgp.ac.in/department/CS"
html=requests.get(url)
data=html.content
print(data[1:200])
