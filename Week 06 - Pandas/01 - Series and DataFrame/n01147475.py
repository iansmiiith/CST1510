import pandas as pd
app_sizes = pd.Series([45, 120, 15], index=["photos", "games", "music"])
print(app_sizes)
phones = pd.DataFrame({
    "Model": ["Phone A", "Phone B", "Phone C"],
    "Total_storage_gb": [128, 256, 64],
    "used_storage_gb": ["96", "128", "50"],
})
phones["Used_storage_gb"] = phones["used_storage_gb"].astype(int)
phones["Free_storage_gb"] = phones["Total_storage_gb"] - phones["Used_storage_gb"]
phones["percentage"] = phones["Used_storage_gb"] / phones["Total_storage_gb"] * 100
print(phones)