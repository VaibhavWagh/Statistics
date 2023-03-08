#Statistics Calculation for two columns data
import pandas as pd
from scipy.stats import ttest_ind

# Load the TSV file into a pandas dataframe
df = pd.read_csv('Species_Abundance.txt', delimiter='\t')

# Extract the two columns
col1 = df['Control_Abs']
col2 = df['Test_Abs']

# Perform the t-test
t_stat, p_val = ttest_ind(col1, col2)

# Write the results to a new file
with open('Stats.tsv', 'w') as f:
    f.write(f"t-statistic: {t_stat}\tp-value: {p_val}\n")
