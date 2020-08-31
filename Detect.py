class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.isupper() or word.islower() or word.istitle()
val=Solution()
s=input()
if(val.detectCapitalUse(s)):
  print('yes')
else:
  print('no')
