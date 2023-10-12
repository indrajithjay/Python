# demonstrate the use of re class
import re  # import re class

test_string = "Introduction to python programming"  # initialise the test string
if re.search("python", test_string):  # regular expression - scan the string for a match.
    print("Found a match")  # printing results if the test case is success
else:  # statement body for unmatched expresions
    print("No match")  # printing results if the condition re.search is not succeeded
#######################################################################################
x = re.search("I", test_string)  # scan the string for the character I
print(x)  # print the position of the string
print("The first  character is located in position:", x.start())  # print the position of the string
#########################################################################################
#
#
y = re.sub("\s", "|", test_string)  # Replace all white-space characters in "test_string" with '|'
print(y)  # print the result string
#
string_1 = "Python is a high-level general-purpose programming language"  # initialise new string with the name string_1
z = re.findall('i', string_1)  # using the re.findll() function to return a list containing every occurrence of "i":
print(z)  # print the result
txt = re.sub("i", "", string_1)  # substitute every occurences of "i" with a blank space ("")
print(txt)  # print the resulting string
print(string_1)  # print the original string with all the occurances of the substitute value
#
#
txt = "Irrelevant usage of random words to test the condition "  # declare a string "txt"
x = re.split("e",
             txt)  # using the re.split() function for splitting the string into two parts by taking the '&' symbol as an indicator
print(x)  # print the resulting string
print(x[0])  # print the string from the array position x[0]
print(x[1])  # print the string from the array position x[1]
print(x[2])  # print the string from the array position x[2]
print(x[3])  # print the string from the array position x[3]
#
#
txt_subs = "SplIt the strIng Into array"  # new string
txt = re.sub("I", "i", txt_subs)  # usng the re.sub() function to replace characters
print(txt)  # print the resulting string
print(txt_subs)  # print the original string
