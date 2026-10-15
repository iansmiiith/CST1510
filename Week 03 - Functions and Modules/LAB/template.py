"""
RECORD CHECK  -  my version
===========================

Name  :Ian Smith Ochieng
Lane  :IT
Date  :10/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS

def status_of(percent, warning_at=90):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"
def check(value, limit):
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent # This returns the value used in the code back to the code

def print_report(label, value, limit, difference, percent, status):
    print("=" * 34)
    print(f"RECORD CHECK - {label}")
    print(("=" * 34))
    print(f"{'used':<10}: {value}")
    print(f"{'total':<10}: {limit}")
    print(f"{'difference':<10}: {difference}")
    print(f"{'percent':<10}: {percent:.1f}%")
    print(f"{'status':<10}: {status}")
    print("=" * 34)
# The functions above calculate the percentage and difference of the numbers entered by the user
# ==================================================================== INPUT
label = input("Enter hostname: ")      
value = float(input("Enter GB used: "))   
limit = float(input("Enter GB total: "))   
# This part of the code enables the user to enter custom values
# ================================================================== PROCESS
difference, percent = check(value, limit)
status = status_of(percent)    
# This function assigns values to specific lists    
# =================================================================== OUTPUT
if __name__ == "__main__":
    print_report(label, value, limit, difference, percent, status)
# This function prints out the output made by the user
