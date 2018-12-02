from pyzbar.pyzbar import decode
from Utility.SilentDownloader import download_file
from PIL import Image
def verify_online_barcode(url):
    download_file(url, 'sample.png')
    text_d = decode(Image.open('../DownloadedFiles/sample.png'))
    return text_d