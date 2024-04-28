a = input('')
fio = input('')
fiolist = fio.split()
newtext = a
for i in fiolist:
    newtext = newtext.replace(i, 'N')
print('')
print(newtext)