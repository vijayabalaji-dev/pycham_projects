#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./input/Names/invited_names.txt") as file:
    names_from_file = file.readlines()
    names = []

    for name_in_file in names_from_file:
        new_name = name_in_file.strip()
        names.append(new_name)
    for name in names:
        new_file = open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w")
        txt = open("./Input/Letters/starting_letter.txt").read()
        new_txt = txt.replace("[name]", name)
        new_file.write(new_txt)
        




