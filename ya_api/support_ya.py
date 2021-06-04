import requests

TOKEN = 'token'
dir_url = 'https://cloud-api.yandex.net/v1/disk/resources'


def create_folder(path: str):
    params = {'path': path}
    headers = {'Content-Type': 'application/json',
               'Authorization': TOKEN}
    create_dir = requests.api.put(dir_url, headers=headers, params=params)
    return create_dir.status_code


def delete_folder(path: str):
    params = {'path': path}
    headers = {'Content-Type': 'application/json',
               'Authorization': TOKEN}
    delete_dir = requests.api.delete(dir_url, headers=headers, params=params)
    return delete_dir.status_code
