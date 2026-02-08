def recommend(movie_title, movies, similarity, top_n=5):
    if movie_title not in movies["title"].values:
        return ["Movie not found"]

    index = movies[movies["title"] == movie_title].index[0]
    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1 : top_n + 1]

    return [movies.iloc[i[0]].title for i in movie_list]
