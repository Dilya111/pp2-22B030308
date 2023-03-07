import os
m=os.path.abspath(input())

dir = open("dir.txt","x")
dir.write("list only directories:\n")

dir.close()

file = open("file.txt", "x")
file.write("only files:\n")
file.close()

file_dir = open("file_dir.txt","x")
file_dir.write("all directories and files:\n")
file_dir.close()