# -*- coding: utf-8 -*-
__author__ = 'lololol'

# def firstRead( parameters ):
#    "function_docstring"
#    function_suite
#    return [expression]

f = open('try.csv', 'r')
motherFile = f.read()
# print motherFile.read().index(u'\u4E3B')
# print motherFile.read().index('主  文')
# print motherFile.read().index('187')
# print '雨'
rawFile = motherFile[motherFile.index('主  文'):]
rawFile = rawFile.replace("\r\n        ", "");
rawFile = rawFile.replace("\r\n       ", "");
rawFile = rawFile.replace("\r\n      ", "");
rawFile = rawFile.replace("\r\n     ", "");
rawFile = rawFile.replace("\r\n    ", "");
rawFile = rawFile.replace("\r\n   ", "");
rawFile = rawFile.replace("\r\n  ", "");
rawFile = rawFile.replace("\r\n ", "");
childFile = open('child.csv', 'w')
childFile.write(rawFile)
childFile.close()
f.close()
