# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
def insert_into(pair, sorted_list):
    for idx, p2 in enumerate(sorted_list):
        if p2.key <= pair.key:
            continue
        else:
            return sorted_list[:idx] + [pair] + sorted_list[idx:]
    else:
        sorted_list.append(pair)
        return sorted_list

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []
        
        result = [
            [p for p in pairs],
        ]
        for idx in range(1, len(pairs)):
            partial = result[-1]
            
            sorted_part = partial[:idx]
            to_sort = partial[idx]
            unsorted_part = partial[idx + 1:] if (idx + 1 <= len(pairs)) else []

            result.append(
                insert_into(to_sort, sorted_part) + unsorted_part
            )
        return result
                
