def min_difference_pair(nums):
    n = sorted(nums)
    diffs = [n[i] - n[i - 1] for i in range(1, len(n))]
    idx = diffs.index(min(diffs))
    return n[idx:idx + 2]

n = [40, 16, 8, -17, 17, 15]
n1=[1, -31, -27, -18, -48, -15, -11, -34]
n2=[0, 2, 35, 42, 45, 14, -6, -1]
n3=[32, 33, 4, 6, 48, 18, 20, -7, -4, 31]

print(min_difference_pair(n2))