import sys, os

def renamer (path):
        dir = os.chdir(path)
        setFilename = "TextFile"
        i = 0
        
        if os.path.exists(path):
                for filename in os.listdir(dir):         
                        src = path + filename
                        dst = setFilename + str(i) + ".txt"
                        dst = path + dst 
              
                        os.rename(src, dst) 
                        i += 1
        else:
                print("Directory does not exist!")
        
renamer(sys.argv[1])
