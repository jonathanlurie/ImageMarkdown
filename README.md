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
[![Picture description][1]][1]
[![Picture description][2]][2]
[![Picture description][3]][3]
[![Picture description][4]][4]
[![Picture description][5]][5]

  [1]: http://myBlog.com/wp-content/uploads/2015/01/myHolydays-11.jpg
  [2]: http://myBlog.com/wp-content/uploads/2015/01/myHolydays-12.jpg
  [3]: http://myBlog.com/wp-content/uploads/2015/01/myHolydays-13.jpg
  [4]: http://myBlog.com/wp-content/uploads/2015/01/myHolydays-14.jpg
  [5]: http://myBlog.com/wp-content/uploads/2015/01/myHolydays-15.jpg

```

**Note** This output is automatically copied to your clipboard.
