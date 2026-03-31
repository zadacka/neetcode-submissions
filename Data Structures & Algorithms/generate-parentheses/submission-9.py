class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(current, left, right):
            if left == 0 and right == 0:
                result.append(''.join(current))
                return
            
            if right and right > left:
                # we have some )'s remaining and and could use one
                current.append(')')
                dfs(current, left, right -1 )
                current.pop()
            if left:
                current.append('(')
                dfs(current, left -1, right)
                current.pop()


        dfs([], n , n)
        return result