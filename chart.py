import matplotlib.pyplot as plt
import os

def generate_bar_chart(values, analysis_results):
    # Filter only those keys present in analysis_results
    labels = [label for label in values if label in analysis_results]
    result_vals = [values[label] for label in labels]
    colors = []

    for label in labels:
        status = analysis_results[label]["status"]
        if status == "Normal":
            colors.append("green")
        elif status == "High":
            colors.append("red")
        elif status == "Low":
            colors.append("orange")
        else:
            colors.append("gray")

    plt.figure(figsize=(10, 5))
    bars = plt.bar(labels, result_vals, color=colors)

    for i, bar in enumerate(bars):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height + 5, f"{height:.1f}", ha='center', va='bottom')

    plt.ylabel("Values")
    plt.title("Health Marker Chart")
    plt.xticks(rotation=45)

    chart_path = "temp_chart.png"
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()
    return chart_path
