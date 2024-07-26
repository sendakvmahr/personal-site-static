# figure out how to configure static site generator someday
import os
files = os.listdir(".")

to_replace = ("http://localhost/", "/")
while len(files):
	file = os.path.abspath(files.pop())
	if os.path.isdir(file):
		files += os.listdir(file)
	elif file[-5:] == ".html":
		with open(file, "r") as dfile:
			data = dfile.read()
		with open(file, "w") as dfile:
			dfile.write(data.replace(to_replace[0], to_replace[1]))

print(files)