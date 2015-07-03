import os
import sys
if(len(sys.argv) < 2):
    sys.exit("Enter the directory in which xib is present")
directoryToBeChecked = sys.argv[1]

for root,dirs,files in os.walk(directoryToBeChecked):
    for file in files:
        if (file.endswith(".xib") or file.endswith(".storyboard")):
            xibText = ""
            with open(os.path.join(root,file), 'r') as readFileHandler:
                xibText = readFileHandler.read()
                print(xibText)
            with open(os.path.join(root,file), 'w') as writeFileHandler:
                xibText = xibText.replace(".png","")
                writeFileHandler.write(xibText)


