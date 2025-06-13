import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('netflix_titles.csv')

df = df.dropna(subset=['type','title','country','release_year','rating','duration'])

# how manys movies and tv shows
count_types = df['type'].value_counts()

plt.figure(figsize=(10,5))
plt.bar(count_types.index, count_types.values, color=['skyblue','orange'])
plt.title('Number of movies vs TV shows on  Netflix')
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig('movies vs tv.png',dpi=300)
plt.show()

# what is the percenatge of each content rating(PG, R,TV-MA)
# plot a pie chart

type_rating = df['rating'].value_counts()

plt.figure(figsize=(10,6))
plt.pie(type_rating, labels= type_rating.index, autopct='%1.1f%%')
plt.title('Distribution of ratings on Netflix')
plt.legend(loc = 'upper left', fontsize = 5)
plt.tight_layout()
plt.savefig('rating.png',dpi=300)
plt.show()


# how has the number of release changed over the years  
# plot a line

count_release = df['release_year'].value_counts()


plt.figure(figsize=(10,6))
plt.plot(count_release.index, count_release.values, marker='o', linestyle='-', color='red',label = 'releases over the year')
plt.title('Number of releases on Netflix over the years')
plt.xlabel('Year')
plt.ylabel('Count')
plt.grid(True)
plt.legend()
plt.savefig('releases.png',dpi=300)
plt.show()



#what is the distrubation of movies duration 
#plot a histogram

movies_df = df[df['type'] == 'Movie'].copy()
movies_df['duration_int'] = movies_df['duration'].str.replace("min"," ").astype(int)

plt.figure(figsize =(10,6))
plt.hist(movies_df['duration_int'], bins = 30, color = 'blue',edgecolor = 'black', label='no of movies') 
plt.title('Distribution of movies duration on Netflix')
plt.xlabel('Duration(min)')
plt.ylabel('Number of Movies')
plt.legend()
plt.savefig('movies_duration.png',dpi=300)
plt.show()


#relationship   between relese year and number o shows
#plot a scatter plot


type_release = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(type_release.index, type_release.values,color = 'red',label='relese_years over the shows')
plt.title('Relationship between release year and number of shows on Netflix')
plt.xlabel('Release year')
plt.ylabel('Number of shows')
plt.legend(loc='upper left',fontsize = '10')
plt.tight_layout()
plt.savefig('scatter_release year.png')
plt.show()



# top 10 countries with the highest number of shows
# plot bar chart horizontal


top_country = df['country'].value_counts().head(10)
plt.figure(figsize=(10,6))
plt.barh(top_country.index, top_country.values, color = 'blue',label = 'top 10 country')
plt.title('Top 10 countries with the highest number of shows on Netflix')
plt.xlabel('Number of shows')
plt.ylabel('Country')
plt.legend()
plt.tight_layout()
plt.savefig('top countries data_barh.png')
plt.show()

# compare movies vs tv shows
# using subplot

content_by_year = df.groupby(['release_year','type']).size().unstack().fillna(0)
fig , ax = plt.subplots(1,2, figsize=(12,5))
ax[0].plot(content_by_year.index,content_by_year['Movie'],color='red',label = 'no of movies')
ax[0].set_xlabel('year')
ax[0].set_ylabel('number of movies and Tv shows release per year')
ax[0].legend()

ax[0].plot(content_by_year.index,content_by_year['TV Show'],color='blue',label = 'no of tv shows')
ax[0].legend()

fig.suptitle('compare between movies and tv shows release per year')
plt.tight_layout()
plt.savefig('compare of movies vs tv shows.png')
plt.show()
"""
