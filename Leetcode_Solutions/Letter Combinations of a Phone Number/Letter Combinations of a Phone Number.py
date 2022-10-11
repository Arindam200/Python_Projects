class Solution:
    def letterCombinations(self, D: str) -> List[str]:
        lenD, ans = len(D), []
        if D == "": return []
        def bfs(pos: int, st: str):
            if pos == lenD: ans.append(st)
            else:
                letters = L[D[pos]]
                for letter in letters:
                    bfs(pos+1,st+letter)
        bfs(0,"")
        return ans


"""
Solution Idea:

Since each digit can possibly mean one of several characters, you'll need to create code that branches down the different paths as you iterate through the input digit string (D).

This quite obviously calls for a depth-first search (DFS) approach as you will check each permutation of characters and store them in our answer array (ans). For a DFS approach you can use one of several options, but a recursive solution is generally the cleanest.

But first, you'll need to set up a lookup table (L) to convert a digit to its possible characters. Since the digits are actually low-indexed integers, you can actually choose between an array or map/dictionary here with little difference.

For our DFS function (dfs), you'll have to feed it the current position (pos) in D as youll as the string (str) being built. The function will also need to have access to D, L, and ans.

The DFS function itself is fairly simple. It will push a completed str onto ans, otherwise it will look up the characters that match the current pos, and then fire off new recursive functions down each of those paths.

Once you're done, you should be ready to return ans.

You can find solution in multiple languages in the link mentioned below:
https://dev.to/seanpgallivan/solution-letter-combinations-of-a-phone-number-1n91#idea
"""
