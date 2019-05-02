import sys, os

def renamer (path):
        path = sys.argv[1]
        dir = os.chdir(path)
        setFilename = "TextFile"

        i = 0
        for filename in os.listdir(dir):         
                src = path + filename
                dst = setFilename + str(i) + ".txt"
                dst = path + dst 
                
                os.rename(src, dst) 
                i += 1
  
renamer(sys.argv[1])