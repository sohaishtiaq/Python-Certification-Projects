def hanoi_solver(no_of_disks):
    rod1 = [disk for disk in range(no_of_disks, 0, -1)]
    rod2 = []
    rod3 = []

    def get_lists_string():
        return f"{rod1} {rod2} {rod3}\n"

    def move_disk(start, target):
        if not start:
            return
        target.append(start.pop())

    def move_tower(start, auxiliary, target, n):
        if n == 1:
            move_disk(start, target)
            return get_lists_string()

        result = ''

        result += move_tower(start, target, auxiliary, n - 1)

        move_disk(start, target)
        result += get_lists_string()

        result += move_tower(auxiliary, start, target, n - 1)

        return result

    return_str = get_lists_string()

    if no_of_disks > 0:
        return_str += move_tower(rod1, rod2, rod3, no_of_disks)

    return return_str.strip()
