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

<img width="687" height="241" alt="image" src="https://github.com/user-attachments/assets/774b8d96-11ad-4065-97b7-f3e84cf44e7f" />


This encoding enabled numerical and statistical analysis.

---

## Analysis & Visualizations
The following visualizations were created:

- Mood frequency distribution (bar chart)
  <img width="764" height="519" alt="image" src="https://github.com/user-attachments/assets/271ca48b-4560-48fc-8f1a-fe59e1b6c6b3" />

- Sleep hours distribution (histogram)
  <img width="826" height="563" alt="image" src="https://github.com/user-attachments/assets/197415b2-d727-4e54-8520-b8095ff5f024" />

- Activity distribution (pie chart)
  <img width="579" height="496" alt="image" src="https://github.com/user-attachments/assets/20025600-a7d5-4874-8819-878c74d44d09" />

- Sleep hours vs mood (scatter plot)
  <img width="704" height="415" alt="image" src="https://github.com/user-attachments/assets/61191bc8-40d8-458f-9122-5ebbb219f018" />

- Activity distribution across moods (stacked bar chart)
  <img width="833" height="415" alt="image" src="https://github.com/user-attachments/assets/c7755aa6-0bf2-48cb-8de9-63f1ebecdb88" />

- Sleep hours vs mood (boxplot)
  <img width="935" height="451" alt="image" src="https://github.com/user-attachments/assets/cf8d1d07-7e2f-42b8-9fc0-4842945694b5" />

- Combined mood frequency and average sleep comparison (bar chart)
  <img width="910" height="515" alt="image" src="https://github.com/user-attachments/assets/215d8051-de38-45b8-b075-b332288a73eb" />


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
