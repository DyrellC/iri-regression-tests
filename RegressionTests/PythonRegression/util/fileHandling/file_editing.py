'''
Created on Jun 27, 2018

@author: d
'''
import os


class FileEditing():
    
    def make_file(self,file_name):
        return open(file_name,"w+")
            
    def open_file_read(self,file):
        return open(file,"r")    
    
    
    def close_file(self,file_name):
        try:
            file_name.close()
        except:
            print("Close File Failed")


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
        
        
        