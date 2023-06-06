class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        reverse_words=[]
        empty = ''
        for char in s:
            if char != ' ':
                empty+=char
            else:
                reverse_words.append(empty)
                empty=''
        reverse_words.append(empty)
        ans_list=[]
        for i in range(len(reverse_words)-1,-1,-1):
            if reverse_words[i] :
                ans_list.append(reverse_words[i])
        ans_string=' '.join(ans_list)
        return ans_string
    
obj=Solution()
print(obj.reverseWords(s = "the sky is blue"))
print(obj.reverseWords(s = "  hello world  "))
print(obj.reverseWords(s = "a good   example"))