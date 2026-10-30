"""
RECORD CHECK  -  my version
===========================

Name  : Ian Smith
Lane  : IT  
Date  : 24/10/2026

Run it:   python template.py
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
def load_records(path):
    records_list = []
    try:
        with open(path, 'r') as file:
            for line in file:
                clean_line = line.strip()
                if not clean_line:
                    continue
                parts = clean_line.split(',') # Only processes lines that have exactly 3 parts
                if len(parts) == 3:
                    records_list.append({
                        "label": parts[0].strip(), 
                        "value": float(parts[1]), 
                        "limit": float(parts[2])
                    })
    except FileNotFoundError:
        print(f"Error: '{path}' not found.")
    return records_list
# ==================================================================== PROCESS
# Define the file name
file_name = 'data.txt'
#1. load the dictionaries from the file
raw_data = load_records(file_name)
#2. Convert the dictionaries into Record objects
records = []
for item in raw_data:
    # Create a Record object using the dictionary keys 
    new_record = Record(item["label"], item["value"], item["limit"])
    records.append(new_record)
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

