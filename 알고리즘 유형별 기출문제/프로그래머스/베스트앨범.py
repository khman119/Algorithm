# 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시
# 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def solution(genres, plays):
    answer = []
    sumGenres = {}
    songs = {}
    for i in range(len(genres)):
        sumGenres[genres[i]] = sumGenres.get(genres[i], 0) + plays[i]
    for i in range(len(genres)):
        songs[i] = [sumGenres[genres[i]], plays[i]]
    songs = sorted(songs.items(), key=lambda x: x[1], reverse=True)
    sumGenres = sorted(sumGenres.items(), key=lambda x: x[1], reverse=True)
    start = 0
    for song in sumGenres:
        count = 0
        for i in range(start, len(songs)):
            if songs[i][1][0] == song[1] and count < 2:
                answer.append(songs[i][0])
                start += 1
                count += 1
    return answer


print(solution(genres, plays))