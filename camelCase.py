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

# Example usag:
input_string = "BOB loves- coding"
camel_case_string = stringchallenge(input_string)
print(camel_case_string)



# function CamelCase(str) {
#   return str
#     .toLowerCase()
#     .replace(/[^\w]+(.)/g, (ltr) => ltr.toUpperCase())
#     .replace(/[^a-zA-Z]/g, '');
# }
# // keep this function call here 
# console.log(CamelCase("cats AND*Dogs-are Awesome"));
# console.log(CamelCase("a b c d-e-f%g"));


def is_letter(char):
    return 'a'<= char <= 'z' or 'A' <= char <= 'Z'

def camelCase(s):
    result=''
    capitalize_next=False

    for char in s:
        if is_letter(char):
            if capitalize_next:
                result+=char.upper()
                capitalize_next=False
            else:
                result+=char.lower()
        else:
            capitalize_next=True

    return result                  

input_string = "BOB loves- coding"
camel_case_string=camelCase(input_string)
print(camel_case_string)