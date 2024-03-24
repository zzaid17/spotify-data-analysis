import pandas as pd
import matplotlib.pyplot as plt

# Setup

df = pd.read_csv("data.csv")
df.drop_duplicates(inplace=True)

df['Popularity'] = pd.to_numeric(df['Popularity'])
df['Duration (s)'] = (pd.to_numeric(df['Duration (ms)'])) / 1000

fig, axs = plt.subplots(1,2, figsize=(12,5))

# Popularity vs Duration Plot

df.plot(x='Duration (s)', y='Popularity', kind='scatter', ax=axs[0])
axs[0].set_xlabel('Song duration (s)')
axs[0].set_ylabel('Song popularity')
axs[0].title('Spotify song popularity vs duration')

# Popularity vs Artist Plot

artist_popularity = {}
for index, row in df.iterrows():
    artist = row['Artist']
    popularity = row['Popularity']
    if artist in artist_popularity:
      artist_popularity[artist].append(popularity)
    else:
      artist_popularity[artist] = [popularity]

mean_popularity = {}
for artist, popularity in artist_popularity.items():
    mean_popularity[artist] = round(sum(popularity) / len(popularity), 2)

mean_popularity_sorted = dict(sorted(mean_popularity.items(), key=lambda x:x[1], reverse=True))
print(mean_popularity_sorted)

plt.bar(mean_popularity.keys(), mean_popularity.values())
plt.xlabel('Artist')
plt.ylabel('Popularity')
plt.title('Artist Popularity')
plt.show()