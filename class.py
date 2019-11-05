import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt 
import datetime
df = pd.read_csv('C:\\Users\\Admin\\Desktop\\taolao\LungTung\\mean-daily-temperature-fisher-river.csv')

df['month_year'] = pd.to_datetime(df['Date']).dt.to_period('M')

monthly_stats = df.groupby(by='month_year')['Mean temparature'].aggregate([np.mean, np.median, np.std])

monthly_stats.reset_index(inplace=True)
fig = plt.figure(figsize=(5.5, 5.5))
ax = fig.add_subplot(1,1,1)
monthly_stats = monthly_stats.drop(['median', 'std'], axis=1)
monthly_stats['mean'].plot(color='b')
plt.show()
