# Countdown
def countdown(num):
    result = []
    for i in range(num, -1, -1):
        result.append(i)
    return result

print(countdown(10))

# Print and Return
def print_and_return(num1):
    print(num1[0])
    return num1[1]

num1 = [1,7]
print(num1)

# First Plus Length
def first_plus_length(value):
    return value[0] + len(value)

list = [1,2,3,4,5]
result = first_plus_length(list)
print(result)

# Values Greater than Second
