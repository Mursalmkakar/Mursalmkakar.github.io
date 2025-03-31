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
The visualization highlights several key findings: First, an unprecedented peak of 18,103 thefts occurred in the early 2000s. This period coincides with the pre-smartphone era when vehicle security systems were less sophisticated. Second, a sharp decline occurred from 2005 to 2006, with theft numbers dropping dramatically from approximately 18,000 to 7,000. This significant reduction might be attributed to the implementation of new police strategies, improvements in vehicle anti-theft technology, and the introduction of better security systems [1]. Third, a steady decline period from 2006 to 2010 showed a gradual decrease to around 4,500 thefts. During 2011-2019, the trend shifted to show a moderate increase followed by fluctuating patterns, with thefts hovering between 5,000 and 8,000 annually. These small peaks and valleys suggest seasonal patterns in vehicle theft activity. Finally, the period from 2020 to 2024 exhibited notable fluctuations, particularly during the pandemic years, reflecting the unusual circumstances and changing urban dynamics of this period.


# Vehicle Thefts by District

![Vehicle Theft by District](/vehicle_theft_by_district.png)

*Figure 2: Theft distribution across San Francisco districts.*

When breaking down vehicle thefts by police district, distinct spatial patterns begin to emerge. Ingleside leads with over 20.000 reported thefts, followed closely by Mission and Bayview, together accounting for nearly half of all vehicle thefts citywide. These districts consistently experienced high theft volumes throughout the two decades, especially during peak years in the early 2000s. In contrast, districts such as Park, Tenderloin, and Richmond reported significantly fewer incidents, suggesting either more effective local deterrents, differences in vehicle density, or varying levels of police reporting and enforcement. 

# Top District Analysis 
<iframe src="plot_of_2005.html" width="800" height="600"></iframe>
<iframe src="plot_of_2006.html" width="800" height="600"></iframe>
From previous plots on total vehicle theft crimes per year, we saw a significant decline in crime reports from 2005 to 2006. The following comparison between vehicle theft reports in 2005 and 2006 highlights possible reasons for this decline aswell as argues for why Ingleside, mission & bayview are the districts with the most vehicle theft crimes. Thus the following sections builds on previous analysis to address aspects of the data that likely raise questions for the reader.

To better understand the factors influencing vehicle theft rates, it's important to first examine the demographics and socio-economic conditions of the city's districts. Looking into the demographics of the different districts, neither Ingleside, Mission or Bayview seem to have significant larger populations than others. More interestingly, both Mission and Bayview are among the districts with the highest poverty rate (>10%) possibly placing these areas aming the ones with the highest crime rates [2]. This may very well be one of the main reasons for these being in the top districts with most vehicle thefts as higher poverty levels typically leads to more crime occurences in society.

# 2005-2006 Comparison
At first glimps, the rapid decline from 2005 to 2006 may likely raise a few questions to how crime reports more than halved in just 1 year. To rule out inaccurate tracking as a potential explanation, it’s useful to compare the proportions of vehicle thefts by district between 2005 and 2006. As the map above reveals, there is no significant change in the proportion of vehicle thefts by district despite the sharp decline in the total number of theft reports across all districts. This suggests that the large drop in vehicle thefts from 2005 to 2006 is unlikely to be attributed to flawed data collection.

Instead, a closer look at statewide police initiatives helps explain this decline. According to the *East Bay Times*, law enforcement institutions across California adopted new technologies in 2006 in order to reduce the amount of vehicle theft in the state. For instance, the introduction of bait cars, equipped with GPS tracking devices and cameras, helped officers track and arrest thieves more effectively. Additionally, increased vehicle security features, such as built-in alarms and key-coding systems, made newer models much harder to steal. These combined measures likely contributed to the reduction in thefts observed in 2006 [2].

# Interactive Bokeh Plot for Vehicle Theft Hotspots

We have looked into the vehicle thefts on a macro level divided into districts, why not jump into the specifics? Below is an interactive plot made in bokeh, using the OpenStreetMap tool and we can find red circles on the map indicating where a vehicle theft has occured in a given year. Some areas experienced vehicle theft multiple times and it has been captured in this map, where larger circles along with more opaque red colors indicate higher concentrations of vehicle theft. Hovering over each red circle will show the year, number of crimes as well as which district it belongs to.

Dive into this interactive plot below to find hotspots by hovering over the red markers! 

<iframe 
    src="/assets/crime_viz.html" 
    width="900" 
    height="820"
    frameborder="0"
    scrolling="no"
></iframe>

### Notable Recent Developments in 430A in Bayview
 
By going through the dropdown, there is a large concentration of vehicle thefts at 430A just east of Portola in the Bayview district. This area experienced this large concentration in the 2000s, later on dying out in the 2010s, but recently since the pandemic, this area is seeing a meteoric rise in vehicle thefts. Concentrated in areas like Portola, the Mission and the Bayview, we have "freeways crisscross blocks of industrial buildings with parking lots" leave them vulnerable to thieves. Further comments by a Bayview station police officer mentions Bayview's "large, secluded industrial zones" make it vulnerable compared to denser neighborhoods with cameras [3].

### Other developments 
 
Other concentrations have also been formed between Mission district as well as the South of Market. Reasons as to why there are instances of vehicle theft concentrations are attributed to similiar reasons to the Bayview area. The mission area contains "warehouses, business high-rises and a quick route to the open road" and as such, both South of Market as well as Mission are highly ranked in the neighborhoods vulnerable to vehicle theft [4]. How these trends will continue to evolve is yet to be seen as 2025 isn't completed yet, but historical trends are accessible through a dropdown and a hover of your computer mouse!

### References

[1] Sheppard, H. (2016). *Car thefts decrease statewide*. East Bay Times. [URL](https://www.eastbaytimes.com/2007/02/16/car-thefts-decrease-statewide/)

[2] Tsai, J. (2022). *One in three homes in this San Francisco neighborhood lives below the poverty line*. The San Francisco Standard. [URL](https://sfstandard.com/2022/12/08/san-francisco-neighborhood-new-census-data-maps/)

[3] Swan, Rachel, and Adriana Rezal. "These Neighborhoods Are San Francisco's Car-Theft Hot Spots." San Francisco Chronicle, San Francisco Chronicle, 28 Sept. 2023, [URL](https://www.sfchronicle.com/crime/article/car-theft-san-francisco-18387300.php)

[4] Kaplan, Ben. "2023 WE San Francisco Auto Theft Report." WE San Francisco, 1 Jan. 2024, www.wesanfrancisco.org/data/2023-car-theft. [URL](https://www.wesanfrancisco.org/data/2023-car-theft)