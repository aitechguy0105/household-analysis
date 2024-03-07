# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
# Load the dataset
data = pd.read_csv('test_data.csv')

# Define the custom order of activity names
custom_order = ['Activity 1', 'Activity 2', 'Activity 3']

# Convert 'activity_name' column to categorical data type with custom ordering
data['activity_name'] = pd.Categorical(data['activity_name'], categories=custom_order, ordered=True)

# Sort the DataFrame based on the custom order of activity names
data = data.sort_values('activity_name')
data['date_of_birth'] = pd.to_datetime(data['date_of_birth'], errors='coerce', format='%m/%d/%Y')

# Calculate age in years
current_date = datetime.now()
data['age'] = (current_date - data['date_of_birth']).dt.days // 365
# Display the DataFrame with activity names in the specified order
print(data)

# Group by 'activity_name' and count unique 'household_identifier' values
household_counts = data.groupby('activity_name')['household_identifier'].nunique()

# Create a bar plot to show the number of household members for each activity
plt.figure(figsize=(10, 6))
plt.bar(household_counts.index, household_counts.values, color='skyblue')
plt.title('Number of Household Members for Each Activity')
plt.xlabel('Activity Name')
plt.ylabel('Number of Household Members')
plt.xticks(rotation=45)
plt.show()

# Data exploration and visualization for demographic profile
plt.figure(figsize=(12, 6))
sns.countplot(x='activity_name', hue='gender', data=data)
plt.title('Gender Distribution of Beneficiaries by Activity')
plt.xlabel('Activity Name')
plt.ylabel('Count')
plt.show()

for activity, group in data.groupby('activity_name'):
    plt.figure()
    plt.hist(group['age'], bins=10, color='skyblue')
    plt.title(f'Age Distribution for {activity}')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.show()

plt.figure(figsize=(12, 6))
sns.histplot(data['age'], bins=10, kde=True)
plt.title('Age Distribution of Beneficiaries')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# Visualization for beneficiaries appearing in multiple activities
beneficiary_counts = data['beneficiary_identifier'].value_counts()
multiple_activity_beneficiaries = beneficiary_counts[beneficiary_counts > 1]

plt.figure(figsize=(8, 5))
sns.countplot(x=multiple_activity_beneficiaries.values)
plt.title('Number of Activities Beneficiaries are Enrolled In')
plt.xlabel('Number of Activities')
plt.ylabel('Count')
plt.show()
