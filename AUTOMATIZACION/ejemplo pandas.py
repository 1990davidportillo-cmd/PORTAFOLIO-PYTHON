import pandas as pd

data = {
    "Nombre": ["Ana", "Juan", "Maria"],
    "Edad": [25, 30, 28],
    "Ciudad": ["Guatemala", "Antigua", "Quetzaltenango"]
}

df = pd.DataFrame(data)

print(df)

df.to_excel("Ejemplo pandas.xlsx")
df.to_csv("Ejemplo pandas.csv")
df.to_json("Ejemplo pandas.json")
