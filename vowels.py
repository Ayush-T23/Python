def count_vowels(input_string):
    vowels = {'a', 'e', 'i', 'o', 'u','A','E','I','O','U'}
    input_string = input_string.lower()
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

user_input = input("Enter a string: ")
vowel_count = count_vowels(user_input)
print("Total number of vowels in the string:", vowel_count)
