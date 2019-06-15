flintstones = ['fred','wilma','pebbles','dino']

#title function mean first letter in name is uppercase
newNames = []
for name in flintstones:
    if name == 'dino':
        newNames.append(name.title())

print(newNames)

#duplicates for loop in 1 line instead of 3
#python users call this List Comprehension

#do name.title operation for each name in the flintstone list ==
#1st letter in is changed to uppercase

#do name.upper operation == entire name is changed to uppercase
#dump result in newNames (this is title case)
newNames =[name.title () for name in flintstones if name == 'dino']

print(newNames)