# coding=utf-8
import numpy
from pandas import DataFrame, Series


def numpy_dot():
    """
    Imagine a point system in which each country is awarded 4 points for each
    gold medal,  2 points for each silver medal, and one point for each
    bronze medal.

    Using the numpy.dot function, create a new dataframe called
    'olympic_points_df' that includes:
        a) a column called 'country_name' with the country name
        b) a column called 'points' with the total number of points the country
           earned at the Sochi olympics.
    """

    countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea', 
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

    gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
    bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]
    df = DataFrame({"country_name": Series(countries), "gold": Series(gold),
                    "silver": Series(silver), "bronze": Series(bronze)})
    # 直接利用pandas中的dot解决
    # df["point"] = df[["gold", "silver", "bronze"]].dot([4, 2, 1])
    # olympic_points_df = df[["country_name", "point"]]
    # 使用numpy的dot
    medal_counts = df[["gold", "silver", "bronze"]]
    points = numpy.dot(medal_counts, [4, 2, 1])  # 每行进行内积运算
    print points
    olympic_points_df = DataFrame({"country_name": countries, "point": points})
    # contury_df = DataFrame({"country_name": countries,
    #                         "points": map(lambda i: gold[i] * 4 + silver[i] * 2 + bronze[i] * 1, range(len(gold)))})
    return olympic_points_df

print numpy_dot()