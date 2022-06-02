import fileinput

# with fileinput.input(files="T", encoding="utf8", inplace=True) as f:
#     for line in f:
#         print(fileinput.filelineno(), line)


for line in fileinput.input("T", inplace=True):
    if line.find("FILE_NAME="):
        temp = line.split("=")[1]
        line = line.replace(temp, "\"" + "悼亡" + "\"")
        print('{}'.format(line), end='')
