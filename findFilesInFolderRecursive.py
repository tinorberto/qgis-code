import os

def listfiles(folder):
    for root, folders, files in os.walk(folder):
        for filename in folders + files:
            yield os.path.join(root, filename)
            
for filename in listfiles('D:\\resultado_croqui\\938036_012_0015'):
    print filename