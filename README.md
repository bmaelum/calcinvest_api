# FastAPI Tutorial
This repo is for learning how to use FastAPI.

## Tutorial
The code in this tutorial is found in the official documentation for FastAPI: https://fastapi.tiangolo.com/.

## Getting Started
### Requirements
Make sure you have installed the requirements found in requirements.txt in a virtual environment using tools such as conda or virtualenv.

### Running the code
```
uvicorn main:app --reload
```

### Sample Request
#### Python
```
import requests

url = "localhost:8000/items/2"

payload="{\n    \"name\": \"string\",\n    \"price\" : 0\n}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
```

#### Curl
```
curl --location --request PUT 'localhost:8000/items/2' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "string",
    "price" : 0
}'
```




# calcinvest_api
