class Solution:

def containsNearbyAlmostDuplicate(self, nums, k, t):
    if k < 1 or t < 0:
        return False
    dic = collections.OrderedDict()
    for n in nums:
        key = n if not t else n // t
        for m in (dic.get(key - 1), dic.get(key), dic.get(key + 1)):
            if m is not None and abs(n - m) <= t:
                return True
        if len(dic) == k:
            dic.popitem(False)
        dic[key] = n
    return False