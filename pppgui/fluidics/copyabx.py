import shutil
import os
srcs = '/home/othman/PycharmProjects/GitStuff/OC-playgroung/pppgui/fluidics/testkfolder/folderlevel1' # kartik change this to the files you want to move
dsts = '/home/othman/PycharmProjects/GitStuff/OC-playgroung/pppgui/fluidics' # kartik change this to the folder you want things to go
for root, subdirs, files in os.walk(srcs):
    for file in files:
        path = os.path.join(root, file)
        shutil.copyfile(path, os.path.join(dsts, os.path.relpath(path, srcs)))
