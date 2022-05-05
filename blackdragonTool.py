import os
import glob
from tqdm import tqdm     # library for the loading bar

print(""" 
┌───────────────────┬───────────────────────┐
│ .blackdragon Tool │ removing header bytes │  by Zabz
└───────────────────┴───────────────────────┘     """)

files = glob.glob("**/*.blackdragon",recursive=True)

output_directory = "_RIP"

print(len(files),"Files found")

for i in tqdm(files):
    with open(i, 'rb') as f:
        s = f.read(200) # read the first 200 bytes as string
        position = s.find(b'UnityFS')

        f.seek(0) # reset pointer to the beginning
        f.seek(position) # go to the position
        filename = i[:-12] # filename without .blackdragon
        filepath = '\\'.join(i.split('\\')[:-1]) # all the subfolders
        #print(filepath)
        #print(type(filepath))

        if not os.path.exists(output_directory + "\\" + filepath):
            os.makedirs(output_directory + "\\" + filepath)

        with open(output_directory + "\\" + filename +'.UnityFS', 'wb') as outFile:
            outFile.write(f.read())

input("saved results under: " + output_directory + " \nPress anything to exit")
