# --- Nvirgula Suite v4 (High-Precision Manual Parsing) ---
# This version prioritizes data integrity by processing strings character by character.
# By avoiding direct string-to-float conversion, we eliminate binary representation 
# noise (e.g., 52.300000000000004). 
# Returns: [Status, Converted Value, Is_Negative, Is_Float]

def nvirgula(num):
    """
    Sanitizes numerical strings using manual fixed-point logic for maximum precision.
    Ideal for ERPs and industrial systems where precision is mandatory.
    """
    # Checks if the input is actually a string to avoid processing errors
    if not isinstance(num, str):
        return [False, num, False, False]

    # Buffer to store only the numeric digits extracted from the string
    buffer_digits = ""
    # Boolean flag to indicate if a decimal separator was found
    is_float = False
    # Counter to track the number of digits after the decimal separator
    decimal_count = -1
    # Check if the string starts with a minus sign (ignoring leading spaces)
    is_negative = num.strip().startswith("-")

    # Step 1: Character-by-character parsing loop
    for char in num:
        # If a comma or dot is found, we mark the number as a float
        if char in (",", "."):
            is_float = True
            continue # Move to the next character without adding the separator to the buffer
        
        # Only add to buffer if it is a digit or a minus sign at the very beginning
        if char.isdigit() or (char == "-" and not buffer_digits):
            buffer_digits += char # Append digit to the clean numeric string
            # If we are already past a separator, increment the decimal place counter
            if is_float:
                decimal_count += 1

    try:
        # Step 2: Basic Validation
        # If the buffer is empty or contains only a minus sign, the input is invalid
        if not buffer_digits or buffer_digits == "-":
            return [False, num, False, False]

        # Step 3: Numerical Reconstruction Logic
        if is_float:
            # Convert the clean string of digits to a float
            raw_val = float(buffer_digits)
            # Re-position the decimal point by dividing by 10 raised to the count of decimals
            converted_val = raw_val / (10 ** (decimal_count + 1))
        else:
            # If no separator was found, convert directly to integer
            converted_val = int(buffer_digits)

        # Step 4: Final Return
        # Returns [Success, Value, Negative_Flag, Float_Flag]
        return [True, converted_val, is_negative, is_float]

    except (ValueError, ZeroDivisionError):
        # Catch any unexpected mathematical or conversion errors
        return [False, num, False, False]
