def increase(salary, percentage, rating):
    """ increase salary base on rating and percentage
    rating 1 - 2 no increase
    rating 3 - 4 increase 5%
    rating 5 - 6 increase 10%
    """
    if rating < 3:
        result = salary * percentage
    elif rating < 5:
        result = salary * percentage * 1.05
    else:
        result = salary * percentage * 1.10
    print(result)

increase(100,0.10, 1)