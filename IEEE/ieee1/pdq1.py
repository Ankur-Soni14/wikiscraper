import numpy as np
import pandas as pd

df = pd.read_csv(
    "D:\ANKUR\IMP\BITS\Pythonprojects\IEEE\ieee1\survey_results_public.csv")

print(df.iloc[1]["Employment"])
print(df.iloc[2]["Employment"])
