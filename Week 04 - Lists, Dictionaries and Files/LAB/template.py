"""
RECORD CHECK  -  my version
===========================

Name  : Ian Smith Ochieng
Lane  : IT      
Date  : 17/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
def check_record(value, limit):
    # DIfference between the limit and the actual value.
    diff = limit - value
    # Calculate percentage, avoiding a crash if limit is 0
    pct = (value / limit) * 100 if limit > 0 else 0
    if value > limit:
    # Determine the status based on the rules
        status = "OVER LIMIT"
    elif pct >= 90:
        status = "WARNING"
    else:
        status = "OK"
    # Return the results as a dictionary
    return {"difference": diff, "percent": pct, "status": status}
def print_report(label, value, limit):
    # Call check_record to get the calculated stats
    res = check_record(value, limit)
    # Print a formatted line
    print(f"{label}: {value}/{limit} ({res['percent']:.1f}%) - {res['status']}")

    def load_records(path):
        try:
            # Open the file in read mode
            with open(path, 'r') as file:
                # List comprehension to build dictionaries from each line
                return [
                    {"label": p[0], "value": float(p[1]), "limit": float(p[2])}
                # Strip whitespace, split by comma, and only keep lines with 3 parts
                    for line in file if len(p := line.strip().split(',')) == 3
                ]
        except FileNotFoundError:
        # If the file is missing, print a clear error and return an empty list
            print(f"Error: '{path}' not found.")
            return []

# ====================================================================== STORE
def load_records(path):
    # Reads a file and returns a list of dicts.
    records_list = []
    try:
        with open(path, 'r') as file:
            for line in file:
                clean_line = line.strip()
                if not clean_line:
                    continue
                parts = clean_line.split(',')
                if len(parts) == 3:
                    records_list.append({
                        "label": parts[0],
                        "value": float(parts[1]),
                        "limit": float(parts[2])
                    })
    except FileNotFoundError:
        print(f"Error : '{path}' not found.")
    return records_list
records = [
    {"label": "srv-01", "value": 110.0, "limit": 100.0},
    {"label": "srv-02", "value": 50.0, "limit": 100.0},
    {"label": "srv-03", "value": 95.0, "limit": 100.0}
]

# =============================================================== PROCESS + OUTPUT
# Initialize a counter for the "Excellent" requirement
over_limit_count = 0
# Loop through every dictionary in the formatted report
for r in records:
    # Call the function to print the formatted report
    print_report(r["label"], r["value"], r["limit"])
#check if the current record is over the limit and update the counter
    if r["value"] > r["limit"]:
        over_limit_count += 1
# Print a separator line and the final summary
print("-" * 40)
print(f"{over_limit_count} of {len(records)} were over limit")

# ==========================================================================
