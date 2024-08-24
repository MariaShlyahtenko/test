import sys
import json

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def save_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=1)

def fill_values(tests, values_dict):
    for test in tests:
        test_id = test['id']
        if test_id in values_dict:
            test['value'] = values_dict[test_id]
        if 'values' in test:
            fill_values(test['values'], values_dict)

if __name__ == "__main__":
    
    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    values_data = load_json(values_file)
    tests_data = load_json(tests_file)

    values_dict = {item['id']: item['value'] for item in values_data['values']}
    fill_values(tests_data['tests'], values_dict)
    save_json(tests_data, report_file)
