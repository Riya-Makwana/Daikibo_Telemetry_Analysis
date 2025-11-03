import json

def load_data(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    print(f"Loaded {len(data)} telemetry records")
    print("Sample Record:", data[0])
    return data
