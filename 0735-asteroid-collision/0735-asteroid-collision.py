class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids: # 10, 2, -5
            if asteroid > 0: # We know its pos
                stack.append(asteroid) # [10]/[10, 2]
            else: # Its neg, we need to check if we destroy n asteroids
                while stack and stack[-1] > 0 and stack[-1] < -asteroid: # neg asteroid destroy n asteroids
                    stack.pop() #[10]
                if stack and stack[-1] == -asteroid: # They are same, will destroy each other
                    stack.pop()
                elif not stack or stack[-1] < 0: # is neg, same sign as asteroid i, can append
                    stack.append(asteroid)


        return stack # [10]
        