def hammingDistance(x, y):

    xor_result = x ^ y

    count = 0
    while xor_result:
        count += xor_result & 1
        xor_result >>= 1
    return count

# Example Usage:
print(hammingDistance(1, 4))  
print(hammingDistance(3, 5)) 