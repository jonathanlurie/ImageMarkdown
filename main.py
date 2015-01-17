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

import os


# list of images to build
_imgList = []


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
        bigStr = bigStr + "[![Picture description][" + imgId + "]][" + imgId + "]\n"
        # [![La photo 2][3]][4]

    # split
    bigStr = bigStr + "\n"

    # build the references at page bottom
    for i in range(0, len(_imgList)):
        #imgId = str(i+1)
        # the filename without extention is taken as link ID
        imgId = os.path.splitext(os.path.basename(_imgList[i]))[0]
        bigStr = bigStr + "  [" + imgId + "]" + ": " + _imgList[i] + "\n"




    print("\t\t OUTPUT")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n\n")

    print(bigStr)

    print("\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print("\t\t END OF OUTPUT")
    print("NOTE: this was automatically copied to your clipboard.")

    pyperclip.copy(bigStr)
    spam = pyperclip.paste()

if __name__ == "__main__":

    print("\n------------------------ ImageMarkdown -----------------------------------------\n")


    inputByIndexAndExtention()
    printImageListMarkdown()
