"""Write a python program to add items from another set to the current set. thisset =
{"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}"""
thisset ={"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}
for a in thisset:
    secondset.add(a)
print(secondset)    
