import pandas as pd

combustivel_df = pd.read_csv("precos-semestrais-ca-2022-01.csv", on_bad_lines='skip')

print(combustivel_df)