def encode_string(str1):
    encoded = ''
    ctr = 1
    last_char = str1[0]

    for i in range(1, len(str1)):

        if last_char == str1[i]:
            ctr += 1

        else:
            encoded += str(ctr) + last_char
            ctr = 0
            last_char = str1[i]
            ctr += 1
    encoded += str(ctr) + last_char
    return encoded


print(encode_string("AAAABBBCCDAAA"))
print(encode_string("PHP"))
print(encode_string("AAAABBBCCCDAABDAAAAC"))
