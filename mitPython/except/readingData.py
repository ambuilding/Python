# control input
data = []

file_name = input("Provide a name of a file of data ")

try:
    fh = open(file_name, 'r')
#    print(type(fh))
except IOError:
    print('cannot open', file_name)
else:
    for new in fh:
        if new != '\n':
            addIt = new[:-1].split(',') #remove trailing \n
            print(addIt)
            data.append(addIt)
    fh.close() # close file even if fail
finally:
    print("hi")