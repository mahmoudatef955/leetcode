class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def per_rec(path, res, letters):
            if letters is None or len(path) == len(s):
                res.append("".join(path))
                return
            if letters[0].isdigit():
                path.append(letters[0])
                per_rec(path, res, letters[1:])
                path.pop()
            elif letters[0].islower():
                path.append(letters[0])
                per_rec(path, res, letters[1:])
                path.pop()
                path.append(letters[0].upper())
                per_rec(path, res, letters[1:])
                path.pop()
            elif letters[0].isupper():
                path.append(letters[0])
                per_rec(path, res, letters[1:])
                path.pop()
                path.append(letters[0].lower())
                per_rec(path, res, letters[1:])
                path.pop()

        res = []
        path = []
        per_rec(path, res, s)
        return res
