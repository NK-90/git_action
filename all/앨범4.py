import collections

genres = ['classic','pop','classic','pop','classic','classic','rap','rap','rap']
plays  = [400,       600,   150,    2500,   500,      500,     400,  400,  100]


def solution(genres, plays):
    less_genres = list(set(genres))
    sum_list = []
    dict1 = {}

    print('less_genres:', less_genres)

    for j in range(len(less_genres)):

        sum = 0
        for i, gen in enumerate(genres):

            if gen == less_genres[j]:
                sum += plays[i]
        sum_list.append(sum)

    for i in range(len(sum_list)):
        dict1[sum_list[i]] = less_genres[i]

    sum_list.sort(reverse=True)

    print('sum_list:', sum_list)
    print('dict1:', dict1)

    list5 = []

    for i in range(len(sum_list)):
        q = dict1[sum_list[i]]
        list5.append(q)

    answer = []

    for i in range(len(list5)):

        append_list = []
        dict = {}

        for j in range(len(genres)):
            dict[j] = genres[j]

        k = list5[i]

        for i in range(len(genres)):
            if genres[i] == k:
                append_list.append(plays[i])

        list2 = list(dict.keys())

        after_list = sorted(append_list, reverse=True)

        if len(after_list) == 1:

            a = after_list[0]
            c = plays.index(a)
            ans = [c]
            answer.extend(ans)

        else:

            a = after_list[0]
            b = after_list[1]
            c = plays.index(a)
            d = plays.index(b)
            if a == b:
                d += 1
            ans = [c, d]
            answer.extend(ans)

    return answer

solution(genres, plays)