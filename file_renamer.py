import os

def renamer (path):
        #path = 'C:\\Users\\NEMETH\\Desktop\\rename\\'
        dir = os.chdir(path)

        i = 0
        for filename in os.listdir(dir):         
                src = path + filename
                dst = "Text" + str(i) + ".txt"
                dst = path + dst 
                
                os.rename(src, dst) 
                i += 1
  
renamer('C:\\Users\\NEMETH\\Desktop\\rename\\')