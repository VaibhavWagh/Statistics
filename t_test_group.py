import pandas as pd
from scipy.stats import ttest_ind

# Load the tsv file into a pandas DataFrame
df = pd.read_csv('Abundance_Group.txt', sep='\t')

# Create two separate dataframes, one for the suffix B samples and one for the suffix E samples
#we can change it based on the grouping interests

df_b = df[df.columns[df.columns.str.endswith('_B')]]
df_e = df[df.columns[df.columns.str.endswith('_E')]]

# Calculate the means of the B and E samples
b_mean = df_b.mean(axis=1)
e_mean = df_e.mean(axis=1)

# Calculate the difference between the means
mean_diff = e_mean - b_mean

# Calculate the p-value using a two-sided t-test
p_value = ttest_ind(df_b, df_e, axis=1)[1]

# Add the mean difference and p-value columns to the original DataFrame
df['Base_mean'] = b_mean
df['End_mean'] = e_mean
df['mean_diff'] = mean_diff
df['p_value'] = p_value

# Save the updated DataFrame to a new tsv file
df.to_csv('Abundance_Group_Stats.tsv', sep='\t', index=False)
