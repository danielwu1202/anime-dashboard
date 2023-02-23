def genres_counter(data):
    genres_counter = data.Genres.str.get_dummies(sep=', ').sum().to_frame(name = 'counter').reset_index()
    genres_counter.columns = ['genres', 'counter']
    return genres_counter

def theme_counter(data):
    theme_counter = data.Themes.str.get_dummies(sep=', ').sum().to_frame(name = 'counter').reset_index()
    theme_counter.columns = ['themes', 'counter']
    return theme_counter