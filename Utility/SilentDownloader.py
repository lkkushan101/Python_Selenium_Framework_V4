import requests

def download_file(url, file_name_with_extention):
    req = requests.get(url)
    file = open('../DownloadedFiles/'+file_name_with_extention, 'wb')
    for chunk in req.iter_content(100000):
        file.write(chunk)
    file.close()
