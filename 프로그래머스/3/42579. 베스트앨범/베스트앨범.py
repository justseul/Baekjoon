def solution(genres, plays):
    answer = []
    genre_total = {}
    genre_songs = {}
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_total[g] = genre_total.get(g, 0) + p
        genre_songs.setdefault(g, []).append((p, i))
    
    sorted_genres = sorted(genre_total.items(), key=lambda x: x[1], reverse=True)
    
    for genre, _ in sorted_genres:
        songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))
        answer.extend([i for _, i in songs[:2]])
    
    return answer
