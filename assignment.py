#1
def count_pairs(list, target_sum):
    count=0
    n=len(list)
    for num1 in range(0,n):
        for num2 in range(num1+1,n):
            if list[num1]+list[num2]==target_sum:
                count=count+1
    print(count)
list=[3,7,4,1,2,6]
count_pairs(list,10)

#2
def range(list1):
    list1.sort()
    n=len(list1)
    Range=list1[n-1]-list1[0]
    if Range<3:
        print("Range determination is not possible")
    else:
        print("Range is",Range,"(",list1[n-1],"-",list1[0],")")
list1=[1,4,5,6,7]
range(list1)

#3
import numpy as np
 
def power_of_matrix(matrix, m):
    return np.linalg.matrix_power(matrix, m)
 
n = int(input("Enter the matrix dimension:"))
matrix = np.random.randint(0,10,(n,n))
m = int(input("Enter the power of the matrix to be found:"))
result = power_of_matrix(matrix, m)
print(result)
    
#4
def String_occurrence(word):
    word = word.lower()  
    dict = {}
    for char in word:
        dict[char] = dict.get(char, 0) + 1
    max = 0
    max_char = []

    for j, k in dict.items():
        if k > max:
            max = k
            max_char = [j]
        elif k == max:
            max_char.append(j)

    chars_str = ", ".join([f"'{char}'" for char in max_char])
    print(f"Characters {chars_str} have the highest occurrence with {max} times.")    
word=input("Enter the String:")
String_occurrence(word)