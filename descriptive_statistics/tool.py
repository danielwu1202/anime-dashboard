# 根據type分類
def type_filter(data, type):
    mask = data['Type'] == type
    data[mask].to_csv(str(type) + '_anime.csv', index=False, encoding = 'utf-8')

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

# 統計type
def type_counter(data):
    type_counter = data.Type.str.get_dummies(sep=', ').sum().to_frame(name = 'counter').reset_index()
    type_counter.columns = ['type', 'counter']
    return type_counter

'''
# 分類
def anime_filter(data, column, genre, type):
    mask = data[column] == genre
    data[mask].to_csv(str(type)+ '_' +str(genre) + '.csv', index=False)
'''

# 分類
def anime_filter(data, column, filter):
    data[data[column].str.contains(filter)].to_csv(str(filter) + '.csv', index=False, encoding = 'utf-8')


# 根據年份分類
def year_spliter(data, start, end, step, column='Start_Aired'):
    for year in range(start, end, step):
        data[(data[column] >= str(year)) & (data[column] < str(year + 10))].to_csv(str(year) + '_' + str(year + 10) + '.csv', index=False, encoding='utf-8')