 # Function to handle and convert numerical strings with commas or dots into float format.
    
  def nvirgula(num):
    ler1 = ""                                # Variable declaration
    ler2 = 0                                 # Variable declaration
    ref = -1                                 # Variable declaration

    for ler in num:                          # Reads the characters from the input text
        if ler == "," or ler == ".":         # Detects comma (,) or dot (.) entered by the user
            ler = ""                         # Cleans commas and dots
            ler2 = 1                         # Flags that a separator was detected
        if ler2 == 1:                        # If separator was found
            ref = ref + 1                    # Counts decimal places after the separator
        ler1 = ler1 + ler                    # Builds a string with the clean number (no dots/commas)
    
    dj = ler1.isdigit()                      # Checks if the string consists only of digits
    if dj == True:                           # If it contains only digits
        ler1 = float(ler1) / (10**ref)       # Converts to float and divides by 10 raised to the decimal count
        return True, ler1                    # Returns True and the converted value
    if dj == False:                          # If it's not a valid number
        return dj                            # Returns False      
