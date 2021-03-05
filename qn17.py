givn_char = input("input character: ")
str = input("input string: ")

starts_with_char = list(filter(lambda x:x.startswith(givn_char),str))
not_start = list(filter(lambda x:not x.startswith(givn_char),str))
if starts_with_char:
   print(f"The string with given_char {givn_char} is: {str}")
else:
 print(f"The string with given_char {givn_char} is not in string: {str}")

