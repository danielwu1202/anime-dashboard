# 根據type分類
def type_filter(data, type):
    mask = data['Type'] == type
    data[mask].to_csv(str(type) + 'anime.csv', index=False)

# 統計genres
def genres_counter(data):
    genres_counter = data.Genres.str.get_dummies(sep=', ').sum().to_frame(name = 'counter').reset_index()
    genres_counter.columns = ['genres', 'counter']
    return genres_counter

# 統計theme
def theme_counter(data):
    theme_counter = data.Themes.str.get_dummies(sep=', ').sum().to_frame(name = 'counter').reset_index()
    theme_counter.columns = ['themes', 'counter']
    return theme_counter

'''
# 分類
def anime_filter(data, column, genre, type):
    mask = data[column] == genre
    data[mask].to_csv(str(type)+ '_' +str(genre) + '.csv', index=False)
'''

# 分類
def anime_filter(data, column, filter, type):
    data[data[column].str.contains(filter)].to_csv(str(type)+ '_' +str(filter) + '.csv', index=False)