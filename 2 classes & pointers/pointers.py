num1 = 11
num2 = num1

print(f"num 1: {num1}")
print(f"num 2: {num2}")

print(f"mem address of num1: {id(num1)}")
print(f"mem address of num2: {id(num2)}")

num2 = 22

print(f"num 1: {num1}")
print(f"num 2: {num2}")

# immutable
print(f"mem address of num1: {id(num1)}")
print(f"mem address of num2: {id(num2)}")

dict1 = {
    'value':1
}

dict2 = dict1

print(f"dict 1: {dict1}")
print(f"dict 2: {dict2}")

print(f"mem address of dict1: {id(dict1)}")
print(f"mem address of dict2: {id(dict2)}")
# mutable
dict2['value']=22

print(f"dict 1: {dict1}")
print(f"dict 2: {dict2}")

print(f"mem address of dict1: {id(dict1)}")
print(f"mem address of dict2: {id(dict2)}")
