import os
import json
from os import listdir, stat
from os.path import isfile, isdir, join


class FileStats(object):
    def __init__(self, fpath, fsize, fmod):
        self.filePath = fpath
        self.fileSize = fsize
        self.lastModified = fmod




if __name__ == "__main__":
    folderPath = "D:\PythonTraining\day1"
    files = filter(lambda f: isfile(join(folderPath, f)), os.listdir(folderPath))

    for file in files:
        s = stat(folderPath + '\\' + file)
        fObj = FileStats(folderPath + '\\' + file, s.st_size, s.st_mtime)
        print(json.dumps(fObj.__dict__))
