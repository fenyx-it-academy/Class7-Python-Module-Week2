# Class7-Python-Module-Week2

### 1.
Write a program that takes two inputs; one of them is a list and the other is a number, and returns the list obtained by shifting the elements in the list n places to the right (left) when n is positive (negative). Use wrap-around: if an element is shifted beyond the end of the list, then continue to shift starting at the beginning of the list.

```
Example
Inputs>>> [1, 2, 3, 4, 5], 2
Output>>> [4, 5, 1, 2, 3]
Inputs>>> [1, 2, 3, 4, 5], -2
Output>>> [3, 4, 5, 1, 2]
```


### 2.
Write a code snippet that inputs a sentence from the user, then uses a dictionary to summarize the number of occurrences of each letter. Ignore case, ignore blanks and assume the user does not enter any punctuation. Display a two-column table of the letters and their counts with the letters in sorted order.

```
Example
Input >>> "This is a sample text with several words This is more sample text with some different words"
Output >>>
[('a', 4), ('d', 3), ('e', 10), ('f', 2), ('h', 4), ('i', 7), ('l', 3), ('m', 4), ('n', 1), ('o', 4), ('p', 2), ('r', 5), ('s', 10), ('t', 9), ('v', 1), ('w', 4), ('x', 2)]
```


### 3.
Write a program that takes in two words as input and returns a list containing three elements, in the following order:
-		Shared letters between two words.
 	
-		Letters unique to word 1.
 	
-		Letters unique to word 2.

Each element of the output should have unique letters, and should be alphabetically sorted. Use set operations. The strings will always be in lowercase and will not contain any punctuation.

```
Example
Input1>>> "sharp"
Input2>>> "soap"
Output>>> ['aps', 'hr', 'o']
```

### 4.
A palindromical prime number is a prime number that reads the same when reversed. 
Write a function which returns the nearest palindromical prime number less than the multiplication of all the arguments.

```
Example
Input1>>>  some_function(2, 3, 4) 
Output1>>>  the nearest palindromical prime number less than 24
Input2>>> some_function(31, 77, 99)
Output2>>> the nearest palindromical prime number less than 236,313
```
