import json

# Step 1: Open and read the JSON file
with open('daikibo_may2021_telemetry.json', 'r') as f:
    data = json.load(f)

# Step 2: Print how many records were loaded
print(f"Total records: {len(data)}")

# Step 3: View the first few entries
for record in data[:3]:  # shows first 3 records
    print(record)
