class Solution:
    def decodeString(self, s: str) -> str:
        stack = [] # Doing LIFO
        currentString = ""
        currentNumber = 0

            #  3[a2[c3[b]]]
        for char in s: # 3, [, a, 2, [, c, 3, [
            if char.isdigit(): # is number
                currentNumber  = currentNumber  * 10 + int(char) # 3, 2, 3
            elif char == '[': # Pop on current values
                stack.append((currentString, currentNumber)) # [(“”, 3)], [(“”, 3), (“a”, 2)], [[(“”, 3), (“a”, 2), (“c”, 3)]
                currentString = ""
                currentNumber = 0
            elif char == ']': # End bracket, pop off
                # c,3/a,2/””,3
                lastString, lastNumber = stack.pop()
                # c + 3 * “b” = cbbb/ a + 2 * cbbb = acbbbcbbb/ “”+ 3 * acbbbcbbbacbbbcbbbacbbbcbbb
                currentString = lastString + lastNumber * currentString 
            else: # Regular char
                # “a”, “c”, “b”
                currentString += char 


        return currentString

        