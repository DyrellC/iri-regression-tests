'''
Created on Jun 27, 2018

@author: d
'''

class FileEditing():
    
    def make_file(self,file_name):
        try:
            open(file_name,"w+") 
        except:
            print("Make File Failed, file may already exist")
            
    def close_file(self,file_name):
        try:
            file_name.close()
        except:
            print("Close File Failed")

    def write_to_file(self,file,content):
        try:
            file.write(content)
        except:
            print("Write To File Failed")
        
    def read_from_file(self,file):
        try:
            file.readlines()
        except: 
            print("Read Lines Failed")
        
        
        