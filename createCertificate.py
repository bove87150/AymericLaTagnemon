import urllib2
import os.path

def downloadRessources():
    path = 'ressources/fond.png'
    if os.path.isfile(path) :
        print("file exists")
    else :
        img = urllib2.urlopen('http://p-fb.net/fileadmin/fond_attestation.png')
        with open(path, 'w') as f:
            f.write(img.read())


# check whether the certificate template exists in ressources folder if not use CURL to download it

#def downloadQr():


# use CURL to call the QR creation webservice

#def composeImage(QR, name, certificateName):


# use something like openCV2 or PIL to compose an image from the blank certifacte, the name and the QRcode
# return completed Image

#def injectStegano(completedImage):


# process completed image and manipulate the least valuable bits to insert an ASCII text to the image
# Next create algorithme to revers stegano on any given image (search the bytes with the mask created while encypting),
# this should be done in a different programm
