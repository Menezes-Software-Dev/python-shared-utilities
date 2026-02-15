# --- Nvirgula Suite v2 ---
# A specialized collection of functions designed to bridge the gap between diverse 
# user inputs (using commas or dots) and system-ready numerical formats. 
# This version implements manual string parsing to demonstrate core algorithmic logic.
    
 def nvirgula_float(num):    
    # Function to handle and convert numerical strings with commas or dots into float format.
    ler1 = ""                                # Variable declaration
    ler2 = 0                                 # Variable declaration
    ref = -1                                 # Variable declaration
    dj = False                               # Variable declaration
    
    for char in num:                         # Reads the characters from the input text
        if char == "," or char == ".":       # Detects comma (,) or dot (.) entered by the user
            char = ""                        # Cleans commas and dots
            ler2 = 1                         # Flags that a separator was detected
        if ler2 == 1:                        # If separator was found
            ref = ref + 1                    # Counts decimal places after the separator
        ler1 = ler1 + char                   # Builds a string with the clean number (no dots/commas)
    
    dj = ler1.isdigit()                      # Checks if the string consists only of digits
    if dj == False:                          # If it does not contain only digits
        try:
            float(ler1)                      # Test for negative numbers
            dj = True                        # Flags that it is a valid numerical value
        except:
            dj = False                       # If it's not a valid number
            
    if dj == True and ler2 == 1:             # If valid and has a separator
        ler1 = float(ler1) / (10**ref)       # Converts to float and applies decimal logic
        return [True, ler1]                  # Returns: [Success Status, Float Value]
    
    if dj == True and ler2 == 0:             # If valid and no separator
        ler1 = float(ler1)                   # Simple float conversion
        return [True, ler1]                  # Returns: [Success Status, Float Value]
        
    if dj == False:                          # If not a valid number
        return [dj, num]                     # Returns: [False Status, Original Input String]

def nvirgula_int(num):    
    # Processes the string and returns the value as an integer.
    ler1 = ""                                # Variable declaration
    ler2 = 0                                 # Variable declaration
    ref = -1                                 # Variable declaration
    
    for char in num:                         # Reads the characters from the input text
        if char == "," or char == ".":       # Detects comma (,) or dot (.) entered by the user
            char = ""                        # Cleans commas and dots
            ler2 = 1                         # Flags that a separator was detected
        if ler2 == 1:                        # If separator was found
            ref = ref + 1                    # Counts decimal places after the separator
        ler1 = ler1 + char                   # Builds a string with the clean number (no dots/commas)
        
    dj = ler1.isdigit()                      # Checks if the string consists only of digits
    if dj == False:
        try:
            int(ler1)                        # Test for negative integer
            dj = True
        except:
            dj = False
            
    if dj == True and ler2 == 1:             # If valid and has a separator
        ler1 = float(ler1) / (10**ref)       # Applies decimal logic
        ler1 = int(ler1)                     # Converts to integer
        return [True, ler1]                  # Returns: [Success Status, Integer Value]
    
    if dj == True and ler2 == 0:             # If valid and no separator
        ler1 = int(ler1)                     # Simple integer conversion
        return [True, ler1]                  # Returns: [Success Status, Integer Value]
        
    if dj == False:                          # If not a valid number
        return [dj, num]                     # Returns: [False Status, Original Input String]

def nvirgula_int_str(num):    
    # Converts input to integer and returns it as a string.
    ler1 = ""                                # Variable declaration
    ler2 = 0                                 # Variable declaration
    ref = -1                                 # Variable declaration
    
    for char in num:                         # Reads the characters from the input text
        if char == "," or char == ".":       # Detects comma (,) or dot (.) entered by the user
            char = ""                        # Cleans commas and dots
            ler2 = 1                         # Flags that a separator was detected
        if ler2 == 1:                        # If separator was found
            ref = ref + 1                    # Counts decimal places after the separator
        ler1 = ler1 + char                   # Builds a string with the clean number (no dots/commas)
        
    dj = ler1.isdigit()                      # Checks if it consists only of digits
    if dj == True and ler2 == 1:             # If valid with separator
        ler1 = int(float(ler1) / (10**ref))
        return [True, str(ler1)]             # Returns: [Success Status, Value as String]
        
    if dj == True and ler2 == 0:             # If valid without separator
        ler1 = int(ler1)
        return [True, str(ler1)]             # Returns: [Success Status, Value as String]
        
    if dj == False:                          # If not valid
        return [dj, num]                     # Returns: [False Status, Original Input String]
