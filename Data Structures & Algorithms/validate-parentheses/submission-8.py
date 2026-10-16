class Solution:
    def isValid(self, s: str) -> bool:
        temp = {
            '(' : ')' , '{' : '}', '[' : ']'
        }
        lst = []
        b = False
        if len(s) == 1 or s[0] not in temp:
            return b
        for i in s:
            if i == "(" or i == "[" or i == "{":
                lst.append(i)
            elif len(lst) == 0:
                b = False
                break
            else:
                if i == temp[lst[-1]]:
                    lst.pop()
                    b = True
                    continue
                else:
                    b = False
                    break                    
        if len(lst) !=0:
            b = False
        return b