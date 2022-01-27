import time
floors = 20
current_floor = 0
num = int(input('How namy?\n'))
destinations = []
for i in range(num):
    floor = int(input("[ + ] Floor \n"))
    destinations.append(floor)
destinations.sort()

for x in range(floors):
    print(f"Moving up. Floor {x}")
    for y in range(num):
                
        if destinations[y] == x:
            print(f"[ + ] Arrived floor {x}")
            time.sleep(5)

    time.sleep(3)
    if destinations[-1] == x:
        print(f"Final destination arrived. Floor {destinations[i]}")
        break