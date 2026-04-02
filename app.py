# import streamlit as st
# import pickle
# import pandas as pd

# movies_dict=pickle.load(open('movie_dict.pkl','rb'))
# movies=pd.DataFrame(movies_dict)

# st.title('Movie Recommender System')
# st.subtext('hello there,please select a movie of ur choice')

# option = st.selectbox(
#     "Select a movie",
#     (movies['title'].values),
#     #index=None,
#     #placeholder="Select contact method...",
# )

# st.write("You selected:", option)
import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(id):
   response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=cd9a740228c87c6e907578e592acbabf&language=en-US'.format(id))
   data=response.json()
   #st.text('https://api.themoviedb.org/3/movie/{}?api_key=cd9a740228c87c6e907578e592acbabf&language=en-US'.format(id))
   poster_path = data['poster_path']
   full_path = "https://image.tmdb.org/t/p/w500/" + data['poster_path']

   return full_path


# def fetch_poster(movie_id):
#     # url = f"https://api.themoviedb.org/3/movie/{}?api_key=cd9a740228c87c6e907578e592acbabf&language=en-US".format(movie_id)
#    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=cd9a740228c87c6e907578e592acbabf&language=en-US'.format(movie_id))
#     #    data=response.json()
#     # Debug (optional)
#     # print(data)
#     # 
# if 'poster_path' in data and data['poster_path'] is not None:
#         return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
# else:
#         return "https://via.placeholder.com/500x750?text=No+Image"

similarity = pickle.load(open('similarity.pkl','rb'))
movies_dict = pickle.load(open('movie_dict1.pkl','rb'))
movies = pd.DataFrame(movies_dict)

# 1. Renamed the parameter to 'movie_title' for clarity
# def recommend(movie_title):
#     # 2. Changed 'movie' to 'movies' to reference the DataFrame
#     index = movies[movies['title'] == movie_title].index[0]
#     distances = similarity[index]

#     movies_list = sorted(enumerate(distances), reverse=True, key=lambda x: x[1])

#     recommended_movies = []
#     recommended_movies_posters=[]
#     for i in movies_list[1:6]:   # skip first + take top 5
#         # 3. Changed 'movie' to 'movies' here as well
#         movie_id=i[0]
#         recommended_movies.append(movies.iloc[i[0]].title)
#         #fetch poster from API
#         recommended_movies_posters.append(fetch_poster(i[0]))

#     return recommended_movies,recommended_movies_posters
st.title('Movie Recommender System')
st.subheader('hello there,please select a movie of ur choice')



option = st.selectbox(
    "Select a movie",
    movies['title'].values
)
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list[1:6]:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append((fetch_poster(movie_id)))

    return recommended_movies, recommended_movies_posters


# if st.button("Recommend"):
#     names,posters= recommend(option)
#     col1,col2,col3=st.beta_columns(3)
#     with col1:
#        st.text("A cat")

#     for i in recommendations:
#      st.write(i)

st.write("You selected:", option)

if st.button('Recommend'):
    recommended_movie_names,recommended_movie_posters = recommend(option)
    col1, col2, col3, col4, col5  = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])