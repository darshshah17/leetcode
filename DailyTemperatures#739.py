class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Explanation (did not solve myself):
        # for each num in temperatures, if the num is greater than 
        # the previous, then keep popping from the stack until the
        # top of the stack is >= the curr num. 
        # Each time before you pop, find the index diff between
        # the curr num and the top of stack and store it at index
        # of the top of stack
        # Note: we could technically comment out if temp[i-1] < temp[i]
        
        result = [0] * len(temperatures)
        stack = [(0, temperatures[0])] # stack will contain tuples (i, val)

        for i in range(1, len(temperatures)):
            if temperatures[i-1] < temperatures[i]:
                while len(stack) and stack[-1][1] < temperatures[i]:
                    result[stack[-1][0]] = i - stack[-1][0]
                    stack.pop()
            
            stack.append((i, temperatures[i]))

        return result


        
