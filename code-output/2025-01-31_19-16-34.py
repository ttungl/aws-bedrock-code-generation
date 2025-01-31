 Here is Python code to reverse a string using a function:

```python
def reverse_string(input_str):
  reversed_str = ""
  for i in range(len(input_str)-1, -1, -1):
    reversed_str += input_str[i]
  return reversed_str

my_string = "Hello World"
print(reverse_string(my_string))
```

The key steps are:

- Define a function called reverse_string that takes the input string as a parameter 
- Initialize an empty string variable to hold the reversed string
- Loop through the input string in reverse order, from the end to the start
- Append each character to the reversed string variable
- Return the reversed string 

To test it:

- Define a sample string 
- Call the reverse_string function, passing the string as the argument
- Print the result returned by the function

This will reverse the input string and print out the reversed version.