import nltk
import re
import os
import urllib
import  errno
from urllib import request
from os.path import expanduser

def getSentenceFile(rawFile):
    # If punkt model is not present locally. Use nltk.download() and in the popup that appears, go to Models->punkt and Download it
    home = expanduser("~")
    projectFolder=os.path.join(home,".EmotionGraph")
    make_sure_path_exists(projectFolder)
    filepath=os.path.join(projectFolder,os.path.basename(os.path.normpath(rawFile)))
    f = open(filepath, "w")
    if urllib.parse.urlsplit(rawFile).scheme in ['http','https']:
        response = request.urlopen(rawFile)
        rawtext = response.read().decode('utf8')
    else:
        rawtext = open(rawFile, "r").read()
    for sentence in nltk.sent_tokenize(rawtext):
        line = re.sub(r"[\r\n]+", "", sentence)
        if line:
            f.write(line + "\n")
    f.close()
    return filepath

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise