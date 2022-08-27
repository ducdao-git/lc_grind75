def isBadVersion(version):
    pass


def firstBadVersion(n):
    lo, hi = 1, n

    while lo < hi:
        if hi - lo == 1:
            if isBadVersion(lo):
                return lo
            else:
                return hi

        mid = (hi - lo) // 2 + lo
        print(mid)

        if isBadVersion(mid):
            hi = mid
        else:
            lo = mid

    return lo
