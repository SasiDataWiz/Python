# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# URL of CSV file
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/01-01-2021.csv"

# Read CSV data from URL
df = pd.read_csv(url)

# Explore and analyze the dataset
# Display the first 5 rows
print(df.head())

# Display the last 5 rows
print(df.tail())

# Display dataset info (column names, data types, etc.)
print(df.info())

# Display summary statistics
print(df.describe())

# Data cleaning and preprocessing
# Check for missing data
print(df.isnull().sum())

# Drop missing data
df_clean = df.dropna()

# Convert data type of 'Last_Update' column to datetime
df_clean['Last_Update'] = pd.to_datetime(df_clean['Last_Update'])

# Filtering, sorting, and indexing
# Filter rows with more than 10,000 confirmed cases
high_cases = df_clean[df_clean['Confirmed'] > 10000]

# Sort the data by confirmed cases in descending order
sorted_cases = df_clean.sort_values('Confirmed', ascending=False)

# Set 'Province_State' as the index
df_indexed = df_clean.set_index('Province_State')

# Grouping and aggregation
# Group data by 'Country_Region' and calculate the sum of confirmed cases
grouped_cases = df_clean.groupby('Country_Region')['Confirmed'].sum()

# Merging, joining, and concatenating DataFrames
# Example DataFrames for merging
df1 = df_clean[['Province_State', 'Confirmed']]
df2 = df_clean[['Province_State', 'Deaths']]

# Merge DataFrames on 'Province_State' column
merged_df = pd.merge(df1, df2, on='Province_State')

# Reshaping and pivoting DataFrames
# Pivot data to show confirmed cases and deaths by state
pivoted_df = df_clean.pivot_table(values=['Confirmed', 'Deaths'], index='Province_State')

# Visualizing data using Pandas
# Bar plot of confirmed cases by state
df_clean.plot(x='Province_State', y='Confirmed', kind='bar', figsize=(12, 6))
plt.title('Confirmed COVID-19 Cases by State')
plt.ylabel('Number of Cases')
plt.show()

# Scatter plot of confirmed cases vs. deaths
df_clean.plot(x='Confirmed', y='Deaths', kind='scatter', figsize=(12, 6))
plt.title('COVID-19 Confirmed Cases vs. Deaths')
plt.xlabel('Number of Cases')
plt.ylabel('Number of Deaths')
plt.show()
