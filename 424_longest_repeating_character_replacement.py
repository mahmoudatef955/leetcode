class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1

        start = end = 0
        max_window = 0
        repeated_char = s[0]
        char_rep_count = 0
        char_map = {repeated_char: 1}

        while end < len(s) - 1:
            end += 1
            current_char = s[end]
            char_map[current_char] = char_map.get(current_char, 0) + 1

            if current_char != repeated_char and char_map[current_char] > char_map[repeated_char]:
                char_rep_count -= char_map[current_char] - 1
                char_rep_count += char_map[repeated_char]
                repeated_char = current_char
            elif current_char != repeated_char:
                char_rep_count += 1

            if end - start > max_window and char_rep_count <= k:
                max_window = end - start
            elif char_rep_count > k:
                start_char = s[start]
                char_map[start_char] = char_map[start_char] - 1
                start += 1
                if start_char != repeated_char:
                    char_rep_count -= 1

        return max_window + 1
