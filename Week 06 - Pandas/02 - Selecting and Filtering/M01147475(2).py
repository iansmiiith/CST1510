import pandas as pd
data = pd.DataFrame ({
"name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
"math": [85, 90, 72, 60, 95],
"science": [78, 88, 85, 55, 92],
})

data["average"] = (data["math"] + data["science"]) / 2
print(data)
print(data [["name", "average"]])
print(data[data["average"] >= 80])
print(data[(data["math"] >=90) & (data["science"] >= 90)])