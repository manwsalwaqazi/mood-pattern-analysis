# Data-Driven Analysis of Mood Patterns

## Project Overview
This project presents a data-driven exploratory analysis of mood tracking data to
understand emotional well-being patterns. The dataset includes daily mood ratings,
sleep hours, and recorded activities.

The analysis explores how mood fluctuates over time, examines relationships between
sleep and emotional state, and evaluates how daily activities impact overall mood.

---

## Objectives
- Analyze frequency and distribution of different mood states
- Examine the relationship between sleep duration and mood
- Identify activity patterns associated with positive and negative moods
- Use statistical summaries and visualizations to uncover trends

---

## Dataset Description
The dataset contains:
- **Mood** (categorical: awful, bad, meh, good, rad)
- **Sleep hours**
- **Daily activity**
- **Date**

> The dataset used in this project is locally generated and used strictly for
educational and analytical purposes.

---

## Data Preprocessing
- Removed rows with missing values
- Encoded categorical mood values into numerical scores
- Converted date column to datetime format
- Applied basic statistical analysis (mean, median, standard deviation)

---

## Mood Encoding
Mood values were mapped numerically as follows:

| Mood  | Score |
|------|------|
| Rad  | 5 |
| Good | 4 |
| Meh  | 3 |
| Bad  | 2 |
| Awful | 1 |

This encoding enabled numerical and statistical analysis.

---

## Analysis & Visualizations
The following visualizations were created:

- Mood frequency distribution (bar chart)
- Sleep hours distribution (histogram)
- Activity distribution (pie chart)
- Sleep hours vs mood (scatter plot)
- Activity distribution across moods (stacked bar chart)
- Sleep hours vs mood (boxplot)
- Combined mood frequency and average sleep comparison (bar chart)

These visualizations provide insights into behavioral and emotional trends.

---

## Key Insights
- Higher sleep duration is generally associated with better mood states
- Certain activities correlate more frequently with positive moods
- Mood patterns show measurable variation across different days and behaviors

---

## Tools & Technologies
- **Python**
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **NumPy**

---

## How to Run the Project
1. Clone the repository
2. Place the dataset file (`mood_track.csv`) in the project directory
3. Update the dataset path if required
4. Run `mood_track.py`

---

## Author
**Man-w-Salwa Qazi**

---

## Disclaimer
This project is for educational and analytical purposes only and does not provide
medical or psychological advice.
