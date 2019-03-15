import os
Path = "Path to the Files"
filelist = os.listdir(Path)
for i in filelist:
    if i.endswith(".txt"):  # You could also add "and i.startswith('f')
        with open(Path + i, 'a') as f:
        	f.write("%s" % (i))
        	f.close()
        	
