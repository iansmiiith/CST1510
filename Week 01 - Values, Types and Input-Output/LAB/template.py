"""
RECORD CHECK  -  my version
===========================

Name  : Ian Smith
Lane  :  IT      
Date  :25/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT


label =input("Enter the label (text): ")      
first = float(input("Enter the first number: "))     
second = float(input("Enter the second number: "))    


# ================================================================== PROCESS


difference = 0.0   # 
percent = 0.0      # 
difference = first - second
percent = (first / second) * 100

# =================================================================== OUTPUT

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)


print(f"Label: {label}")
print(f"First number: {first:>10.2f}")
print(f"Second number: {second:>10.2f}")
print(f"Difference: {difference:>+10.2f}")
print(f"Percentage: {percent:>10.2f}%")
print("=" * 34)


