from collections import Counter

def analyze_breakdowns(data):
    broken = [d for d in data if d.get('status') == 'broken']
    factory_counts = Counter(d['factory'] for d in broken)
    worst_factory, max_breaks = factory_counts.most_common(1)[0]
    print(f"Worst Factory: {worst_factory} ({max_breaks} breakdowns)")
    machine_counts = Counter(
        d['machine_type'] for d in broken if d['factory'] == worst_factory
    )
    return factory_counts, worst_factory, machine_counts
