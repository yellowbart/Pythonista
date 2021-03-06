# Script posted at: http://n8henrie.com/2013/02/quickly-import-pythonista-scripts-via-textexpander-or-bookmarklet
# Script name: Import Pythonista Script from Clipboard

# I got help from here: http://twolivesleft.com/Codea/Talk/discussion/1652/what-others-do%3A-pythonista/p1
# I got help from here: http://www.macdrifter.com/2012/09/pythonista-trick-url-to-markdown.html

import clipboard
import urllib2
import editor
import os

url = clipboard.get()
scriptName = os.path.basename(url)
contents = urllib2.urlopen(url).read()
editor.make_new_file(scriptName[:-3], contents)
