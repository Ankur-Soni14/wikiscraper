import numpy as np
import pandas as pd

survey_data = pd.read_csv(
    "D:\ANKUR\IMP\BITS\Pythonprojects\IEEE\ieee1\survey_results_public.csv")

emp = survey_data['Employment'].value_counts()["Employed, full-time"]
total = len(survey_data)

print(emp/total*100, "%")
