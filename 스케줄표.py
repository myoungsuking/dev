import matplotlib.pyplot as plt

# Sample data for the timetable (you can adjust this part)
activities = {
    "Sleep": 8,         # Hours spent sleeping
    "Work": 9,          # Hours spent working
    "Exercise": 1,      # Hours spent exercising
    "Relax": 2,         # Hours spent relaxing
    "Hobby": 2,         # Hours spent on hobbies
    "Family Time": 2    # Hours spent with family
}

# Define colors for each activity (similar to a playful aesthetic)
colors = ['#d3baff', '#ffe599', '#a9d08e', '#9dc3e6', '#f4cccc', '#ffd966']

# Create a pie chart
fig, ax = plt.subplots()

# Create the pie chart based on the activities and their corresponding times
ax.pie(activities.values(), labels=activities.keys(), autopct='%1.1f%%', startangle=90, colors=colors)

# Make sure the pie chart is a circle
ax.axis('equal')

# Add a title similar to the image's playful tone
plt.title("My Cute Timetable for the Day", fontsize=16)

# Show the chart
plt.show()
