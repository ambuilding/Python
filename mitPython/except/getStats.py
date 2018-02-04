def get_stats(class_list):
    new_stats = []

    for elt in class_list:
        new_stats.append([elt[0], elt[1], avg(elt[1])])
    return new_stats


test_grades = [[['peter', 'parker'], [10.0, 5.0, 85.0]],
           [['bruce', 'wayne'], [10.0, 8.0, 74.0]],
           [['captain', 'america'], [8.0,10.0,96.0]],
           [['deadpool'], []]]

#def avg(grades):
#    return sum(grades)/len(grades)

def avg(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print('no grades data')
        return 0.0
