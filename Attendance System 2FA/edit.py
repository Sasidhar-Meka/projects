import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path  # Python Standard Library
from pyecharts import options as opts  # pip install pyecharts
from pyecharts.charts import Bar, Calendar, Tab

# create attendance data
my_file = open("Staff.txt", "r")
# reading the file
data = my_file.read()
# replacing end of line('/n') with ' ' and
# splitting the text it further when '.' is seen.
data_into_list = data.replace('', '').split("\n")
days = pd.date_range(start='2023-04-01', end='2023-05-30', freq='B')
attendance = np.random.randint(low=0, high=2, size=(len(data_into_list), len(days)))
df_attendance = pd.DataFrame(data=attendance, index=data_into_list, columns=days)

# create heatmap
sns.set()
ax = sns.heatmap(df_attendance, cmap='coolwarm', linewidths=.5, annot=True)
plt.title('Attendance Heatmap (April 2023)')
plt.show()
