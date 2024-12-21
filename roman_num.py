# Dictionary mapping Roman numeral characters to their corresponding decimal values
roman_to_decimal = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

# Function to convert Roman numerals to decimal.
def roman_to_int(roman):
    total = 0  # Initialize total to 0, this will hold the final decimal value.
    prev_value = 0  # Track the previous Roman numeral value to handle subtraction cases.

    # Validate input by filtering only valid Roman numeral characters and converting to uppercase.
    roman = ''.join([char.upper() for char in roman if char.upper() in roman_to_decimal])

    if not roman:  # If the string is empty after filtering, return 0 as it's invalid.
        return 0

    # Iterate through the Roman numeral string in reverse to calculate decimal value.
    for char in reversed(roman):
        value = roman_to_decimal.get(char, 0)  # Get the decimal value of the current Roman numeral.
        
        # If the current value is smaller than the previous one, subtract it (e.g., IV -> 4).
        if value < prev_value:
            total -= value
        else:  # Otherwise, add it to the total.
            total += value
        
        prev_value = value  # Update the previous value for the next iteration.

    return total  # Return the total decimal value.

# Function to convert numbers to words manually (only handles numbers from 0 to 9999).
def number_to_words(num):
    # Arrays for word representations of numbers.
    units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand"]

    if num == 0: 
        return "Zero"  # Handle zero case explicitly.

    result = ""  # Initialize the result string.

    # Process thousands place, if any.
    if num >= 1000:
        result += units[num // 1000] + " Thousand "  # Convert thousands to words.
        num %= 1000  # Remove the thousands place.

    # Process hundreds place, if any.
    if num >= 100:
        result += units[num // 100] + " Hundred "  # Convert hundreds to words.
        num %= 100  # Remove the hundreds place.
        if num > 0:
            result += ""  # Ensure proper spacing for tens/units.

    # Process tens and units place.
    if 10 < num < 20:  # Handle numbers between 11 and 19.
        result += teens[num - 10]
    else:
        result += tens[num // 10]  # Convert tens to words.
        if num % 10 > 0:  # If there is a unit, add it to the result.
            result += " " + units[num % 10]

    return result.strip()  # Return the result string after trimming any extra spaces.

# Function to read Roman numerals from a file.
def read_input_file(input_file):
    try:
        with open(input_file, 'r') as infile:  # Open the input file for reading.
            return [line.strip() for line in infile]  # Return a list of stripped lines.
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")  # Handle file not found error.
        return []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")  # Handle other exceptions.
        return []

# Function to write results to an output file.
def write_output_file(output_file, results):
    try:
        with open(output_file, 'w') as outfile:  # Open the output file for writing.
            for result in results:
                outfile.write(result + "\n")  # Write each result on a new line.
        print(f"Results successfully written to {output_file}.")  # Success message.
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")  # Handle write errors.

# Main function to process the file.
def process_file(input_file, output_file):
    try:
        roman_numerals = read_input_file(input_file)  # Read input file containing Roman numerals.
        results = []  # Initialize an array to store the results.

        for roman in roman_numerals:  # Iterate through each Roman numeral in the list.
            if roman:  # Ensure the line is not empty.
                decimal = roman_to_int(roman)  # Convert Roman numeral to decimal.
                if decimal == 0:
                    results.append("Invalid Roman numeral")  # Handle invalid Roman numeral.
                else:
                    words = number_to_words(decimal)  # Convert decimal to words.
                    results.append(words)  # Append the words result.

        write_output_file(output_file, results)  # Write the results to the output file.
        print("File processed successfully.")  # Success message.
    except Exception as e:
        print(f"An error occurred: {e}")  # Handle any unforeseen errors during processing.

# Process the file by calling the main function.
process_file('input.txt', 'output.txt')