# coding=utf-8
# 协同过滤
import math

# 影评人：｛电影：评分,...｝
critics = {'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
                         'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
                         'The Night Listener': 3.0},
           'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
                            'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
                            'You, Me and Dupree': 3.5},
           'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
                                'Superman Returns': 3.5, 'The Night Listener': 4.0},
           'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
                            'The Night Listener': 4.5, 'Superman Returns': 4.0,
                            'You, Me and Dupree': 2.5},
           'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                            'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
                            'You, Me and Dupree': 2.0},
           'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                             'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
           'Toby': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0, 'Superman Returns': 4.0}}


# Euclidean Distance Score
# tip 1： 根据二者在坐标系的距离以确定二者兴趣偏好的相似性
# tip 2:  通过求每个坐标上的差值的平方，将之求和，然后开平方根。如此这般，距离越短，则偏好约相似
# tip 3： 为了更好的评价相似性，可以对tip2的结果+1并求其倒数，这样可以将结果的范围至于[0,1]之间，这样1即表示两人偏好一样
def sim_distance(prefs, person1, person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    if len(si) == 0:
        return 0
    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2) for item in si.keys()])

    return 1 / (1 + sum_of_squares)


# Pearson Correlation Score
# tip 1: 找出两位影评人都评价过的电影，然后计算两者的评分总和与平方和，并求出评分的乘积之和
# tip 2: 返回-1与1之间的值，值为1表示评价一致
def sim_pearson(prefs, p1, p2):
    si = {item: 1 for item in prefs[p1] if item in prefs[p2]}
    n = len(si)
    if n == 0:
        return 1
    # 偏好求和
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])
    # 偏好平方和
    sum1sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2sq = sum([pow(prefs[p2][it], 2) for it in si])
    # 偏好乘积和
    psum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

    # 计算皮尔逊相关系数
    num = psum - (sum1 * sum2 / n)
    den = math.sqrt((sum1sq - pow(sum1, 2) / n) * (sum2sq - pow(sum2, 2) / n))
    if den == 0:
        return 0
    r = num / den
    return r


# ranking the critics
# 获得与指定person品味相似的其他人，并进行排序
def top_matches(prefs, person, n=5, similarity=sim_pearson):
    scores = [(similarity(prefs, person, other), other) for other in prefs if other != person]
    # 按分数降序排列
    scores.sort(key=lambda x: -x[0])
    return scores[0:n]


# recommending items
# tip 1: 获得相关度的和，计算相关度与评价值的乘积，得到新的相关度之和。然后用新的除以旧的
# tip 2: 可以知道，相关度更高的人，对整体的评价贡献更大
def get_recommendations(prefs, person, similarity=sim_pearson):
    totals = {}
    simSums = {}
    for other in prefs:
        # don't compare me to myself
        if other == person:
            continue
        sim = similarity(prefs, person, other)
        # ignore scores of zero or lower
        if sim <= 0:
            continue
        for item in prefs[other]:
            # only score movies I haven't seen yet
            if item not in prefs[person] or prefs[person][item] == 0:
                # Similarity * Score
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim
                # Sum of similarities
                simSums.setdefault(item, 0)
                simSums[item] += sim
                # Create the normalized list
        rankings = [(total / simSums[item], item) for item, total in totals.items()]
        # Return the sorted list
        rankings.sort()
        rankings.reverse()
        return rankings


# 将评价和电影对换
def transformPrefs(prefs):
    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})[person] = prefs[person][item]
    return result

if __name__ == '__main__':
    # print sim_distance(critics, "Lisa Rose", "Gene Seymour")
    # print sim_pearson(critics, "Lisa Rose", "Gene Seymour")
    # print top_matches(critics, 'Toby', n=3)
    print get_recommendations(critics, 'Toby', similarity=sim_distance)
    movies = transformPrefs(critics)
    print get_recommendations(movies, "Just My Luck")