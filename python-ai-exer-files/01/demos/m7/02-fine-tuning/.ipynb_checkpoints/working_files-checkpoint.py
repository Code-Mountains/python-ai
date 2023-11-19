"""Open AI List Files"""

import json
import os
import requests

# API
print("\n\n---API---\n\n")


def make_get_request(url):
    """Takes a prompt as an argument and sends a POST request to the OpenAI API"""
    headers = {
        'Authorization': f'Bearer {os.getenv("OPENAI_API_KEY")}'
    }
    response = requests.get(url, headers=headers, timeout=20)

    if response.status_code == 200:
        result = response.json()
        return result
    print('Request failed with status code:', response.status_code)
    return None


def make_delete_request(url):
    """Takes a prompt as an argument and sends a POST request to the OpenAI API"""
    headers = {
        'Authorization': f'Bearer {os.getenv("OPENAI_API_KEY")}'
    }
    response = requests.delete(url, headers=headers, timeout=20)

    if response.status_code == 200:
        result = response.json()
        return result
    print('Request failed with status code:', response.status_code)
    return None


def make_post_request(url, data, files):
    """Takes a prompt as an argument and sends a POST request to the OpenAI API"""
    headers = {
        'Authorization': f'Bearer {os.getenv("OPENAI_API_KEY")}'
    }
    response = requests.post(url, headers=headers, data=data, files=files, timeout=20)

    if response.status_code == 200:
        result = response.json()
        return result
    print('Request failed with status code:', response.status_code)
    return None


# List Files

LIST_URL = "https://api.openai.com/v1/files"
list_result = make_get_request(LIST_URL)

if list_result:
    print(json.dumps(list_result, indent=2))

# Upload File

UPLOAD_URL = "https://api.openai.com/v1/files"
data = {
    "purpose": "fine-tune"
}
files = {
    "file": open("./research/m4/demos/data.jsonl", "rb")
}
upload_result = make_post_request(UPLOAD_URL, data, files)

if upload_result:
    print(json.dumps(upload_result, indent=2))

uploaded_file_id = upload_result["id"]

# Retrieve File

RETRIEVE_URL = f"https://api.openai.com/v1/files/{uploaded_file_id}"
retrieve_result = make_get_request(RETRIEVE_URL)

if retrieve_result:
    print(json.dumps(retrieve_result, indent=2))

# Delete File

DELETE_URL = f"https://api.openai.com/v1/files/{uploaded_file_id}"
delete_result = make_delete_request(DELETE_URL)

if delete_result:
    print(json.dumps(delete_result, indent=2))
