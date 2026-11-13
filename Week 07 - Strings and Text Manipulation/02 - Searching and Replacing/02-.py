filenames = ["ALERT: reaching margin log", "ERROR: invalid syntax", "ALERT: margin hit log"]
for f in filenames:
    if f.endswith("log"):
        print(f)
    if f.startswith("ALERT"):
        print(f)