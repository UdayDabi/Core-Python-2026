import shutil

source = "C:/Users/udayd/OneDrive/Desktop/IO/Dog.jpg";
target = "C:/Users/udayd/OneDrive/Desktop/Op/Dogs.jpg";

shutil.copyfile(source, target)
print(source + " is copied to " + target)
