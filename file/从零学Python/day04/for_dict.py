def test_for():
    dict_score = {'math':'80','english':'90','chinese':'100'}
    print(dict_score)

    for key in dict_score:
        print(key)
        # ==
        print(dict_score[key])

    for value in dict_score:
        print(dict_score[value])

    for key,value in dict_score.items():
        print(key,value)
