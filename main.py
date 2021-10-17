#gihub.com/formeo/requestsPY

import requests

class YaUploader:

    def __init__(self, token):
        self.token = token 
    
    def upload(self, path_to_file, file_name):
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(token)}
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {"path": path_to_file, "overwrite": "true"}
        response = requests.get(url = upload_url, headers=headers, params=params)          
        href = response.json()['href']
        response = requests.put(href, data=open(file_name, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
          print("Success")

# Получить путь к загружаемому файлу и токен от пользователя
file_name = 'text.txt'
path_to_file = 'text.txt'
token = '...'
uploader = YaUploader(token)
result = uploader.upload(path_to_file, file_name )


