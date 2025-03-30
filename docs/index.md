---

layout: page
title: Home
permalink: /
styles:
  - /assets/css/custom.css

---

<style>
body {
    background-image: url('/Mursalmkakar.github.io/assets/images/pic1.jpg');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

.page-content {
    background-color: rgba(255, 255, 255, 0.9);
    padding: 20px;
    border-radius: 10px;
}
</style>


# **Vehicle Theft in San Francisco: A Tale of Two Decades**

In the bustling streets of San Francisco, vehicle theft remains a persistent urban challenge that affects residents and visitors alike. This analysis delves into an extensive dataset from the San Francisco Police Department, combining historical records from 2003 to 2018 with contemporary data through present day.
Our dataset captures every reported vehicle theft incident, including crucial details such as the location, timing, and police district response. This comprehensive view allows us to track not just the raw numbers, but also understand the geographical and temporal patterns that shape vehicle crime in San Francisco.

# Time Series Trend Analysis (2003-2024)

![Vehicle Theft Trend](/vehicle_theft_trend.png)

*Figure 1: Yearly trends in vehicle thefts across San Francisco.*

Our first visualization reveals the ebb and flow of vehicle thefts across San Francisco over two decades. The time series plot is rendered in deep red to emphasize the gravity of these incidents.
The visualization highlights several key findings: First, an unprecedented peak of 18,103 thefts occurred in the early 2000s. This period coincides with the pre-smartphone era when vehicle security systems were less sophisticated. Second, a sharp decline occurred from 2005 to 2006, with theft numbers dropping dramatically from approximately 18,000 to 7,000. This significant reduction might be attributed to the implementation of new police strategies, improvements in vehicle anti-theft technology, and the introduction of better security systems.
Third, a steady decline period from 2006 to 2010 showed a gradual decrease to around 4,500 thefts. During 2011-2019, the trend shifted to show a moderate increase followed by fluctuating patterns, with thefts hovering between 5,000 and 8,000 annually. These small peaks and valleys suggest seasonal patterns in vehicle theft activity. Finally, the period from 2020 to 2024 exhibited notable fluctuations, particularly during the pandemic years, reflecting the unusual circumstances and changing urban dynamics of this period.


# Vehicle Thefts by District

![Vehicle Theft by District](/vehicle_theft_by_district.png)

*Figure 2: Theft distribution across San Francisco districts.*

Our second visualization presents a horizontal bar chart showing the distribution of vehicle thefts across San Francisco's police districts. The top three high-risk districts account for 47% of total thefts: Ingleside (20,546 thefts, 16.3%), Mission (17,297 thefts, 13.7%), and Bayview (16,780 thefts, 13.3%). These districts consistently showed high theft rates, particularly during the peak years of the early 2000s, when overall city thefts reached 18,103 annually.

# Mapping of total vehicle theft reports
<iframe src="plot1.html" width="800" height="600"></iframe>
The following choropleth map is a more visual and interactive presentation of the previous the bar plot. The map is colour-graded by total amount of reports of vehicle thefts, and allows the reader to examine the data in more detail by the zooming and hovering functions.

As you zoom out also allowing the sorrounding areas of San Francisco to be displayed, you see that the top 3 districts (Ingleside, Mission & Bayview) are located in the center/center-right side of San Francisco. Initially, one might think that this also translates to more civilized areas naturally leading to more vehicle thefts. However, as you examine the demographics of the different districts, neither Ingleside, Mission or Bayview seem to have significant larger populations than others. More interestingly, both Mission and Bayview are among the districts with the highest poverty rate (>10%) possibly placing these areas aming the ones with the highest crime rates [1]. This may very well be one of the main reasons for these being in the top 3 district with most vehicle thefts as higher poverty levels typically leads to more crime occurences in society. 

### References:
[1] Tsai, J. (2022). *One in three homes in this San Francisco neighborhood lives below the poverty line*. The San Francisco Standard. URL: *https://sfstandard.com/2022/12/08/san-francisco-neighborhood-new-census-data-maps/*

# Diving into 2005 to 2006 numbers
<iframe src="plot_of_2005.html" width="800" height="600"></iframe>
<iframe src="plot_of_2006.html" width="800" height="600"></iframe>
From the previous plot on total vehicle theft crimes per year, we saw a significant decline in crime reports from 2005 to 2006. This reduction is likely due to the implementation of enhanced security measures and more accurate tracking of vehicle theft incidents.

To rule out inaccurate tracking as a potential explanation, it’s useful to compare the proportions of vehicle thefts by district between 2005 and 2006. As the map above reveals, there is no significant change in the proportion of vehicle thefts by district despite the sharp decline in the total number of theft reports across all districts. This suggests that the large drop in vehicle thefts from 2005 to 2006 is unlikely to be attributed to flawed data collection.

Instead, a closer look at statewide police initiatives helps explain this decline. According to the *East Bay Times*, law enforcement institutions across California adopted new technologies in 2006 in order to reduce the amount of vehicle theft in the state. For instance, the introduction of bait cars, equipped with GPS tracking devices and cameras, helped officers track and arrest thieves more effectively. Additionally, increased vehicle security features, such as built-in alarms and key-coding systems, made newer models much harder to steal. These combined measures likely contributed to the reduction in thefts observed in 2006 [2].

### References

[2]: Sheppard, H. (2016). *Car thefts decrease statewide*. East Bay Times
URL: *https://www.eastbaytimes.com/2007/02/16/car-thefts-decrease-statewide/*


# Interactive Vehicle Theft Hotspots Map

<iframe 
    src="/assets/crime_viz.html" 
    width="900" 
    height="800"
    frameborder="0"
    scrolling="no"
></iframe>
