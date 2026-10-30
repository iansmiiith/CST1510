first_name = input("Enter your first name(text): ")
last_name = input("Enter your last name(text): ")
marks = float(input("Enter your marks: "))

def marks(value, limit=100):
    if value >= 100:
        return "OVER LIMIT"
    elif value >= limit:
        return "WARNING"
    else:
        return "OK"
    
print(first_name, last_name, marks)

    
