stairs_sol = {1: 1, 2: 2}  # <n>:<#_of_way>


def climb_stairs(n):
    if n in stairs_sol:
        return stairs_sol[n]
    else:
        stairs_sol[n] = climb_stairs(n - 1) + climb_stairs(n - 2)
        return stairs_sol[n]
