class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make a dictionary with every new combo we see
        #  map the sorted word combo to an index value.
        #  This index value will be the index of the big list, not the sublists.
        # if the sorted word is in the dictionary, 
        #   append the original word to the sublist found at the index.
        # if it is not, put it in the dictionary mapped to index+1
        #   and append a new list to the big list with just that word inside.

        seen = {}
        result = []
        index = 0

        for i, s in enumerate(strs):
            cur = ''.join(sorted(s))
            if cur in seen:
                result[seen.get(cur)].append(s)
            else:
                seen.update({cur: index})
                result.append([s])
                index += 1
        return result