"""
RECORD CHECK  -  my version
===========================

Name  : Ian Smith Ochieng
Lane  : IT      
Date  : 08/11/2026

Run it:   python template.py
"""

import pandas as pd

# ==================================================================== LOAD

# Using the IT lane columns: hostname, used_gb, total_gb
data = {
    "hostname": ["srv-01", "srv-02", "srv-03", "srv-04", "srv-05"],
    "used_gb": [87, 115, 40, 98, 200],
    "total_gb": [120, 120, 100, 100, 250]
}
df = pd.DataFrame(data)

# ================================================================= PROCESS
# Adding a "percent" column: (value / limit) * 100
# The brackets around the division ensures it happens before multiplication
df["percent"] = df["used_gb"] / df["total_gb"] * 100
# Adding a "status" column using .apply() with a lambda
# Lambda must be one expression. Use &(and) or | (or) with brackets.
df["status"] = df["percent"].apply(
    lambda x: "OVER LIMIT" if x > 100 
else ("WARNING" if x >= 90 else "OK")
)

# ================================================================== OUTPUT
import matplotlib.pyplot as plt 

print(df.describe())

df.to_csv("servers_report.csv", index=False)

df["status"].value_counts().plot(kind="bar", title="Servers by status")
plt.tight_layout()
plt.show()
print("=== Full DataFrame ===")
# I am doing the typical which says that I should filter it to show only rows that are not "OK".
# Using != (not equal to) to filter
print(df)

print("\n=== Filtered DataFrame (Not 'OK') ===")

not_ok_df = df[df["status"] != "OK"]
print(not_ok_df)
# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
