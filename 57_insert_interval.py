def insert(intervals, new_interval):
    result = [[0, 0]]
    added_new_inter = False

    for inter in intervals:
        if inter[0] < new_interval[0]:
            result.append(inter)
        else:
            if not added_new_inter:
                if new_interval[0] <= result[-1][1] <= new_interval[1]:
                    result[-1] = [min(new_interval[0], result[-1][0]), max(new_interval[1], result[-1][1])]
                added_new_inter = True

            if inter[0] <= result[-1][1] <= inter[1]:
                result[-1] = [min(inter[0], result[-1][0]), max(inter[1], result[-1][1])]

    if not added_new_inter:
        if new_interval[0] <= result[-1][1] <= new_interval[1]:
            result[-1] = [min(new_interval[0], result[-1][0]), max(new_interval[1], result[-1][1])]

    return result[1:]
