import matplotlib.pyplot as plt

# Data for the bar chart
areas = [
    "Real-time Monitoring",
    "Personalized Learning",
    "Dropout Risk Prediction",
    "LMS Integration",
    "Career Guidance",
    "Faculty Feedback",
    "Mental Health Data",
    "Multi-institutional Expansion"
]
importance = [9, 8.5, 9, 8, 7.5, 7, 8, 8.5]
 
# Plotting the bar chart
plt.figure(figsize=(12, 6))
bars = plt.barh(areas, importance, color="#4682B4")
plt.xlabel("Importance (out of 10)")
plt.title("Future Importance of Features in Student Performance Prediction System")
plt.xlim(0, 10)

# Add values next to bars
for bar in bars:
    plt.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2,
             f"{bar.get_width()}", va='center')

plt.gca().invert_yaxis()  # Highest value on top
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
