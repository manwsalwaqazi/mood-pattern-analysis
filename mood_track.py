import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


df= pd.read_csv("mood-pattern-analysis/mood_track.csv") 
print(df)
print(df.isnull().sum())  #check for missing values for each column
#print(df.describe())
print(df)

#handle missing value
df= df.dropna() #drop rows with missing values
print(df.isnull().sum())

#basic statistics functions

#find the most common value for each category using 1. Mode function
print(df.mode().iloc[0])  

#encoding categorical data for numerical analysis

mapping_mood = {"rad":5, "good":4, "meh":3, "bad":2, "awful":1} 
df['mood_numeric'] = df['mood'].map(mapping_mood)


#2. mean value of mood and sleep
sleep_mean = df['sleep_hours'].mean()
mood_mean = df['mood_numeric'].mean()
print("Mean Mood Score:", mood_mean)
print("Mean Sleep Hours Score: ", sleep_mean)


#3. median value of mood and sleep
mood_median = df['mood_numeric'].median()
sleep_median = df['sleep_hours'].median()
print("Median Mood Score:", mood_median)
print("Median SLeep Hours Score", sleep_median)

#4. sd of mood and sleep
std_mood = df['mood_numeric'].std()
std_sleep = df['sleep_hours'].std()
print("Standard Deviation of Mood:", std_mood)
print("Standard Deviation of Sleep Hours", std_sleep)


#1. Frequecny of each category
#print(df['mood'].value_counts())
#print(df['sleep_hours'].value_counts())
#print(df['activity'].value_counts())

# Convert 'date' column to datetime format
df['full_date'] = pd.to_datetime(df['full_date'])

# Set style for Seaborn
sns.set_style("whitegrid")

# Define custom colors for each mood
custom_palette = {"rad": "#C71585", "good": "#FF69B4", "meh": "orange", "bad": "yellow", "awful": "#90EE90"}

# 1️⃣ Mood Frequency Distribution (Bar Chart)
plt.figure(figsize=(6,4))
sns.countplot(x=df['mood'], order=mapping_mood, palette=custom_palette)
plt.title("Mood Frequency Distribution")
plt.xlabel("Mood")
plt.ylabel("Count")
plt.show()

# 2️⃣ Histogram of Sleep Hours (Histogram)
plt.figure(figsize=(6,4))
sns.histplot(df['sleep_hours'], bins="auto", kde=True, color="blue")
plt.title("Distribution of Sleep Hours")
plt.xlabel("Sleep Hours")
plt.ylabel("Frequency")
plt.show()

# 3️⃣ Pie chart of activities
plt.figure(figsize=(5,5))
# Count occurrences of each activity
activity_counts = df['activity'].value_counts()
# Create pie chart
plt.pie(activity_counts, labels=activity_counts.index, autopct='%1.1f%%', colors=sns.color_palette("pastel"))
plt.title("Activity Distribution")
plt.show()



# 4️⃣ Scatter plot of sleep vs mood
plt.figure(figsize=(6,4))
sns.scatterplot(x=df['sleep_hours'], y=df['mood_numeric'], color="red")
plt.title("Sleep Hours vs. Mood")
plt.xlabel("Sleep Hours")
plt.ylabel("Mood Score")
plt.show()

# 5 stacked bar chart of activty and mood
plt.figure(figsize=(12, 6))  # Increase width for better spacing
# Count occurrences of each activity per mood
activity_mood_counts = df.groupby(["mood", "activity"]).size().unstack()
# Create stacked bar chart with adjusted layout
activity_mood_counts.plot(kind="bar", stacked=True, figsize=(12, 6), colormap="tab20")
plt.xlabel("Mood", fontsize=12)
plt.ylabel("Activity Count", fontsize=12)
plt.title("Activity Distribution Across Moods", fontsize=14)
plt.xticks(rotation=0, fontsize=11)  # Keep moods readable
plt.yticks(fontsize=11)
plt.legend(title="Activity", bbox_to_anchor=(0.85, 1), loc="upper left", fontsize=10, frameon=True)
plt.show()

#  6 Sleep Hours vs. Mood (Boxplot)
plt.figure(figsize=(7,5))
sns.boxplot(x=df['mood'], y=df['sleep_hours'], palette="coolwarm")
plt.title("Sleep Hours vs. Mood")
plt.xlabel("Mood")
plt.ylabel("Sleep Hours")
plt.show()


# 7 Mood and sleep comparsion using bar char

plt.figure(figsize=(7,5))
# Calculate counts of each mood
mood_counts = df['mood'].value_counts().reindex(["awful", "bad", "meh", "good", "rad"])
# Calculate average sleep hours for each mood
avg_sleep = df.groupby("mood")["sleep_hours"].mean().reindex(["awful", "bad", "meh", "good", "rad"])
# Define bar width
bar_width = 0.4  
x = np.arange(len(mood_counts))  # X-axis positions
# Plot bars
plt.bar(x - bar_width/2, mood_counts, width=bar_width, label="Mood Count", color="blue")
plt.bar(x + bar_width/2, avg_sleep, width=bar_width, label="Avg Sleep Hours", color="orange")

# Labels & Formatting
plt.xticks(x, ["Awful", "Bad", "Meh", "Good", "Rad"])  # Set x-axis labels
plt.xlabel("Mood")
plt.ylabel("Count / Avg Sleep Hours")
plt.title("Mood Frequency & Avg Sleep Hours")
plt.legend()
plt.show()


