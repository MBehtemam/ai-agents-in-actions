import matplotlib.pyplot as plt
import numpy as np

# Sample data for popularity over time
dates = np.array(['2020-01', '2020-04', '2020-07', '2020-10', '2021-01', '2021-04', '2021-07', '2021-10', '2022-01', '2022-04', '2022-07', '2022-10', '2023-01', '2023-04'])
popularity = np.array([5, 15, 25, 35, 50, 65, 80, 90, 85, 80, 70, 75, 85, 95])

# Creating the plot
plt.figure(figsize=(10, 5))
plt.plot(dates, popularity, marker='o')
plt.title('Popularity of GPT Agents Over Time')
plt.xlabel('Date')
plt.ylabel('Popularity (search interest)')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.savefig('gpt_popularity_plot.png')
plt.show()