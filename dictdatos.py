import json

def json_to_dict(json_file_path, encoding='utf-8'):
    try:
        with open(json_file_path, 'r', encoding=encoding) as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: File '{json_file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{json_file_path}'.")
        return None

def dict_to_json(data_dict, output_file_path, encoding='utf-8'):
    try:
        with open(output_file_path, 'w', encoding=encoding) as output_file:
            json.dump(data_dict, output_file, indent=2, ensure_ascii=False)
        print(f"Data dictionary successfully written to '{output_file_path}'.")
    except Exception as e:
        print(f"Error writing to '{output_file_path}': {e}")

if __name__ == "__main__":
    # Replace 'your_dataset.json' with the actual path to your JSON file
    input_json_file = 'dataset.json'

    data_dict = json_to_dict(input_json_file)

    if data_dict:
        print("Data Dictionary:")
        print(data_dict)

        # Replace 'output_data.json' with the desired output file path
        output_json_file = 'output_data.json'

        dict_to_json(data_dict, output_json_file)
