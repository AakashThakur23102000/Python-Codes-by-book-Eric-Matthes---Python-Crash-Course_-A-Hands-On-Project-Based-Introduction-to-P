import json
filename = "17data.json"
with open(filename) as f:
    files = json.load(f)
print(f"your fav num is {files}")
