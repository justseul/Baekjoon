def solution(genres, plays):
    play_num = dict()
    genre = dict()
    for idx, (g, p) in enumerate(zip(genres, plays)):
        if g in genre.keys():
            genre[g].append((idx,p))
            play_num[g] += p
        else:
            genre[g] = [(idx,p)]
            play_num[g] = p
    sorted_genres = sorted(play_num.items(), key=lambda x: x[1], reverse=True)
    
    result = []
    for genre_name, _ in sorted_genres:
        sorted_songs = sorted(genre[genre_name], key=lambda x: (-x[1], x[0]))
        result.append(sorted_songs[0][0])  
        if len(sorted_songs) > 1:
            result.append(sorted_songs[1][0])  
    return result