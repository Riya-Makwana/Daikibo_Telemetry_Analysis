from load_data import load_data
from analyze_breakdowns import analyze_breakdowns
from visualize_reports import create_reports

if __name__ == "__main__":
    filepath = "data/daikibo_may2021_telemetry.json"
    data = load_data(filepath)
    factory_counts, worst_factory, machine_counts = analyze_breakdowns(data)
    create_reports(factory_counts, worst_factory, machine_counts, data)
