import pandas as pd

data = {
    "Nombre": ["Ana", "Juan", "Maria"],
    "Edad": [25, 30, 28],
    "Ciudad": ["Guatemala", "Antigua", "Quetzaltenango"]
}

df = pd.DataFrame(data)

print(df)
