---
layout: page
title: Home
permalink: /
---

# Social Data Analysis and Visualization 




# **Vehicle Theft in San Francisco: A Tale of Two Decades**

In the bustling streets of San Francisco, vehicle theft remains a persistent urban challenge that affects residents and visitors alike. This analysis delves into an extensive dataset from the San Francisco Police Department, combining historical records from 2003 to 2018 with contemporary data through present day.
Our dataset captures every reported vehicle theft incident, including crucial details such as the location, timing, and police district response. This comprehensive view allows us to track not just the raw numbers, but also understand the geographical and temporal patterns that shape vehicle crime in San Francisco.

# Time Series Trend Analysis (2003-2025)

![Vehicle Theft Trend](/vehicle_theft_trend.png)

*Figure 1: Yearly trends in vehicle thefts across San Francisco.*

Our first visualization reveals the ebb and flow of vehicle thefts across San Francisco over two decades. The time series plot is rendered in deep red to emphasize the gravity of these incidents.
The visualization highlights several key findings: First, an unprecedented peak of 18,103 thefts occurred in the early 2000s. This period coincides with the pre-smartphone era when vehicle security systems were less sophisticated. Second, a sharp decline occurred from 2005 to 2006, with theft numbers dropping dramatically from approximately 18,000 to 7,000. This significant reduction might be attributed to the implementation of new police strategies, improvements in vehicle anti-theft technology, and the introduction of better security systems.
Third, a steady decline period from 2006 to 2010 showed a gradual decrease to around 4,500 thefts. During 2011-2019, the trend shifted to show a moderate increase followed by fluctuating patterns, with thefts hovering between 5,000 and 8,000 annually. These small peaks and valleys suggest seasonal patterns in vehicle theft activity. Finally, the period from 2020 to 2025 exhibited notable fluctuations, particularly during the pandemic years, reflecting the unusual circumstances and changing urban dynamics of this period.


# Vehicle Thefts by District

![Vehicle Theft by District](/vehicle_theft_by_district.png)

*Figure 2: Theft distribution across San Francisco districts.*

Our second visualization presents a horizontal bar chart showing the distribution of vehicle thefts across San Francisco's police districts. The top three high-risk districts account for 47% of total thefts: Ingleside (20,546 thefts, 16.3%), Mission (17,297 thefts, 13.7%), and Bayview (16,780 thefts, 13.3%). These districts consistently showed high theft rates, particularly during the peak years of the early 2000s, when overall city thefts reached 18,103 annually.



