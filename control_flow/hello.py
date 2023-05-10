#Write a Python program that takes a list of strings as input and outputs the number of times 
#each string appears in the list, using a dictionary and conditional statements.
def check_appearance(strings):
    result = {}
    for string in strings:
        if string in result:
            result[string] +=1
        else:
            result[string] = 1
        return result

strings = ['emmie','joan','paul','emmie','john','emmie']
print(check_appearance(strings))

#Write a Python program that takes a list of numbers as input and outputs the median of the numbers 
numbers = [10,60,50,70,40]
numbers.sort()
length = len(numbers) 
if length %2== 0 :
    mediun =(numbers[(length)//2])
else:mediun = numbers[(length -1)//2]
print(mediun)

#Write a Python program that takes a list of numbers as input and outputs the second largest number in the list using conditional 
# statements and a for loop.
list =[1,4,5,8,9,7.2,3]
new_list =set(list)
new_list.remove(max(new_list))
print(max(new_list))

#Write a Python program that takes a year as input and determines if it is a leap year.
year = 2020
if (year%4==0)and(year % 100 == 0):
    print("{year}is leap")
elif(year %4 == 0)and(year %100 !=0):
    print("{year}is leap year")
else:
    print("{year}notleap")



#Write a Python program that takes a string as input and checks if it is a palindrome 
# (reads the same forwards and backwards), ignoring spaces and punctuation.
def palindrome(string):
    return string == string[::-1]
string ="bob" 
answer = palindrome(string)
if answer:
    print("is palindrome")
else:
    print("not palindrome")