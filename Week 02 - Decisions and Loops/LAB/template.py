"""
RECORD CHECK  -  my version
===========================

Name  :Ian Smith Ochieng
Lane  :IT
Date  :3/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
count = 0
while True:

    label = input("Enter the label or type quit to stop: ")  
    if label == "quit":
        break # stops the code from looping if the wrong data is entered

    value = float(input("Enter the first number: "))    
    limit = float(input("Enter the seecond number: "))    
# This enables the user to enter a number of choice
# ================================================================== PROCESS

    difference = value - limit 
    percent = (value / limit) * 100     

    if value > limit:
        status = "OVER LIMIT"

        count += 1 # Adds an increment of 1 on the number entered
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
   # This calculates the numbers entered by the user respectively 
# =================================================================== OUTPUT
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print(f"Typical : Difference: {difference:.2f} Percent: {percent:.2f}%") # Arranges the data in a certain hierachy

    print("=" * 34)
    print(f"Total records that came back OVER LIMIT: {count}")
# This displays the output of the data entered by the user