```python

import pandas as pd
import matplotlib.pyplot as plt
import os
import sys


def check_file_exists(filename):
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found. Please make sure the file exists in the docs/data directory.")
        sys.exit(1)

try:
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, 'data')

    # Check if required files exist
    print("\nLoading data sources...")
    historical_file = os.path.join(data_dir, 'Police_Department_Incident_Reports__Historical_2003_to_May_2018_20250325.csv')
    recent_file = os.path.join(data_dir, 'Police_Department_Incident_Reports__2018_to_Present_20250325.csv')

    check_file_exists(historical_file)
    check_file_exists(recent_file)

    # Read and process the data
    print("Loading datasets...")
    historical_df = pd.read_csv(historical_file)
    recent_df = pd.read_csv(recent_file)

    # Process dates for historical dataset
    print("\nProcessing dates...")
    if 'Date' in historical_df.columns:
        historical_df['Date'] = pd.to_datetime(historical_df['Date'])
    elif 'Report Datetime' in historical_df.columns:
        historical_df['Date'] = pd.to_datetime(historical_df['Report Datetime'])

    # Process dates for recent dataset
    if 'Incident Datetime' in recent_df.columns:
        recent_df['Date'] = pd.to_datetime(recent_df['Incident Datetime'])
    elif 'Incident Date' in recent_df.columns:
        recent_df['Date'] = pd.to_datetime(recent_df['Incident Date'])

    # Harmonize category names and filter vehicle thefts
    print("\nHarmonizing categories...")
    historical_vehicle_theft = historical_df[historical_df['Category'] == 'VEHICLE THEFT'].copy()

    # For recent data, handle both possible category column names
    if 'Incident Category' in recent_df.columns:
        recent_vehicle_theft = recent_df[recent_df['Incident Category'].str.contains('Vehicle Theft', case=False, na=False)].copy()
    else:
        recent_vehicle_theft = recent_df[recent_df['Category'].str.contains('Vehicle Theft', case=False, na=False)].copy()

    # Combine datasets
    print("\nCombining datasets...")
    vehicle_theft_df = pd.concat([historical_vehicle_theft, recent_vehicle_theft], ignore_index=True)

    # Filter out future dates
    current_date = pd.Timestamp.now()
    vehicle_theft_df = vehicle_theft_df[vehicle_theft_df['Date'] <= current_date]

    # Extract time components
    vehicle_theft_df['Year'] = vehicle_theft_df['Date'].dt.year
    vehicle_theft_df['Month'] = vehicle_theft_df['Date'].dt.month

    print(f"\nCombined data range: {vehicle_theft_df['Date'].min()} to {vehicle_theft_df['Date'].max()}")
    print(f"Total vehicle theft records: {len(vehicle_theft_df)}")

    # Create visualizations
    plt.style.use('seaborn-v0_8')

    # 1. Time Series Plot
    plt.figure(figsize=(15, 8))
    yearly_thefts = vehicle_theft_df.groupby('Year').size().reset_index(name='count')

    plt.fill_between(yearly_thefts['Year'], yearly_thefts['count'], 
                     color='darkred', alpha=0.3)
    plt.plot(yearly_thefts['Year'], yearly_thefts['count'], 
             marker='o', linewidth=2, color='darkred')

    plt.xticks(yearly_thefts['Year'], rotation=45)

    peak_year = yearly_thefts.loc[yearly_thefts['count'].idxmax()]
    plt.annotate(f'Peak: {int(peak_year["count"]):,} thefts',
                 xy=(peak_year['Year'], peak_year['count']),
                 xytext=(10, 10), textcoords='offset points',
                 bbox=dict(facecolor='white', edgecolor='darkred', alpha=0.7))

    plt.grid(True, alpha=0.3)

    start_year = int(vehicle_theft_df['Year'].min())
    end_year = int(vehicle_theft_df['Year'].max())
    plt.title(f'Vehicle Theft Trends in San Francisco ({start_year}-{end_year})', pad=20, fontsize=14)
    plt.xlabel('Year')
    plt.ylabel('Number of Vehicle Thefts')
    plt.tight_layout()
    plt.savefig('vehicle_theft_trend.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 2. District Bar Chart
    plt.figure(figsize=(15, 8))

    if 'PdDistrict' in vehicle_theft_df.columns:
        vehicle_theft_df.rename(columns={'PdDistrict': 'District'}, inplace=True)
    elif 'Police District' in vehicle_theft_df.columns:
        vehicle_theft_df.rename(columns={'Police District': 'District'}, inplace=True)

    district_counts = vehicle_theft_df.groupby('District').size().sort_values(ascending=True)
    bars = plt.barh(range(len(district_counts)), district_counts.values, color='darkred', alpha=0.7)
    plt.yticks(range(len(district_counts)), district_counts.index)

    for i, v in enumerate(district_counts.values):
        plt.text(v, i, f' {v:,}', va='center', fontsize=10)

    plt.title('Vehicle Thefts by District in San Francisco', pad=20, fontsize=14)
    plt.xlabel('Number of Vehicle Thefts')
    plt.ylabel('District')
    plt.tight_layout()
    plt.savefig('vehicle_theft_by_district.png', dpi=300, bbox_inches='tight')
    plt.close()

    # Print key statistics
    print("\nKey Findings:")
    print(f"Total vehicle thefts ({start_year}-{end_year}): {len(vehicle_theft_df):,}")
    print(f"Peak year: {int(peak_year['Year'])} with {int(peak_year['count']):,} thefts")
    print(f"Average yearly thefts: {int(yearly_thefts['count'].mean()):,}")

    print("\nDistrict Analysis:")
    for district, count in district_counts.items():
        percentage = (count / len(vehicle_theft_df)) * 100
        print(f"{district}: {count:,} thefts ({percentage:.1f}%)")

    recent_trend = yearly_thefts.iloc[-3:]  # Last 3 years
    trend_change = ((recent_trend['count'].iloc[-1] - recent_trend['count'].iloc[0]) 
                    / recent_trend['count'].iloc[0] * 100)
    print(f"\nRecent trend (last 3 years): {trend_change:+.1f}% change")

except Exception as e:
    print(f"\nAn error occurred: {str(e)}")
    print("Please ensure all required packages are installed:")
    print("pip install pandas matplotlib")
    sys.exit(1)

```


# One map



# One interactive visualization in Bokeh

