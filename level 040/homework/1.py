def dirReduc(arr):
    #dictionary to store opposite directions
    opposites = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "EAST": "WEST",
        "WEST": "EAST"
    }

    # checking all directions
    i = 0  # this makes it start at the begining
    while i < len(arr) - 1:  # keep going as long as 'i' is less than the length of the list minus 1 (to avoid going into loop)
        # the current direction and the next direction checker
        if arr[i] == opposites[arr[i + 1]]:
            # If opposites, remove both
            del arr[i:i + 2]
            i = 0  # reset 'i' to start checking from the beginning again
        else:
            # If they aren't opposites, move on to the next direction
            i += 1 


    return arr    # Return 