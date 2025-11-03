import json
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the JSON data
with open('daikibo_may2021_telemetry.json', 'r') as f:
    data = json.load(f)

# Step 2: Filter only records where machines broke
broken_records = [d for d in data if d.get('status') == 'broken']

# Step 3: Count breakdowns by factory
factory_breakdowns = Counter(d['factory'] for d in broken_records)

# Step 4: Convert to DataFrame for easy export
df_factories = pd.DataFrame(factory_breakdowns.items(), columns=['Factory', 'Breakdowns'])

# Step 5: Visualize factory breakdowns
plt.figure(figsize=(8,5))
plt.bar(df_factories['Factory'], df_factories['Breakdowns'])
plt.title('Machine Breakdowns by Factory (May 2021)')
plt.xlabel('Factory')
plt.ylabel('Number of Breakdowns')
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

# Step 6: Find factory with most breakdowns
worst_factory, max_breaks = factory_breakdowns.most_common(1)[0]
print(f"Factory with most breakdowns: {worst_factory} ({max_breaks})")

# Step 7: Count breakdowns by machine type in that factory
machine_breakdowns = Counter(
    d['machine_type'] for d in broken_records if d['factory'] == worst_factory
)

df_machines = pd.DataFrame(machine_breakdowns.items(), columns=['Machine_Type', 'Breakdowns'])

# Step 8: Visualize breakdowns by machine in worst factory
plt.figure(figsize=(8,5))
plt.bar(df_machines['Machine_Type'], df_machines['Breakdowns'], color='orange')
plt.title(f'Machine Breakdowns in {worst_factory}')
plt.xlabel('Machine Type')
plt.ylabel('Breakdowns')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 9: Export both summaries to CSV
df_factories.to_csv('factory_breakdowns_summary.csv', index=False)
df_machines.to_csv(f'{worst_factory.lower().replace(" ", "_")}_machine_breakdowns.csv', index=False)

print("\nCSV reports generated successfully:")
print("- factory_breakdowns_summary.csv")
print(f"- {worst_factory.lower().replace(' ', '_')}_machine_breakdowns.csv")
