def convert_to_indian_currency(num):
    num_str = str(num)
    n = len(num_str)
    if n <= 3:
        return num_str
    result = ""
    for i in range(n):
        if i % 3 == 0 and i != 0:
            result += ','
        result += num_str[n-i-1]
    return result[::-1]

# Example usage:
input_num = 5046799
output = convert_to_indian_currency(input_num)
print("Input:", input_num)
print("Output:", output)





