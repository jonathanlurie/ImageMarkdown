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


### The Output is:

```
[![Picture description][myHolydays-11]][myHolydays-11]
[![Picture description][myHolydays-12]][myHolydays-12]
[![Picture description][myHolydays-13]][myHolydays-13]
[![Picture description][myHolydays-14]][myHolydays-14]
[![Picture description][myHolydays-15]][myHolydays-15]

  [myHolydays-11]: http://myBlog.com/wp-content/uploads/2015/01/myHolydays-11.jpg
  [myHolydays-12]: http://myBlog.com/wp-content/uploads/2015/01/myHolydays-12.jpg
  [myHolydays-13]: http://myBlog.com/wp-content/uploads/2015/01/myHolydays-13.jpg
  [myHolydays-14]: http://myBlog.com/wp-content/uploads/2015/01/myHolydays-14.jpg
  [myHolydays-15]: http://myBlog.com/wp-content/uploads/2015/01/myHolydays-15.jpg

```

As you can see, the ID within square bracket is the filename without extension.
It could be an incremental integer number, but some editors do it by default when you add a link, so using the filename won't mess with automatic addings.

**Note** This output is automatically copied to your clipboard.
