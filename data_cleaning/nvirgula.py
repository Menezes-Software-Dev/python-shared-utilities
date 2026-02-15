# --- Nvirgula Suite v3 (Mature Manual Logic) ---
# A consolidated version of the manual logic suite. This function returns 
# a detailed metadata list: [Status, Converted Value, Is_Negative, Is_Decimal].
# It is designed to be highly descriptive, allowing for complex business logic.

def nvirgula(num):    
    # Advanced handler that validates numbers and returns specific type metadata.
    ler1 = ""                                # Variable declaration
    ler2 = 0                                 # Variable declaration
    ref = -1                                 # Variable declaration
    dj = False                               # Variable declaration
    
    for ler in num:                          # Reads characters from the input text
        if ler == "," or ler == ".":         # Detects comma (,) or dot (.)
            ler = ""                         # Cleans separators
            ler2 = 1                         # Flags that a separator was detected
        if ler2 == 1:                        # If separator was found
            ref = ref + 1                    # Counts decimal places after the separator
        ler1 = ler1 + ler                    # Builds the clean number string
    
    dj = ler1.isdigit()                      # Checks if the string consists of positive digits
    if dj == False:                          # If not a positive integer string
        try:
            float(ler1)                      # Test for negative numbers
            dj = 3                           # Flags that a negative value was detected
        except:
            dj = False                       # Not a valid numerical value
            
    # Return Rule: [Success, Converted Value, Is_Negative, Is_Decimal]
    
    if dj == True and ler2 == 1:             # Case: Positive Decimal (Float)
        ler1 = float(ler1) / (10**ref)       # Applies decimal logic
        return [True, ler1, False, True]     # Returns: [True, float_val, False, True]
    
    if dj == True and ler2 == 0:             # Case: Positive Integer (Int)
        ler1 = float(ler1)                   # Internal float conversion
        return [True, int(ler1), False, False] # Returns: [True, int_val, False, False]

    if dj == 3 and ler2 == 1:                # Case: Negative Decimal (Float)
        ler1 = float(ler1) / (10**ref)       # Applies decimal logic to negative value
        return [True, ler1, True, True]      # Returns: [True, float_val, True, True]
    
    if dj == 3 and ler2 == 0:                # Case: Negative Integer (Int)
        ler1 = float(ler1)                   # Internal float conversion
        return [True, int(ler1), True, False] # Returns: [True, int_val, True, False]
        
    if dj == False:                          # Case: Validation Failure
        return [False, num, False, False]    # Returns: [False, original_input, False, False]
