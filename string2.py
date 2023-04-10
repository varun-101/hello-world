parrot="Norwegian Blue"


print(parrot)
#indexing
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()

print(parrot[-11])
print(parrot[-1])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()
#slicing
print(parrot[3:5]) #we
print(parrot[-11:-9]) #we
print(parrot[0:9]) #Norwegian
print(parrot[-14:-5])
print(parrot[:9])  #Norwegian

print(parrot[10:15])
print(parrot[10:])

print(parrot[:6] + parrot[6:])
print(parrot[:])

print()

#slice with steps

print(parrot[0:6:2]) #Nre
print(parrot[0:6:3]) #Nw

number ="9,223,113,134,422,414,144"
print(number[1::4])