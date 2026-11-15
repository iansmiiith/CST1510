"""
RECORD CHECK  -  my version
===========================

Name  : Ian Smith Ochieng
Lane  : IT      
Date  : 15/11/2026

Run it:   python template.py
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
def parse_line(raw_line):
    #parses a raw IT record string into a clean dictionary.
    # remove extra spaces and split by the comma
    parts = raw_line.strip().split(',')
    clean_dict = {}
    for part in parts:
        # Split each part with '=' to separate key and value
        if '=' in part:
            key, value = part.split('=')
        # clean up spaces and make keys lowercase for consistency
            clean_key = key.strip().lower()
            clean_value = value.strip()
        # Try to convert numeric values(like'87') to integers
            if clean_value.isdigit():
                clean_dict[clean_key] = int(clean_value)
            else:
                clean_dict[clean_key] = clean_value
    return clean_dict
    # Typical and above
def status_of(parsed_record):
        # Returns 'WARNING' if used is over 80% of total, else 'OK'.
        used = parsed_record.get('used', 0)
        total = parsed_record.get('total', 100)
        if used > (total * 0.8):
            return 'WARNING'
        else:
            return 'OK"'

# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
raw_records = [
    "Srv-01, used=87, total=100", # Will trigger WARNING
    "SRV-02, USED=45, TOTAL=200", # Extra spaces, uppercase
    "Srv-03,used=95, total=100", # No spaces
    "Srv-04, used=12, total=50", # Will be OK
    "Srv-05 , Used=88 , Total=100 " # Mixed cases and spaces
]

# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
total_records = 0
flagged_count = 0
for raw_record in raw_records:
    # Clean the data
    cleaned = parse_line(raw_record)
    # Check status
    status = status_of(cleaned)
    # Update counters for the final summary
    total_records += 1
    # Print the cleaned dict alongside its status
    print(f"Data: {cleaned} | Status: {status}")
print("\n----------------------------------------")
# Print the one-line summary (Excellent requirement)
print(f"Summary: Processed {total_records} records, {flagged_count} flagged.")

