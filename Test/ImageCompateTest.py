from Utility.SilentDownloader import download_file
from Utility.ImageCompare import compareImages
download_file("https://www.google.lk/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png","google.png")
compareImages("google.png","googlelogo_color_272x92dp.png")