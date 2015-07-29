#! /usr/bin/env python
# -*- coding:utf-8 -*-

import os

class Trie :
    
    def __init__ (self, directory='') :
        self.directory = directory

    def make (self, key, fname) :
        cwd = os.getcwd()
        if self.directory == '' :
            pass
        else :
            if not os.path.exists(self.directory) :
                os.mkdir(self.directory)
            os.chdir(self.directory)
        for char in key :
            if not os.path.exists(char) :
                os.mkdir(char)
            os.chdir(char)
        with open(fname, 'w') as f :
            pass
        dpath = os.getcwd()
        os.chdir(cwd)
        if dpath.endswith('/') :
            return dpath + fname
        else :
            return dpath + '/' + fname

