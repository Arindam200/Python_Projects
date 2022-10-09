def isValid(self, s) :
        stk = []
        flag = True
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stk.append(s[i])
            elif s[i] == ")" or s[i] == "}" or s[i] == "]":
                if len(stk) == 0:
                    flag = False
                    break
                else:
                    if s[i] == ")" and stk[-1] == "(":
                        stk.pop()
                    elif s[i] == "}" and stk[-1] == "{":
                        stk.pop()
                    elif s[i] == "]" and stk[-1] == "[":
                        stk.pop()
                    else:
                        flag = False
                        break
        return flag if len(stk) == 0 else False