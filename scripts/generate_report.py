import os

# Ensure the reports directory exists
os.makedirs("reports", exist_ok=True)

# Path for the report
report_path = "reports/model_report.txt"

# Dummy content for now — replace with real report if needed
with open(report_path, "w") as f:
    f.write("Model Report\n")
    f.write("====================\n")
    f.write("Accuracy: 92%\n")
    f.write("Precision: 89%\n")
    f.write("Recall: 90%\n")

print(f"Report generated at: {report_path}")
