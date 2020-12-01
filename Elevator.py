import time

def door():
    door_open = int(input('Press 1 to open the door: '))
    if door_open != 1:
        print('Please press 1 to open the door.')
        door_open = int(input('Press 1 to open the door: '))
    else:
        print('The door is opening.')
        time.sleep(2)


def up():
    door()
    current_floor = int(input('Enter the current floor: '))
    dest_floor = int(input('Please choose from 1 to 10: '))
    if current_floor > dest_floor:
        print('Already in the highest floor.')
        dest_floor = int(input('Please choose from 1 to 10: '))
        time.sleep(1)
    elif current_floor == dest_floor:
        print('Already on your destination floor.')
        dest_floor = int(input('Please choose from 1 to 10: '))
    else:
        print('Closing the door.')
        time.sleep(2)

    if dest_floor >= 10:
        print('Already in the highest floor.')
    else:
        while dest_floor > current_floor:
            current_floor += 1
            print('Current floor is', current_floor, '.')
            time.sleep(2)

    print('Opening the door.')


def down():
    door()
    current_floor = int(input('Enter you current floor: '))
    dest_floor = int(input('Please choose from 1 to 10: '))
    if dest_floor > current_floor:
        print("Already in lower level.")
        dest_floor = int(input('Please choose from 1 to 10: '))
        time.sleep(1)
    elif current_floor == dest_floor:
        print('Already on your destination floor.')
        dest_floor = int(input('Please choose from 1 to 10: '))
        time.sleep(1)
    else:
        print('Closing the door.')
        time.sleep(3)

    if current_floor <= 1:
        print("Already on lower floor.")
    else:
        while dest_floor < current_floor:
            current_floor -= 1
            print('Current floor is', current_floor, '.')
            time.sleep(2)
    print('Opening the door.')


def main():
    while True:
        print('1 = Going UP, 0 = Going DOWN')
        button = int(input('Enter 1 to GO UP and 0 to GO DOWN: '))
        if button == 1:
            print('Going UP!')
            up()
        elif button == 0:
            print('Going DOWN!')
            down()
        else:
            print('Wrong button pressed. ')
        break

main()









