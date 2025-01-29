

my_dictionary = {
  "String": "A sequence of characters",
  "List": "A sequence of any item",
  "Dictionary": "A collection of keys mapped to values"
}


print("A String is:")
print("  " + my_dictionary["String"])

print("A List is:")
print("  " + my_dictionary["List"])

print("A Dictionary is:")
print("  " + my_dictionary["Dictionary"])


print(len(my_dictionary))

print(type(my_dictionary))
  
if type(my_dictionary) is str:
   print('Yes, string')
elif type(my_dictionary) is int:
  print('no')
elif type(my_dictionary) in [dict, list]:
  print('yes, it\'s a dictionary')



print("- - - -")
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(type(thisdict))



mydict = dict(name = "Beth", age = 36, country = "UK")
print(mydict)
name = mydict.get("name")
print(name)
mykeys = mydict.keys() # returns 'view' object and not a list 
print(mykeys)
convertedKeys = list(mykeys)
print(convertedKeys)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(car.values())
car["colour"] = "black"
print(car.values())


test_dict = {"a": 2, 'b': 5, "c" : 9}
# check if key exists 
if "b" in test_dict:
    print("Yes, b is a key")

# Loop through a dictionary - return value are keys of dict
for x in test_dict:
  print(x)

print(list(test_dict.keys()))
#1 converts to list beforehand is more memory-intensive
for x in list(test_dict.keys()):
   print('inside list => ', x)
#2
for x in test_dict.keys():
   print('with .keys() => ', x)



for key, value in list(test_dict.items()):
   print(key, value)

for key, value in test_dict.items():
   print(key, value)