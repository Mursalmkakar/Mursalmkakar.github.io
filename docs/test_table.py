import pandas as pd

# Define your data
data = {
    "Task": [
        "Build website",
        "Time Series Trend Analysis (2003-2024)",
        "Vehicle Thefts by District",
        "Mapping of total vehicle theft reports",
        "Interactive Vehicle Theft Hotspots Map"
    ],
    "Student": [
        "s240362",
        "s240362",
        "s240362",
        "s233914",
        "s242715"
    ]
}

# Create the DataFrame
df = pd.DataFrame(data)

# Print the table to the terminal
print(df)

# Export the table to CSV
df.to_csv("task_table.csv", index=False)
