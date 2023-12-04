import time

time1 = input("Your goal is to press enter again when 10 seconds has elapsed. \n Press enter when ready to start timer. ")
start = time.time()
time2 = input()
end = time.time()

difference = end - start
goal = 10

outcome = goal - difference

print(f"{difference} time has passed")

print(f"You are {outcome} seconds away from your goal")

