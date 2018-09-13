vowels = ["a", "e", "i", "o", "u"]
string = input("Enter a string:")

contained = [x for x in vowels if x in string]
contained2 = tuple(item for item in contained)
# separator = ''
# output = separator.join(contained2)
# output2 = tuple(output)

if contained:
    print("The vowels are" ,contained2)
    # print(vowels.count(contained2))
else:
    print("no vowels contained")



