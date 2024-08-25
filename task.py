import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from datetime import datetime

# Sample dataset
data = {
    'Task ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Task Description': ['Email follow-up', 'Team meeting', 'Code review', 'Lunch break', 'Project planning', 
                         'Design discussion', 'Documentation update', 'Client call', 'Code deployment', 'Performance analysis'],
    'Start Time': ['10:00 AM', '11:00 AM', '01:00 PM', '12:00 PM', '03:00 PM', 
                   '11:00 AM', '04:00 PM', '05:00 PM', '02:00 PM', '09:00 AM'],
    'End Time': ['10:30 AM', '12:00 PM', '02:00 PM', '01:00 PM', '04:00 PM', 
                 '12:00 PM', '05:00 PM', '05:30 PM', '03:00 PM', '10:00 AM'],
    'Completion Status': ['Completed', 'Completed', 'Completed', 'Completed', 'Completed', 
                          'Not Completed', 'Completed', 'Completed', 'Not Completed', 'Completed']
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert time to datetime objects for easier manipulation
df['Start Time'] = pd.to_datetime(df['Start Time'], format='%I:%M %p').dt.time
df['End Time'] = pd.to_datetime(df['End Time'], format='%I:%M %p').dt.time

# Function to calculate duration
def calculate_duration(row):
    start = datetime.combine(datetime.today(), row['Start Time'])
    end = datetime.combine(datetime.today(), row['End Time'])
    duration = (end - start).seconds / 60
    return duration

df['Duration'] = df.apply(calculate_duration, axis=1)

# Encode completion status
df['Completion Status'] = df['Completion Status'].apply(lambda x: 1 if x == 'Completed' else 0)

# Function to convert time to a single feature
def time_to_minutes(t):
    return t.hour * 60 + t.minute

df['Start Time in Minutes'] = df['Start Time'].apply(time_to_minutes)

# Feature selection
features = df[['Start Time in Minutes', 'Duration', 'Completion Status']]

# Fit Nearest Neighbors model
nbrs = NearestNeighbors(n_neighbors=3, algorithm='auto').fit(features)

# Function to recommend tasks
def recommend_tasks(time):
    time_in_minutes = time_to_minutes(time)
    distances, indices = nbrs.kneighbors([[time_in_minutes, 0, 0]])
    recommended_tasks = df.iloc[indices[0]]
    return recommended_tasks['Task Description'].tolist()

# Encapsulate recommendation system in a function
def task_recommendation_system(input_time):
    recommendation_time = datetime.strptime(input_time, '%I:%M %p').time()
    recommended_tasks = recommend_tasks(recommendation_time)
    return recommended_tasks

# Example usage

print("Task at 5:00pm:",task_recommendation_system('05:00 PM'))
