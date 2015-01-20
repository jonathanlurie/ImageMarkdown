

import exifread

#path_name = "/Users/jonathanlurie/Documents/photos/photosExport/DSC7107.jpg"
path_name = "/Users/jonathanlurie/Documents/photos/photosExport/potw/_NIK3518.jpg"
#path_name = "/Users/jonathanlurie/Documents/photos/photosExport/potw/DSCF5002.jpg"

# Open image file for reading (binary mode)
f = open(path_name, 'rb')

# Return Exif tags
tags = exifread.process_file(f)

#for tag in tags:
#    print(str(tag) + "\t" + str(tags[tag]))


print("\n")

ms = ""

# camera model
if('Image Model' in tags.keys() ):
    ms = ms + u"\U0001F300" + " **" + str(tags["Image Model"]) + "** "

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


print(ms)
