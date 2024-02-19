#!/usr/bin/env python3
# This python script takes First Name and Last Name and generate a list of permutatopn as output.
# Usage 1: ./username-generator.py <Username_list.txt>
# ** Username list should contain Firstname and Lastname on each line **
#   Example:
#   Zed Smith
#   Ted Harry
#
#
# Usage 2: ./username-generator.py <First Name> <Last Name>
#
#
# Output > username_list.txt

import sys

def generate_usernames(fname, lname):
    # Generate permutations of usernames
    usernames = []
    
    # ZedSmith, Zedsmith, zedsmith
    usernames.append(fname.capitalize() + lname.capitalize())
    usernames.append(fname.capitalize() + lname.lower())
    usernames.append(fname.lower() + lname.lower())
    
    # Zed.Smith, Zed.smith, zed.smith
    usernames.append(fname.capitalize() + '.' + lname.capitalize())
    usernames.append(fname.capitalize() + '.' + lname.lower())
    usernames.append(fname.lower() + '.' + lname.lower())

    # Zed-Smith, Zed-smith, zed-smith
    usernames.append(fname.capitalize() + '-' + lname.capitalize())
    usernames.append(fname.capitalize() + '-' + lname.lower())
    usernames.append(fname.lower() + '-' + lname.lower())

    # Zed_Smith, Zed_smith, zed_smith
    usernames.append(fname.capitalize() + '_' + lname.capitalize())
    usernames.append(fname.capitalize() + '_' + lname.lower())
    usernames.append(fname.lower() + '_' + lname.lower())

    # ZSmith, Zsmith, zsmith
    usernames.append(fname[0].upper() + lname.capitalize())
    usernames.append(fname[0].upper() + lname.lower())
    usernames.append(fname[0].lower() + lname.lower())

    # Z.Smith, Z.smith, z.smith
    usernames.append(fname[0].upper() + '.' + lname.capitalize())
    usernames.append(fname[0].upper() + '.' + lname.lower())
    usernames.append(fname[0].lower() + '.' + lname.lower())

    # Z-Smith, Z-smith, z-smith
    usernames.append(fname[0].upper() + '-' + lname.capitalize())
    usernames.append(fname[0].upper() + '-' + lname.lower())
    usernames.append(fname[0].lower() + '-' + lname.lower()) 

    # Z_Smith, Z_smith, z_smith
    usernames.append(fname[0].upper() + '_' + lname.capitalize())
    usernames.append(fname[0].upper() + '_' + lname.lower())
    usernames.append(fname[0].lower() + '_' + lname.lower())

    # ZedS, Zeds, zeds
    usernames.append(fname.capitalize() + lname[0].upper())
    usernames.append(fname.capitalize() + lname[0].lower())
    usernames.append(fname.lower() + lname[0].lower())
    
    # Zed.S, Zed.s, zed.s
    usernames.append(fname.capitalize() + '.' + lname[0].upper())
    usernames.append(fname.capitalize() + '.' + lname[0].lower())
    usernames.append(fname.lower() + '.' + lname[0].lower())
    
    # Return the list of generated usernames
    return usernames

def generate_output(usernames):
    with open('username_list.txt', 'w') as file:
        for username in usernames:
            file.write(username + '\n')

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) == 2:
        file_input = sys.argv[1]
        usernames_list = []
        total_usernames_list = []
        with open(file_input, 'r') as file:
            for line in file:
                fname, lname = line.strip().split()
                usernames_list = generate_usernames(fname, lname)
                total_usernames_list += usernames_list    
            generate_output(total_usernames_list)
            print("Permuatation Finish!")
            print("Output: username_list.txt")

    elif len(sys.argv) == 3:
        print("Usage: python script.py <fname> <lname>")
        sys.exit(1)

        fname = sys.argv[1]
        lname = sys.argv[2]

        # Generate usernames
        usernames = generate_usernames(fname, lname)
        generate_output(usernames)
        print("Permuatation Finish!")
        print("Output: username_list.txt")
    
    else: sys.exit(1)
