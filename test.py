import json,requests
url = "https://data.octagon58.hasura-app.io/v1/query"

# This is the json payload for the query
requestPayload = {
    "type": "select",
    "args": {
        "table": "users",


        }
    }

# Setting headers
headers = {
    "Content-Type": "application/json"
}

# Make the query and store response in resp
resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)
print resp.content
