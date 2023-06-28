import requests

def start():
    # API credentials
    api_key = 'a0241e7861ae5c5'
    api_secret = '365f4b2f89e0d9a'

    # API endpoint
    url = 'https://erp04.tetraserver.com/api/resource/Sales%20Invoice'

    # Request headers
    headers = {
        'Authorization': f'token {api_key}:{api_secret}',
        'Content-Type': 'application/json'
    }

    # Make GET request
    response = requests.get(url, headers=headers)

    # Handle response
    if response.status_code == 200:
        data = response.json()
        # Process the data as needed
        print(data)
    else:
        print('Request failed with status code:', response.status_code)
        print('Error message:', response.text)
