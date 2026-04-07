# load input file
def load_input(file_path):
    # return file contents as a string or None on failure.
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read() # reads the entire file content into a single string
    except FileNotFoundError:
        print(f"Error: '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred while reading '{file_path}': {e}")
    return None

# split the input file into it's individual inputs
def split_data(content=list, separator=str):
    # returns list of non-empty data from string
    if not content:
        return []
    return [data for data in content.split(separator) if data.strip()]
