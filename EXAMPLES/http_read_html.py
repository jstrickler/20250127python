import requests

URL = 'https://www.python.org'

response = requests.get(URL)

if response.ok:  # is response.status_code >=200 and < 300
    for header, value in sorted(response.headers.items()): # response.headers is a dictionary of the headers
        print(f"{header:20.20s} {value}")
    print()
    # response.content  raw data returned  (file contents, etc)
    # response.text     response.content converted to Python str
    # response.json()   response.content converted to Python data structure from JSON

    print(response.text[:400])   # The text is returned as a bytes object, so it needs to be decoded to a string; print the first 200 bytes
    print('...')
    print(response.text[-400:])   # print the last 200 bytes
