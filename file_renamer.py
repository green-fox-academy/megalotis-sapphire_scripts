import os

def renamer (path):
        setFilename = "TextFile"
        dir = os.chdir(path)

        i = 0
        for filename in os.listdir(dir):         
                src = path + filename
                dst = setFilename + str(i) + ".txt"
                dst = path + dst 
                
                os.rename(src, dst) 
                i += 1
  
renamer('C:\\Users\\NEMETH\\Desktop\\rename\\')