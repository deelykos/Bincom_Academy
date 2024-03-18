def extract_names(filename):
    """Extracts first, middle, and last names from a file.

    Args:
        filename (str): The name of the file to read from.

    Raises:
        FileNotFoundError: If the file is not found.

    Returns:
        tuple: A tuple containing the first, middle, and last names.
    """
    try:
        with open(filename, 'r') as file:
            full_name = file.read().strip() # Removes leading/trailing whitespace
            full_name_split = full_name.split() # Converts the filename content to a list

            if len(full_name_split) == 2:
                first_name, last_name = full_name_split
                middle_name = None
            elif len(full_name_split) > 2:
                first_name = full_name_split[0]
                middle_name = " ".join(full_name_split[1:-1]) # Concatenates middle names if multiple
                last_name = full_name_split[-1]
            else:
                raise ValueError("Invalid name format.")
            return first_name, middle_name, last_name
    except FileNotFoundError:
        print(f"{filename} not found.")
        return None, None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None, None
    

first_name, middle_name, last_name = extract_names('full_name.txt')

print(f"First name: {first_name}")
print(f"Middle name: {middle_name}")
print(f"Last name: {last_name}")