import os

path = os.getcwd()
print(f"Files: {[file for file in os.listdir(path) if os.path.isfile(file)]}, directories: {[director for director in os.listdir(path) if os.path.isdir(director)]} all elements are: {os.listdir(path)}")