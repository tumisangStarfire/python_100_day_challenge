"""Working with files and directories"""
# TODO 1: for each name in the invited names list, replace the [name] with the actual name
# TODO 2: save the letters in a folder called ready to send


with open("./input/names/invited_names.txt", mode="r") as invited_names:
    guest_list = invited_names.read().splitlines()

    for guest in guest_list:
        letter_file = open("./input/letters/starting_letter.txt", "r")
        write_letter_to_file = open(f"./output/readyToSend/{guest}_letter.txt", "w")
        write_letter_to_file.write(letter_file.read().strip().replace("[name]",guest))
        write_letter_to_file.close()
        letter_file.close()


