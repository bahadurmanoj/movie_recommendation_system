import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}.?api_key=fa9a7615149d3047e46c4bffaca14e2a&language=en-US'
                 .format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data ['poster_path']

def recommend(movie):
    movie_index = movies_dict[movies_dict['title']== movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse= True, key=lambda x:x[1])[1:17]
    
    recommended_movies=[]
    recommended_moveies_poster = []
    for i in movies_list:
        movie_id = movies_dict.iloc[i[0]].movie_id
        #fetch poster from movie_id:
        
        recommended_movies.append(movies_dict.iloc[i[0]].title)
        recommended_moveies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_moveies_poster

movies_dict =pickle.load(open('movies_dict.pkl','rb'))
movies_list= pd.DataFrame(movies_dict)

similarity= pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommedation System')

selected_movie_name = st.selectbox(
    "How would you like to be contacted?",movies_list['title'].values)


if st.button('Recommend'):
    name, posters = recommend(selected_movie_name)
    
    # cols = st.columns(7, gap="medium", vertical_alignment="center")

    # cols = st.columns(7)
    # Iterate over the movies in chunks of 4
    # for i in range(0, len(name), 10):
    #  cols = st.columns(4)  # Create 4 columns for each row
    
    # # Display up to 4 movies in each row
    # for j in range(4):
    #     if i + j < len(name):  # Check to avoid index error for the last row if there are fewer than 4 remaining
    #         with cols[j]:
    #             st.text(name[i + j])      # Display the name of the movie
    #             st.image(posters[i + j])  # Display the poster of the movie

    
    # cols = st.columns(7)  # Create 7 columns

    # for i, col in enumerate(cols):
    #  with col:
    #     st.text(name[i])
    #     st.image(posters[i])

    # cols = st.columns(7, gap="medium", vertical_alignment="center")

    # for i, col in enumerate(cols):
    #  with col:
    #     st.text(name[i])
    #     st.image(posters[i])
 

    # col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

    # with col1:
    #  st.text(name[0])
    #  st.image(posters[0])

    # with col2:
    #  st.text(name[1])
    #  st.image(posters[1])

    # with col3:
    #  st.text(name[2])
    #  st.image(posters[2])


    # with col4:
    #  st.text(name[3])
    #  st.image(posters[3])


    # with col5:
    #  st.text(name[4])
    #  st.image(posters[4])


    # with col6:
    #  st.text(name[5])
    #  st.image(posters[5])


    # with col7:
        
    #  st.text(name[6])
    #  st.image(posters[6])
    
    # Iterate over the movies in chunks of 4 to create a new row for each group of 4 movies
    for i in range(0, len(name), 4):
    # Create a new row with up to 4 columns
     cols = st.columns(min(4, len(name) - i))
    
    # Display movies in the current row
     for j, col in enumerate(cols):
         with col:
            st.text(name[i + j])      # Display the name of the movie
            st.image(posters[i + j], use_column_width=True)  # Fit the poster to the column width


