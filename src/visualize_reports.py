import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def create_reports(factory_counts, worst_factory, machine_counts, data):
    """Generate charts, CSVs, and visual reports."""
    os.makedirs('reports', exist_ok=True)

    # 1. Factory Breakdown Summary
    df_factories = pd.DataFrame(factory_counts.items(), columns=['Factory', 'Breakdowns'])
    df_factories.to_csv('reports/factory_breakdowns_summary.csv', index=False)

    # Bar Chart - Factory Comparison
    plt.figure(figsize=(8,5))
    sns.barplot(x='Factory', y='Breakdowns', data=df_factories, palette='Blues_d')
    plt.title('Machine Breakdowns by Factory (May 2021)')
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig('reports/factory_comparison_chart.png')
    plt.close()

    # 2. Breakdown by Machines in Worst Factory
    df_machines = pd.DataFrame(machine_counts.items(), columns=['Machine', 'Breakdowns'])
    df_machines.to_csv(f'reports/{worst_factory.lower().replace(" ", "_")}_machines.csv', index=False)

    plt.figure(figsize=(8,5))
    sns.barplot(x='Machine', y='Breakdowns', data=df_machines, palette='Oranges')
    plt.title(f'Machine Breakdowns in {worst_factory}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'reports/{worst_factory.lower().replace(" ", "_")}_machines_chart.png')
    plt.close()

    # 3. Heatmap of Breakdowns by Factory & Machine (extra visual)
    df_all = pd.DataFrame([d for d in data if d.get('status') == 'broken'])

    if not df_all.empty:
        pivot = pd.crosstab(df_all['factory'], df_all['machine_type'])
        plt.figure(figsize=(10,6))
        sns.heatmap(pivot, cmap='coolwarm', annot=True, fmt='d')
        plt.title('Breakdowns Heatmap by Factory and Machine Type')
        plt.tight_layout()
        plt.savefig('reports/breakdowns_heatmap.png')
        plt.close()
        print("Heatmap saved: reports/breakdowns_heatmap.png")
    else:
        print("No 'broken' data found — skipping heatmap generation.")

    print("Reports generated successfully in 'reports/' folder.")
