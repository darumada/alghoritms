def groupAnagrams(arr):
    map = {}

    for str in arr:
        sorted_str = ''.join(sorted(str));
        if sorted_str in map:
            map[sorted_str].append(str)
        else:
            map[sorted_str] = [str]

    return map.values()

arr = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(groupAnagrams(arr))


'''

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

'''