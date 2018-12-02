from PIL import ImageChops, Image


def compareImages(file_sourcename, filedestination_name):
    im1 = Image.open('./CompareImages/'+filedestination_name)
    im2 = Image.open('./DownloadedFiles/'+file_sourcename)
    try:
        diff = ImageChops.difference(im2, im1)

    except ValueError:
       print("Images are different....")