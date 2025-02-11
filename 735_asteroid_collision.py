class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # if the asteroid in my asteroids is < 0 and the one in my stack is > 0
        # i have to check for collision then
        my_stack = []
        for i in asteroids:
            while my_stack and i < 0 and my_stack[-1] > 0:
                diff = i + my_stack[-1]
                if diff == 0:
                    my_stack.pop()
                    break
                elif diff < 0:
                    my_stack.pop()
                else:
                    break
            else:
                my_stack.append(i)
        return my_stack