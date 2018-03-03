import os, shutil

notdeletesplittext = [".h", ".cpp", ".sln"]
cleanupdirname = [".vs", "Debug", "Release", "x64"]

def cleanSingleLayerFilesPath(nowpath):
    files = os.listdir(nowpath)
    for file in files:
        nownewpath = os.path.join(nowpath, file)
        # if os.path.isfile(nownewpath):
        #     if os.path.splitext(nownewpath) not in notdeletesplittext:
        #         os.remove(nownewpath)
        if os.path.isdir(nownewpath):
            if file in cleanupdirname:
                print("deleting: ", nownewpath)
                shutil.rmtree(nownewpath)
            else:
                cleanSingleLayerFilesPath(nownewpath)


path = input("Please input the path you want to clean the vs path:  ")
print("You chose the path: ", path)
if os.path.exists(path) and os.path.isdir(path):
    print("scanning...")
    cleanSingleLayerFilesPath(path)
else:
    print("Error!")