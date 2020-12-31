#importing allowed loibraries for exercise 
import pandas as pand
import matplotlib.pyplot as matlib

#loading genre and movie datasets
genre= pand.read_csv('https://raw.githubusercontent.com/williamykzhang/MAIS_CE/master/genre_data.csv')
movie=pand.read_csv('https://raw.githubusercontent.com/williamykzhang/MAIS_CE/master/movies_data.csv')

genre1=pand.DataFrame(genre)
movie1=pand.DataFrame(movie)

#parsing info
merge=pand.merge(genre1,movie1,on="title")

merge[['worldwide_gross']] = merge[['worldwide_gross']].replace(r'[\$,]', '', regex=True).astype(float)

#representing average gross per genre
group = merge.groupby("Main_Genre").mean()
worldwide_gross = group['worldwide_gross'].reset_index()

print(worldwide_gross)

#contructing Matlib bar graph
rep=worldwide_gross.plot(kind='bar',legend=None)

matlib.title('Worldwide Grosses for each Movie Genre')
matlib.xlabel('Movie Genres')
matlib.ylabel('Worldwide Grosses')


labels=['Action','Adventure','Animation','Comedy','Crime','Drama','Family','Fantasy','History','Horror','Music','Romance','Sci-Fi','Sport','Thriller','War']

rep.set_xticklabels(labels)

matlib.show()









