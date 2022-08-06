
class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_dict = {}
        for index, i in enumerate(s):
            if i == '(':
                parentheses_dict[i] = parentheses_dict.get(i, 0) + 1
            elif i == ')':
                if index != 0 and s[index-1] != '(':
                    return False
                parentheses_dict['('] = parentheses_dict.get('(', 0) - 1
            elif i == '{':
                parentheses_dict[i] = parentheses_dict.get(i, 0) + 1
            elif i == '}':
                if index != 0 and s[index-1] != '{':
                    return False
                parentheses_dict['{'] = parentheses_dict.get('{', 0) - 1
            elif i == '[':
                parentheses_dict[i] = parentheses_dict.get(i, 0) + 1
            elif i == ']':
                if index != 0 and s[index-1] != '[':
                    return False
                parentheses_dict['['] = parentheses_dict.get('[', 0) - 1

        for v in parentheses_dict.values():
            if v != 0:
                return False
        return True

