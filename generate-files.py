#!/usr/bin/python3
index_path = 'styles.styl'
index_content = ''

for i in range(1, 3000):
    file_path = 'src/file-' + str(i) + '.styl'
    file = open(file_path, 'w')
    file_content = ".class-" + str(i) + "\n\tbackground: white"
    file.write(file_content)
    file.close()

    index_content += "\n@import '" + file_path + "'"

index = open(index_path, 'w')
index.write(index_content)
index.close()
