import pandas as pd
import matplotlib.pyplot as plt

# Setup
df = pd.read_csv("data.csv")
df.drop_duplicates(inplace=True)

df['Popularity'] = pd.to_numeric(df['Popularity'])
df['Duration (s)'] = (pd.to_numeric(df['Duration (ms)'])) / 1000

fig, axs = plt.subplots(1,2, figsize=(12,5))

# Define duration popularity plot
def plot_duration_popularity():
  df.plot(x='Duration (s)', y='Popularity', kind='scatter', ax=axs[0])
  axs[0].set_xlabel('Duration (s)')
  axs[0].set_ylabel('Popularity')
  axs[0].set_title('Spotify song popularity vs duration')

# Define artist popularity plot
def plot_artist_popularity():
  artist_popularity = df.groupby('Artist')['Popularity'].mean().sort_values(ascending=False)
  artist_popularity.plot(kind='bar', ax=axs[1])
  axs[1].set_xlabel('Artist')
  axs[1].set_ylabel('Popularity')
  axs[1].set_title('Artist Popularity')

# Plot
plot_duration_popularity()
plot_artist_popularity()
plt.show()