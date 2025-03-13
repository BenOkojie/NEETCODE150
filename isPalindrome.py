    def isPalindrome(self, s: str) -> bool:
        backtrack = -1
        i=0
        print(len(s))
        while i in range(len(s)):
            if(backtrack*-1)>len(s):
                break
            if s[backtrack].isalpha() is False and s[backtrack].isnumeric() is False:
                backtrack-=1
                continue
            if s[i].isalpha() is False and s[i].isnumeric() is False:
                i+=1
                continue
            if s[i].lower() !=s[backtrack].lower():
                print(s[i])
                print(s[backtrack])
                return False
            backtrack-=1
            i+=1

        return True
