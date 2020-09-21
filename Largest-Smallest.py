largest = None 
smallest = None

while True:
    num = input("Enter a number: ")
    
    if num == "done" : break # if "done" is introduced the program end.
    try: 
        var1 = int(num)
            
    except:
        print("Invalid input")
        continue
    
    if smallest is None:
        smallest = var1
    elif var1 < smallest:
        smallest = var1
    if largest is None:
        largest = var1
    elif var1 > largest:
        largest = var1

print("Maximum is", largest)
print("Minimum is", smallest)
