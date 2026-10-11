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
    return difference, percent

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

# ==================================================================== INPUT
label = input("Enter hostname: ")      
value = float(input("Enter GB used: "))   
limit = float(input("Enter GB total: "))   
# ================================================================== PROCESS
difference, percent = check(value, limit)
status = status_of(percent)        
# =================================================================== OUTPUT
if __name__ == "__main__":
    print_report(label, value, limit, difference, percent, status)