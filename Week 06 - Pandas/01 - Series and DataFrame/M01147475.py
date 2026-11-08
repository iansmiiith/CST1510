import pandas as pd 
Inventory = pd.DataFrame({
    "item": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "price": [900.0, 160.0, 400.0, 1000.0],
    "stock": [100, 20, 40, 85]
})
print(Inventory)

Inventory["Total"] = (Inventory["price"] * Inventory["stock"])
print(Inventory)


