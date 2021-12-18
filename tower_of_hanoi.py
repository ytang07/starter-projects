def tower_of_hanoi(disks, start, middle, end):
    if disks == 1:
        print(f"Move disk 1 from {start} to {end}")
        return
    tower_of_hanoi(disks-1, start, end, middle)
    print(f"Move disk {disks} from {start} to {end}")
    tower_of_hanoi(disks-1, middle, start, end)

number_of_disks = 3
tower_of_hanoi(number_of_disks, 'A', 'B', 'C')