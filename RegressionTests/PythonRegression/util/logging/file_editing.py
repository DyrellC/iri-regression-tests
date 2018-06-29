'''
Created on Jun 27, 2018

@author: d
'''
import os


class FileEditing():

    def write_to_file(self,file,content):
        #try:
        file.write(content)
        #except:
        #   print("Write To File Failed")
        
    def read_from_file(self,file):
        #try:
        lines = file.readline() 
        print(lines)
        return lines
        #except: 
         #   print("Read Lines Failed")
        
        
        