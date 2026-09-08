class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        monotonic stack -> increasing version because the
        small bars from the past can create rectangles still into the future.
        larger bars will not be the bounder for the rectangle.

        walk right, add to stack until you find a bar that is smaller than or 
        equal to the top of the stack

        pop from stack until the top of the stack is smaller than the current bar
        use last popped index and current index to calculate width and height = current value

        greedy remember the highest area

        questions: what happens during situation where bar is equal to the stack? etc.
        '''

        stack = []
        best_area = 0

        # if len(heights) == 1: return heights[0]

        for i in range(len(heights)):
            # print("Iter", i, stack, best_area)
            j = i
            while stack and heights[i] <= stack[-1][1]:
                j, height = stack.pop()
                # print(j)
                width = i - j
                area = width * height
                if area > best_area:
                    best_area = area
            stack.append([j, heights[i]])

        i = len(heights)
        # print("Iter", i, stack, best_area)
        while stack:
            j, height = stack.pop()
            # print(j)
            width = i - j
            area = width * height
            if area > best_area:
                best_area = area
        # print("Done", stack, best_area)
        return best_area