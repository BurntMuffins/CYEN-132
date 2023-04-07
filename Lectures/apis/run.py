from requests import get, post

response = get("http://localhost:1234/first").json()

print(response)


response = post("http://localhost:1234/numberInspector", json={"value":5}).json()
print(response)