import json
from collections import Counter

# Step 1: Load the JSON file
with open('daikibo_may2021_telemetry.json', 'r') as f:
    data = json.load(f)

# Step 2: Filter records where status is 'broken'
broken_records = [d for d in data if d.get('status') == 'broken']

# Step 3: Count breakdowns by factory
factory_breakdowns = Counter(d['factory'] for d in broken_records)

# Step 4: Find the factory with the most breakdowns
worst_factory, max_breaks = factory_breakdowns.most_common(1)[0]

print("Factory with the most breakdowns:")
print(f"{worst_factory} → {max_breaks} breakdowns\n")

# Step 5: Within that factory, count breakdowns by machine type
machine_breakdowns = Counter(
    d['machine_type'] for d in broken_records if d['factory'] == worst_factory
)

print(f"🔧 Machines that broke most often in {worst_factory}:")
for machine, count in machine_breakdowns.most_common(5):  # Top 5
    print(f"{machine}: {count} times")
