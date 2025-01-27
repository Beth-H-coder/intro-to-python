
my_name = "Kay"
print(my_name)


your_name = "Beth anne"
print(your_name)
print(type(your_name)) 
print(isinstance(your_name, str)) 
print(isinstance(your_name, float))

# -- String Methods -- 
print(your_name.upper())
print(your_name.count('e'))
print(your_name.find('h'))
print(your_name.index('h'))
print(your_name.replace('th', 'n'))
print(your_name.title())
print(list(your_name)) # puts letters into a list 

sentence = "Hello world"
words = sentence.split()
print(words)  


# is to break a sentence into words based on spaces.