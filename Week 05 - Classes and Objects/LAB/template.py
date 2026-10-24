"""
RECORD CHECK  -  my version
===========================

Name  : Ian Smith
Lane  : IT  
Date  : 24/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
class Record:
    # Represents a server record with usage limits.
    def __init__(self, hostname, gb_used, gb_total):
        # Initialises the record attributes.
        self.label = hostname
        self.value = gb_used
        self.limit = gb_total
    def status(self):
        # Returns the current status based on GB used.
        if self.value > self.limit:
            return "OVER LIMIT"
        elif self.value >= (self.limit * 0.90):
            return "WARNING"
        else:
            return "OK"

# ==================================================================== RECORDS
# 2. Create your records.
records = [
    Record("srv-01", 125, 120), # OVER LIMIT
    Record("srv-02", 110, 120), # WARNING
    Record("srv-03", 45, 120) # OK
]
for r in records:
    print(f"{r.label} status: {r.status()}")

# ==================================================================== OUTPUT
# 3. Print a report for each record.
for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    current_status = record.status()
    print(f" Hostname: {record.label}")
    print(f" GB Used: {record.value}")
    print(f" GB Total: {record.limit}")
    print(f" Status: {current_status}")

    print("=" * 34)

