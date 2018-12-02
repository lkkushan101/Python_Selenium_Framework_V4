from Utility.OnlineBarCodeQRCode import verify_online_barcode

contents = verify_online_barcode('http://qreateandtrack.com/files/2009/12/maps.png')
print(contents)