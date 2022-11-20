#..........Variables and Types..........
print("..........Variables and Types..........")

# To define a Integer or floating number
int = 5.3
print(int)
int = float(5)
print(int)

# Normal calculation
x = -3
y = 4
sum = x + y
print(sum)

# Strings are defined either with a single quote or a double quotes
mystring1 = 'Hello'
print(mystring1)
mystring2 = "World"
print(mystring1)
hw = mystring1 + " " + mystring2
print(hw)

# But using double quotes makes it easy to include apostrophes
string = "Please Don't make a noise"
print(string)

# Assignments can be done on more than one variable on the same line
a, b, c = 7, 9, 86
print(a + b + c)
d, e, f = 100, "bar", "bolechi"
print(d, e, f)

#..........Lists..........
print("..........Lists..........")

newlist = []
newlist.append(5)
newlist.append(6)
newlist.append(7)
print(newlist[0])
print(newlist[1])
print(newlist[2])

# prints out 1,2,3 together
for x in newlist:
  print(x)

mylist = [1,2,3]
print(mylist[2])

#List exercise
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

second_name = names[1]

numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)


#..........Basic Operators..........
print("..........Basic Operators..........")

#Arithmetic Operators
number = 1 + 2 * 3 / 4.0
print(number)

modulo = 26 % 5
print(modulo)

squred = 5 ** 2
cubed = 3 ** 3
print(squred,"and", cubed)

#Using Operators with Strings
Loveu = "LoveYou" * 10
print(Loveu)

#Using Operators with Lists
even_numbers = [2,4,6,8,10]
odd_numbers = [1,3,5,7,9]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

#multiplication operator
print([5,7,8] * 3)

#Operators exercise
x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

#..........String Formatting..........
print("..........String Formatting..........")

name = "Islam" #tuple (a fixed size list)
country = "Bangladesh"
age = 30
print("Mydul %s is from %s. And age %d" % (name, country, age)) #two or more argument, use a tuple (parentheses)

mylist = [1,2,3,6,7]
print("A list: %s" % mylist) #repr method of that object is formatted as the string

#Note: %s - String, %d - Integers, %f - Floating numbers, %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot. %x/%X - Integers in hex representation (lowercase/uppercase)

#String Formatting Exercise
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s"
print(format_string % data)

#..........Basic String Operations..........
print("..........Basic String Operations..........")

astring = "Mydul Islam"
print(astring,"Lenth of String is:", len(astring)) #define lenght using len

print(astring.index("s")) #define location of s using index

print(astring.count("l")) #Count number of l using count

print(astring[6:10]) #prints a slice of the string
print(astring[6:10:3]) #The general form is [start:stop:step]
print(astring[-3]) #-3 means 3rd character from the end

print(astring[::-1]) #There is no function like strrev in C to reverse a string. But we can easily reverse a string like this

print(astring.upper()) #For uppercase 
print(astring.lower()) #For lowercase

#Check the string starts with something or ends with something
print(astring.startswith("Mydul"))
print(astring.endswith("Hossen"))

#splits the string
split = astring.split(" ")
print(split)

#String Exercise
#My choise was : s = "Hey thera! what shou"
#Solutions will be: s = "Strings are awesome!"

s = "Hey there! what should this string be?"

# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))
