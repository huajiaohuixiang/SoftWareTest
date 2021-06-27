import pandas as pd;
import project.ComputerSales;
import os
import datetime



class JavaProjectService(object):
    def getAllJavaPRoject(self):
        return os.listdir('./JavaProject')

    def getAllProjectFile(self,name):
        return self.recGetFile(self,'./JavaProject/'+name)

    def getLinxiServer(self):
        return self.recGetFile(self,'./JavaProject/lingxi-server')
    

    def recGetFile(self,path):
        result=[]
        for file in os.listdir(path):
            temp={
                
            }
            temp["label"]=file
            file_path = os.path.join(path, file)  
            if os.path.isdir(file_path):  
                if file=='.idea' or file=='.git':
                    continue 
                else:
                    temp["children"]=self.recGetFile(self,file_path)  
            result.append(temp)
        return result