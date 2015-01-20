'''
ImageMarkdown
=============
Copyright (c) 2015, Jonathan LURIE, All rights reserved.
This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3.0 of the License, or (at your option) any later version.
This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.
You should have received a copy of the GNU Lesser General Public
License along with this library.
'''

'''
What is it?

This code takes a list of image url and build a Markdown compliant
list of them, with embeded link to themselves.

This intents to facilitate the image ntegration when using a Markdown
plugin in Wordpress.

Requirements:
- The pictures must all be in the same folder (on the web)
- They must be named in a contiguous sequence from M to N (where N is bigger than M)
- They can have a prefix, like DSC_ if they all have the same
- You must specify the extention, like .jpg

Here is a list of file:

http://myurl.com/myHolydays_1.jpg
http://myurl.com/myHolydays_2.jpg
http://myurl.com/myHolydays_3.jpg
-> This works


'''

# Pyperclip is a crossed plateform library to copy text to clipboard
import pyperclip

# For reading the exif data
import exifread

import os
import sys
import urllib2


# list of images to build
_imgList = []
_exifList = []

# default text for the alternative text field of image
_defaultAltText = "Copyright Jonathan Lurie"


def inputByIndexAndExtention():


    # input url of containing folder
    folder = raw_input('\n0- Type the folder URL:\n> ')

    # test if the url finishes by a slash (it must for the following)
    if(folder[-1] != '/'):
        folder = folder + '/'


    # typing the prefix
    prefix = raw_input('\n1- Type the prefix (ie. DSC_ ), or leave blank if none:\n> ')

    # typing the number sequence (first index)
    notDefined = True
    while(notDefined):
        try:
            firstIndex = int(raw_input('\n2- Type the first index (ie. 1) :\n> '))
            notDefined = False
        except ValueError:
            print "This is not a number, try again."


    # typing the number sequence (last index)
    notDefined = True
    while(notDefined):
        try:
            lastIndex = int(raw_input('\n3- Type the last index (ie. 15) :\n> '))
            notDefined = False
        except ValueError:
            print "This is not a number, try again."


    # typing the extention
    ext = raw_input('\n4- Type the file extention (ie. .jpg):\n> ')


    # Typing alternative text
    altText = raw_input('\n5- Type the alternative of all image (of leave blank for default):\n> ')

    # replacing the default Alt Text
    if(altText):
        global _defaultAltText
        _defaultAltText = altText


    # building photo list
    for i in range(firstIndex, lastIndex+1):
        fileURL = folder + prefix + str(i) + ext
        #print(fileURL)
        _imgList.append(fileURL)




def printImageListMarkdown():
    # big string that contain all the output
    bigStr = ''

    # build the links
    for i in range(0, len(_imgList)):
        #imgId = str(i+1)
        # the filename without extention is taken as link ID
        imgId = os.path.splitext(os.path.basename(_imgList[i]))[0]
        bigStr = bigStr + _exifList[i] + ("\n")
        bigStr = bigStr + "[![" + str(_defaultAltText) + "][" + imgId + "]][" + imgId + "]\n\n"
        # [![La photo 2][3]][4]

    # split
    bigStr = bigStr + "\n"

    # build the references at page bottom
    for i in range(0, len(_imgList)):
        #imgId = str(i+1)
        # the filename without extention is taken as link ID
        imgId = os.path.splitext(os.path.basename(_imgList[i]))[0]
        bigStr = bigStr + "  [" + imgId + "]" + ": " + _imgList[i] + " \"" + _defaultAltText + "\""  + "\n"




    print("\t\t OUTPUT")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n\n")

    print(bigStr)

    print("\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print("\t\t END OF OUTPUT")
    print("NOTE: this was automatically copied to your clipboard.")

    pyperclip.copy(bigStr)
    spam = pyperclip.paste()



# fetch the images from the web to a local directory
def fetchImages():

    # get the temp directory
    tempo = None

    if(len(sys.argv) > 1):
        if(os.path.isdir(sys.argv[1])):
            tempo = sys.argv[1]

            print("\nThe image are going to be fetched for exif reading...")

            # fetching every single image to local temp dir
            for img in _imgList:

                try:

                    # copy the file to local
                    print("\tFetching " + os.path.basename(img) + " ... "),
                    distantFile = urllib2.urlopen(img)
                    localFile = open(os.path.join(tempo, os.path.basename(img)),'wb')
                    localFile.write(distantFile.read())
                    localFile.close()
                    print("DONE")

                    # reading the exif
                    exifSentence = buildExifSentence(os.path.join(tempo, os.path.basename(img)))
                    _exifList.append(exifSentence)

                except urllib2.HTTPError as e:

                    print("FAIL! (" + str(e.code) + ")")



# takes an image file address
# return a Markdown string of EXIF data
def buildExifSentence(fileAddress):

    # markdown sentence
    ms = ""

    # Open image file for reading (binary mode)
    f = open(fileAddress, 'rb')

    # Return Exif tags
    tags = exifread.process_file(f)

    # camera model
    if('Image Model' in tags.keys() ):
        ms = ms + "**" + str(tags["Image Model"]) + "** "

    if('EXIF LensModel' in tags.keys() ):
        ms = ms + "with a **" + str(tags["EXIF LensModel"]) + "** lens "

    if('EXIF FocalLength' in tags.keys() ):
        ms = ms + "at **" + str(tags["EXIF FocalLength"]) + "mm** "

    if('EXIF ExposureTime' in tags.keys() ):
        ms = ms + ", a speed of **" + str(tags["EXIF ExposureTime"]) + "s** "

    if('EXIF FNumber' in tags.keys() ):
        fn = str(tags["EXIF FNumber"])

        fnProcessed = None

        # the aperture number is sometimes written as a ratio, we dont want that.
        if("/" in fn):
            fratio = fn.split("/")
            fnProcessed = str(float(fratio[0]) / float(fratio[1]))
        else:
            fnProcessed = str(fn)

        ms = ms + ", an aperture of **f/" + fnProcessed + "** "

    if('EXIF ISOSpeedRatings' in tags.keys() ):
        ms = ms + " and **" + str(tags["EXIF ISOSpeedRatings"]) + "ISO**"



    f.close()

    return ms



if __name__ == "__main__":

    print("\n------------------------ ImageMarkdown -----------------------------------------\n")


    #_imgList.append("http://jonathanlurie.fr/wp-content/uploads/2015/01/DSC9271.jpg")
    #_imgList.append("http://jonathanlurie.fr/wp-content/uploads/2015/01/DSCF5002-1024x679.jpg")


    inputByIndexAndExtention()
    fetchImages()
    printImageListMarkdown()
