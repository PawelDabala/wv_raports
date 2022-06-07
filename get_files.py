import os

# folder path
dir_path = r'attachments'

# list to store files
res = []
# Iterate directory
for file in os.listdir(dir_path):
    # check only text files
    if file.endswith('.csv'):
        res.append(file)

print(res)