class Solution:
    def isValid(self, s: str) -> bool:
        match = {")":"(",
        "]":"[",
        "}":"{"}
        my_list = []

        for ch in s:
            if ch in match:
                if not my_list or my_list[-1] != match[ch]:
                    return False
                    
                my_list.pop()
            else:
                my_list.append(ch)
        
        return not my_list
        