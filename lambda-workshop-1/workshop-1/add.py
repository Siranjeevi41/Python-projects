# Regular function
def add(x, y):
    return x + y

# Equivalent lambda function
add_lambda = lambda x, y: x + y

# Using both
result_function = add(3, 5)
result_lambda = add_lambda(3, 5)

print(result_function)  # Output: 8
print(result_lambda)    # Output: 8
