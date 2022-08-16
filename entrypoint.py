import os

print(os.getcwd())
# print parent directory contents
print(os.listdir('..'))
print(os.listdir())


# print current directory contents
print(os.listdir('/github/workspace/'))
#print(os.listdir('/home/runner/work/'))

print(os.listdir('/github/home'))
print(os.listdir('/github/workflow'))

