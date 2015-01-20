# ImageMarkdown
Helper for publishing images using Markdown plugin for Wordpress

# What is it?

This code takes a list of image url and build a Markdown compliant list of them, with embeded link to themselves.

This intents to facilitate the image integration when using a Markdown plugin in Wordpress. As long as the images are already uploaded to your server.

Requirements:
- The pictures must all be in the same folder (on the web)
- They must be named in a contiguous sequence from M to N (where N is bigger than M)
- They can have a prefix, like DSC_ if they all have the same
- You must specify the extention, like .jpg

# Plateform

This is supposed to be crossed plateform, at least for the main.py file.
However, the file ImageMarkdown.sh will work only on OSX and Linux, but since it is just a double-click shortcut to launch python *main.py*, it will not miss so much to Windows users.

# Launch it

On OSX or Linux, just double click on *ImageMarkdown.sh*, then follow the instructions.
On Windows, launch *python main.py*


# Exemple

Here is a list of images you just uploaded to you server, it was done on January 2015:

http://myBlog.com/wp-content/uploads/2015/01/myHolydays-11.jpg

http://myurl.com/wp-content/uploads/2015/01/myHolydays-12.jpg

http://myurl.com/wp-content/uploads/2015/01/myHolydays-13.jpg

http://myurl.com/wp-content/uploads/2015/01/myHolydays-14.jpg

http://myurl.com/wp-content/uploads/2015/01/myHolydays-15.jpg

### The folder URL is:
http://myBlog.com/wp-content/uploads/2015/01/

### The prefix is:
myHolydays-

### The first index is:
11

### The last index is:
15

### The file extention is:
.jpg

### The Alternative text

The *alternative text* will be used in case the picture could not be loaded. In addition, it will also be used for the image title. For exemple, you can type:
My amazing Holidays


### The Output is:

```
[![My amazing Holidays][myHolydays-11]][myHolydays-11]
[![My amazing Holidays][myHolydays-12]][myHolydays-12]
[![My amazing Holidays][myHolydays-13]][myHolydays-13]
[![My amazing Holidays][myHolydays-14]][myHolydays-14]
[![My amazing Holidays][myHolydays-15]][myHolydays-15]

  [myHolydays-11]: http://myBlog.com/wp-content/uploads/2015/01/myHolydays-11.jpg "My amazing Holidays"
  [myHolydays-12]: http://myBlog.com/wp-content/uploads/2015/01/myHolydays-12.jpg "My amazing Holidays"
  [myHolydays-13]: http://myBlog.com/wp-content/uploads/2015/01/myHolydays-13.jpg "My amazing Holidays"
  [myHolydays-14]: http://myBlog.com/wp-content/uploads/2015/01/myHolydays-14.jpg "My amazing Holidays"
  [myHolydays-15]: http://myBlog.com/wp-content/uploads/2015/01/myHolydays-15.jpg "My amazing Holidays"

```

As you can see, the ID within square bracket is the filename without extension.
It could be an incremental integer number, but some editors do it by default when you add a link, so using the filename won't mess with automatic addings.

Lets describe a bit the output:
```
[![My amazing Holidays][myHolydays-11]][myHolydays-11]
[![My amazing Holidays][myHolydays-12]][myHolydays-12]
[![My amazing Holidays][myHolydays-13]][myHolydays-13]
[![My amazing Holidays][myHolydays-14]][myHolydays-14]
[![My amazing Holidays][myHolydays-15]][myHolydays-15]
```

This part will display 5 pictures, with the *alternative text* "My amazing Holidays". Actually,
```
[My amazing Holidays][myHolydays-11]
```
would be enough to display an image, but, we want it clickable with a link to itself (to display it bigger, with Easy Fancy Box for example), so it is surrounded with another layer of square bracket.


And the second part:
```
[myHolydays-11]: http://myBlog.com/wp-content/uploads/2015/01/myHolydays-11.jpg "My amazing Holidays"
[myHolydays-12]: http://myBlog.com/wp-content/uploads/2015/01/myHolydays-12.jpg "My amazing Holidays"
[myHolydays-13]: http://myBlog.com/wp-content/uploads/2015/01/myHolydays-13.jpg "My amazing Holidays"
[myHolydays-14]: http://myBlog.com/wp-content/uploads/2015/01/myHolydays-14.jpg "My amazing Holidays"
[myHolydays-15]: http://myBlog.com/wp-content/uploads/2015/01/myHolydays-15.jpg "My amazing Holidays"
```

Is the list of reference where:
```
[myHolydays-11]:

```
is the ID of the picture.

```
http://myBlog.com/wp-content/uploads/2015/01/myHolydays-11.jpg
```
Is the target.

And
```
"My amazing Holidays"

```
is the picture title.


**Note** This output is automatically copied to your clipboard.

## TODO
A **lot** of things, among which:

- update Readme about exif
- add a local sync folder for faster exif writing (maybe with a setting file)
- Add a yes/no choice for writing exif
- clean the terminal screen at launching
