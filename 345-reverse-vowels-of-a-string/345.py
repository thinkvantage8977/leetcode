class Solution(object):
    def reverseVowels(self, s):
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        vowelsInString = ""
        for c in s:
        	if c in vowels:
        		vowelsInString +=c
        vowelsInString = vowelsInString[::-1]
        
        print(vowelsInString)

        result = []
        count = 0
        for c in s:
        	if c in vowels:
        		result.append(vowelsInString[count])
        		count +=1
        	else:
        		result.append(c)

        print(result)

        return ''.join(result)


testClass = Solution()


print(testClass.reverseVowels("leetcode"))