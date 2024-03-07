#1
def count_pairs(list, target_sum):
    count=0          #variable to store the number of pairs that satisifes the condition
    n=len(list)        #length of the list
    for num1 in range(0,n):
        for num2 in range(num1+1,n):
            if list[num1]+list[num2]==target_sum:       #checking condition if pair sum equals target
                count=count+1
    print(count)
list=[3,7,4,1,2,6]
count_pairs(list,10)

#2
def range(list1):
    list1.sort()     #sort the list
    n=len(list1)
    Range=list1[n-1]-list1[0]     #calculation of range
    if Range<3:        #to check if the number of elements is less than 3
        print("Range determination is not possible")
    else:
        print("Range is",Range,"(",list1[n-1],"-",list1[0],")")
list1=[1,4,5,6,7]
range(list1)

#3
import numpy as np
 
def power_of_matrix(matrix, m):
    return np.linalg.matrix_power(matrix, m)           #numpy matrix power function
 
n = int(input("Enter the matrix dimension:"))
matrix = np.random.randint(0,10,(n,n))       #creation of random matrix of dimension n*n
m = int(input("Enter the power of the matrix to be found:"))
result = power_of_matrix(matrix, m)          #function call
print(result)
    
#4
def String_occurrence(word):
    word = word.lower()     #lowercase conversion to consider case-insensivity
    char_count = {}         #dictionary to store character count
    for char in word:
        char_count[char] = char_count.get(char, 0) + 1            #counting the occurrence of the character
    max = 0
    max_char = []       #list to store characters if there are 2 or more have same maximum frequency

    for j, k in char_count.items():
        if k > max:
            max = k     #if the current character is higher than the previous maximum,then maximum is updates to the current character frequency
            max_char = [j]      #character update
        elif k == max:
            max_char.append(j)      #checking if there is any character with frequency same as the maximum

    chars_str = ", ".join([f"'{char}'" for char in max_char])
    print(f"Characters {chars_str} have the highest occurrence with {max} times.")    
word=input("Enter the String:")
String_occurrence(word)