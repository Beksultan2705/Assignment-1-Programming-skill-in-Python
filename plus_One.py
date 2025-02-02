class Solution(object):
    def plusOne(self, digits):
        string = ""
        for d in digits:
            string += str(d)
        
        i = int(string) + 1 
        result = [int(w) for w in str(i)]
        
        return result
