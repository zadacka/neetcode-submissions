class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Note: don't need a stack at all (we never do if we're only pushing and peeking...)
        stack = [] # arrival times
        cars_and_speeds = list(zip(position, speed))
        cars_and_speeds = sorted(cars_and_speeds, reverse=True)
        for position, speed in cars_and_speeds:
            arrival_time = (target - position) / speed
            if stack and arrival_time <= stack[-1]:
                print(f"car {position}, {speed} would take {arrival_time}h so arrives with others at {stack[-1]}")
                pass
            else:
                print(f"car {position}, {speed} would take {arrival_time}h so arrives as part of a new group")
                stack.append(arrival_time)
        print(stack)
        return len(stack)
        