# visualize a directory
import os

# produces a list of 3-tuples
dir = os.walk(".") 

structure = {}
for p in dir:
    for entry in p:
        top_folder = p[0]
        folders = p[1]
        files = p[2]
        structure[top_folder] = {
            "Folders": folders,
            "Files": files
        }

for top_folder, content in structure.items():
    print(f"Top Folder: {top_folder}")
    for folder, files in content.items():
        print(f"    Folders: {folder}")
        print(f"        Files: {files}")
