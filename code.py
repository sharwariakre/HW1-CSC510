def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

input_str = "hello"
result = reverse_string(input_str)

print("Original string:", input_str)
print("Reversed string:", result)
