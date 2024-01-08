def is_letter(char):
    return 'a' <= char <= 'z' or 'A' <= char <= 'Z'

def stringchallenge(s):
    result = ""
    capitalize_next = False

    for char in s:
        if is_letter(char):
            if capitalize_next:
                result += char.upper()
                capitalize_next = False
            else:
                result += char.lower()
        else:
            capitalize_next = True

    return result

# Example usage:
input_string = "BOB loves- coding"
camel_case_string = stringchallenge(input_string)
print(camel_case_string)




