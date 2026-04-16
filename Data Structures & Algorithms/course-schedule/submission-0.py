
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodemap = defaultdict(list)

        for (c, p) in prerequisites:
            nodemap[c].append(p)
            if p not in nodemap:
                nodemap[p] = []
        print(f"nodemap: {nodemap}")
        while True:
            something_removed = False
            for course in list(nodemap.keys()):
                pre = nodemap[course]
                print(f"considering {course}, {pre}")
                if not pre:
                    del nodemap[course]
                    print(f"removing {course}")
                    # strip all references
                    for k, v in nodemap.items():
                        nodemap[k] = [x for x in v if x!=course]
                    something_removed = True
            print(f"remaining: {nodemap}")
            if not something_removed:
                if nodemap:
                    return False
                return True