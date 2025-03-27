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


