import http.client

conn = http.client.HTTPSConnection("famous-quotes4.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "734e4c39c1msheb017ea994fcef2p1b45d4jsn458c4b8f2005",
    'X-RapidAPI-Host': "famous-quotes4.p.rapidapi.com"
    }

conn.request("GET", "/random?category=all&count=2", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))