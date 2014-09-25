class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        word_list = s.strip().split(' ')
        return  ' '.join(reversed(filter(None,word_list)))
