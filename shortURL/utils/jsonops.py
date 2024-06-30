import json
import os


def jsonFileHandle(file_path) :
    def read() :
        if not os.path.exists(file_path) :
            return []
        try :
            with open(file_path, 'r') as file :
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError) :
            return []

    def write(new_data) :
        temp = read()
        for entry in temp :
            if new_data['short_id'] == entry['short_id'] :
                raise ValueError(f"Entry with short_id {new_data['short_id']} already exists.")

        temp.append(new_data)

        with open(file_path, 'w') as file :
            json.dump(temp, file, indent=4)

    return read, write

def dicttojson(dict) :
    return json.dumps(dict)



if __name__ == '__main__' :
    file_path = '/ShiftURL/demo.json'

    # Get the read and write functions
    jsonRead, jsonWrite = jsonFileHandle(file_path)

    try :
        # Append new data
        new_entry = {
            'short_id' : '01J0YZ1NKYV1CDTQCV1K4ABD897',
            'original_url': 'https://example.com',
            'clicks' : 18724,
            'created_at' : '1/5/2020'
        }
        jsonWrite(new_entry)
        print(f"Data successfully written to {file_path}")
    except ValueError as e :
        print(e)

    # Read the current data to verify
    data = jsonRead()
    print(data[-1])
