s = input("Input: s = ")

class Solution:
    list_arab = [] ## it will be a list with corresponding values of arabic numders
    dict = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    def romanToInt(self, s: str) -> int:
        s = list(s) ## make a list of our string input
        self.list_arab.append(self.dict[s[0]])
        sum = 0
        ## Fill out list_arab with corresponding values of arabic numders.
        ## If a smaller value appears earlier than a bigger value, the smaller value must be substracted.
        for i in range(1, len(s)): 
            self.list_arab.append(self.dict[s[i]])
            if  self.list_arab[i-1] < self.list_arab[i]:
                self.list_arab[i-1] *= -1
        for i in range(len(self.list_arab)):
            sum += self.list_arab[i]
        return sum

    def Explanation(self, s: str): 
        ## make new lists and fill them with new values
        ## if next value and current are equal, they are combine.
        ## if next value less than current value, they are combine.
        new_s = []
        new_list_arab = []
        new_list_arab.append(self.list_arab[0])
        new_s.append(s[0])
        j = 1
        ## filling new lists
        for i in range(1, len(self.list_arab)):
            if self.list_arab[i] >= self.list_arab[i-1]:
                new_s[j-1] += s[i]
                new_list_arab[j-1] += self.list_arab[i]
            else:
                new_s.append(s[i])
                new_list_arab.append(self.list_arab[i])
                j += 1
        ## correct pleasant-to-eye output
        print("Explanation: ", end='')
        for j in range(len(new_list_arab)):
            if j == len(new_list_arab)-2:
                print(str(new_s[j]) + " = " + str(new_list_arab[j]) + " and ", end='')
            elif j == len(new_list_arab)-1:
                print(str(new_s[j]) + " = " + str(new_list_arab[j]) + ". ")
            else:
                print(str(new_s[j]) + " = " + str(new_list_arab[j]) + ", ", end='')
        return

result = Solution().romanToInt(s)
print("Output: ", result)
if (result > 10):
    Solution().Explanation(s)