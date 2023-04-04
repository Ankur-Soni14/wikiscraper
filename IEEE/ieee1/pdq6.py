import numpy as np
import pandas as pd

survey_data = pd.read_csv(
    "D:\ANKUR\IMP\BITS\Pythonprojects\IEEE\ieee1\survey_results_public.csv")

p1 = survey_data.loc[survey_data['Country'] == "United States of America"]
p2 = survey_data.loc[survey_data['Country'] ==
                     "United Kingdom of Great Britain and Northern Ireland"]
print(p1)
print(p2)
