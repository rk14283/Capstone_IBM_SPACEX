#!/usr/bin/env python
# coding: utf-8

# <center>
#     <img src="https://gitlab.com/ibm/skills-network/courses/placeholder101/-/raw/master/labs/module%201/images/IDSNlogo.png" width="300" alt="cognitiveclass.ai logo"  />
# </center>
# 

# # **Launch Sites Locations Analysis with Folium**
# 

# Estimated time needed: **40** minutes
# 

# The launch success rate may depend on many factors such as payload mass, orbit type, and so on. It may also depend on the location and proximities of a launch site, i.e., the initial position of rocket trajectories. Finding an optimal location for building a launch site certainly involves many factors and hopefully we could discover some of the factors by analyzing the existing launch site locations.
# 

# In the previous exploratory data analysis labs, you have visualized the SpaceX launch dataset using `matplotlib` and `seaborn` and discovered some preliminary correlations between the launch site and success rates. In this lab, you will be performing more interactive visual analytics using `Folium`.
# 

# ## Objectives
# 

# This lab contains the following tasks:
# 
# *   **TASK 1:** Mark all launch sites on a map
# *   **TASK 2:** Mark the success/failed launches for each site on the map
# *   **TASK 3:** Calculate the distances between a launch site to its proximities
# 
# After completed the above tasks, you should be able to find some geographical patterns about launch sites.
# 

# Let's first import required Python packages for this lab:
# 

# In[1]:


get_ipython().system('pip3 install folium')
get_ipython().system('pip3 install wget')


# In[2]:


import folium
import wget
import pandas as pd


# In[3]:


# Import folium MarkerCluster plugin
from folium.plugins import MarkerCluster
# Import folium MousePosition plugin
from folium.plugins import MousePosition
# Import folium DivIcon plugin
from folium.features import DivIcon


# If you need to refresh your memory about folium, you may download and refer to this previous folium lab:
# 

# [Generating Maps with Python](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module\_3/DV0101EN-3-5-1-Generating-Maps-in-Python-py-v2.0.ipynb)
# 

# ## Task 1: Mark all launch sites on a map
# 

# First, let's try to add each site's location on a map using site's latitude and longitude coordinates
# 

# The following dataset with the name `spacex_launch_geo.csv` is an augmented dataset with latitude and longitude added for each site.
# 

# In[4]:


# Download and read the `spacex_launch_geo.csv`
spacex_csv_file = wget.download('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_geo.csv')
spacex_df=pd.read_csv(spacex_csv_file)


# Now, you can take a look at what are the coordinates for each site.
# 

# In[5]:


# Select relevant sub-columns: `Launch Site`, `Lat(Latitude)`, `Long(Longitude)`, `class`
spacex_df = spacex_df[['Launch Site', 'Lat', 'Long', 'class']]
launch_sites_df = spacex_df.groupby(['Launch Site'], as_index=False).first()
launch_sites_df = launch_sites_df[['Launch Site', 'Lat', 'Long']]
launch_sites_df


# Above coordinates are just plain numbers that can not give you any intuitive insights about where are those launch sites. If you are very good at geography, you can interpret those numbers directly in your mind. If not, that's fine too. Let's visualize those locations by pinning them on a map.
# 

# We first need to create a folium `Map` object, with an initial center location to be NASA Johnson Space Center at Houston, Texas.
# 

# In[6]:


# Start location is NASA Johnson Space Center
nasa_coordinate = [29.559684888503615, -95.0830971930759]
site_map = folium.Map(location=nasa_coordinate, zoom_start=10)


# We could use `folium.Circle` to add a highlighted circle area with a text label on a specific coordinate. For example,
# 

# In[7]:


# Create a blue circle at NASA Johnson Space Center's coordinate with a popup label showing its name
circle = folium.Circle(nasa_coordinate, radius=1000, color='#d35400', fill=True).add_child(folium.Popup('NASA Johnson Space Center'))
# Create a blue circle at NASA Johnson Space Center's coordinate with a icon showing its name
marker = folium.map.Marker(
    nasa_coordinate,
    # Create an icon as a text label
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % 'NASA JSC',
        )
    )
site_map.add_child(circle)
site_map.add_child(marker)


# and you should find a small yellow circle near the city of Houston and you can zoom-in to see a larger circle.
# 

# Now, let's add a circle for each launch site in data frame `launch_sites`
# 

# *TODO:*  Create and add `folium.Circle` and `folium.Marker` for each launch site on the site map
# 

# In[8]:


#doing this will be a lot easier with a loop or a function

CCAFS_LC40_latitude = 28.562302
CCAFS_LC40_longitude = -80.577356

CCAFS_LC40_coordinate = [28.562302, -80.577356]

CCAFS_SLC_40_latitutde = 28.563197
CCAFS_SLC_40_longitude =-80.576820
CCAFS_SLC_40_coordinate = [28.563197,-80.576820]

KSC_LC_39A_latitude = 28.573255
KSC_LC_39A_longitude =-80.646895
KSC_LC_39A_coordinate = [28.573255,-80.646895]


VAFB_SLC_4E_latitude = 34.632834
VAFB_SLC_4E_longitude = -120.610746
VAFB_SLC_coordinate = [34.632834,-120.610746]


#sample array=[CCAFS_LC40_coordinate,CCAFS_SLC_40_coordinate, KSC_LC_39A_coordinate,VAFB_SLC_coordinate] 


# In[9]:


circle = folium.Circle(VAFB_SLC_coordinate, radius=1000, color='#000000', fill=True).add_child(folium.Popup('NASA Johnson Space Center'))
circle_2 =folium.Circle(CCAFS_LC40_coordinate, radius=1000, color='#000000', fill=True).add_child(folium.Popup('NASA Johnson Space Center'))
circle_3 =folium.Circle(CCAFS_SLC_40_coordinate, radius=1000, color='#000000', fill=True).add_child(folium.Popup('NASA Johnson Space Center'))
circle_4 = folium.Circle(KSC_LC_39A_coordinate, radius=1000, color='#000000', fill=True).add_child(folium.Popup('NASA Johnson Space Center'))


marker = folium.map.Marker(
    VAFB_SLC_coordinate, #will not take multiple arguments 
    # Create an icon as a text label
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % 'VAFB_SLC',
        )
    )

# Initial the map
#site_map = folium.Map(location=nasa_coordinate, zoom_start=5)
# For each launch site, add a Circle object based on its coordinate (Lat, Long) values. In addition, add Launch site name as a popup label


marker_2 = folium.map.Marker(
    CCAFS_LC40_coordinate, #will not take multiple arguments 
    # Create an icon as a text label
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % 'CCAFS_LC40',
        )
    )


marker_3 = folium.map.Marker(
    CCAFS_SLC_40_coordinate, #will not take multiple arguments 
    # Create an icon as a text label
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % '  CCAFS_SLC_40',
        )
    )

marker_4 = folium.map.Marker(
    KSC_LC_39A_coordinate, #will not take multiple arguments 
    # Create an icon as a text label
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % 'KSC_LC_39A',
        )
    )
#so it looks like I need to repeat the code multiple times, a loop or a function will help 
site_map.add_child(circle)
site_map.add_child(circle_2)
site_map.add_child(marker)
site_map.add_child(marker_2)
site_map.add_child(circle_3)
site_map.add_child(marker_3)
site_map.add_child(circle_4)
site_map.add_child(marker_4)

#However, I solved the problem, maybe it is not a 100% correct but it looks similar to the output, and I would be happy if I can do it all my life


# An example of folium.Circle:
# 

# `folium.Circle(coordinate, radius=1000, color='#000000', fill=True).add_child(folium.Popup(...))`
# 

# An example of folium.Marker:
# 

# `folium.map.Marker(coordinate, icon=DivIcon(icon_size=(20,20),icon_anchor=(0,0), html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % 'label', ))`
# 

# In[9]:


# Initial the map
site_map = folium.Map(location=nasa_coordinate, zoom_start=5)
# For each launch site, add a Circle object based on its coordinate (Lat, Long) values. In addition, add Launch site name as a popup label


# The generated map with marked launch sites should look similar to the following:
# 

# <center>
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_3/images/launch_site_markers.png" />
# </center>
# 

# Now, you can explore the map by zoom-in/out the marked areas
# , and try to answer the following questions:
# 
# *   Are all launch sites in proximity to the Equator line?
# *   Are all launch sites in very close proximity to the coast?
# 
# Also please try to explain your findings.
# 

# # Task 2: Mark the success/failed launches for each site on the map
# 

# Next, let's try to enhance the map by adding the launch outcomes for each site, and see which sites have high success rates.
# Recall that data frame spacex_df has detailed launch records, and the `class` column indicates if this launch was successful or not
# 

# In[10]:


spacex_df.tail(10)


# Next, let's create markers for all launch records.
# If a launch was successful `(class=1)`, then we use a green marker and if a launch was failed, we use a red marker `(class=0)`
# 

# Note that a launch only happens in one of the four launch sites, which means many launch records will have the exact same coordinate. Marker clusters can be a good way to simplify a map containing many markers having the same coordinate.
# 

# Let's first create a `MarkerCluster` object
# 

# In[19]:


marker_cluster = MarkerCluster()


# *TODO:* Create a new column in `launch_sites` dataframe called `marker_color` to store the marker colors based on the `class` value
# 

# In[ ]:



# Apply a function to check the value of `class` column
# If class=1, marker_color value will be green
# If class=0, marker_color value will be red

#If class=1 color= greeen, else  red return class 


# In[11]:


# Function to assign color to launch outcome
def assign_marker_color(launch_outcome):
    if launch_outcome == 1:
        return 'green'
    else:
        return 'red'
    
spacex_df['marker_color'] = spacex_df['class'].apply(assign_marker_color)
spacex_df.tail(10)


# *TODO:* For each launch result in `spacex_df` data frame, add a `folium.Marker` to `marker_cluster`
# 

# In[13]:


CCAFS_LC40_coordinate = [28.562302, -80.577356]
CCAFS_SLC_40_coordinate = [28.563197,-80.576820]
KSC_LC_39A_coordinate = [28.573255,-80.646895]
VAFB_SLC_coordinate = [34.632834,-120.610746]


# In[14]:


# Add marker_cluster to current site_map
site_map.add_child(marker_cluster)

# for each row in spacex_df data frame
# create a Marker object with its coordinate
# and customize the Marker's icon property to indicate if this launch was successed or failed, 
# e.g., icon=folium.Icon(color='white', icon_color=row['marker_color']
for index, record in spacex_df.iterrows():
    # TODO: Create and add a Marker cluster to the site map
    marker = folium.Marker(CCAFS_LC40_coordinate)
    marker_cluster.add_child(marker)

for index, record in spacex_df.iterrows():
    marker = folium.Marker(KSC_LC_39A_coordinate )
    marker_cluster.add_child(marker)
 

for index, record in spacex_df.iterrows():
    marker = folium.Marker(CCAFS_SLC_40_coordinate)
    marker_cluster.add_child(marker)


for index, record in spacex_df.iterrows():
    marker = folium.Marker(VAFB_SLC_coordinate)
    marker_cluster.add_child(marker)


df_launches = spacex_df[['Lat', 'Long']]
launches_list = df_launches.values.tolist() 
launches_list_size = len(launches_list)
for point in range(0,launches_list_size):
    folium.Marker(launches_list[point]).add_to(site_map)
site_map

#now labeling red and green ones 


# In[20]:


#actual code that runs 
latitudes = list(spacex_df.Lat)
longitudes = list(spacex_df.Long)
labels = list(spacex_df.marker_color)

site_map.add_child(marker_cluster)
from folium import plugins

# Mark cluster object for the incidents in the dataframe
map_locations = plugins.MarkerCluster().add_to(site_map)

for lat, lng, label, in zip(spacex_df.Lat, spacex_df.Long, spacex_df.marker_color):
    folium.Marker(
        location=[lat, lng],
        icon=None,
        popup=label,
    ).add_to(map_locations)
    
site_map.add_child(map_locations)

# display map
site_map


# Your updated map may look like the following screenshots:
# 

# <center>
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_3/images/launch_site_marker_cluster.png" />
# </center>
# 

# <center>
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_3/images/launch_site_marker_cluster_zoomed.png" />
# </center>
# 

# In[24]:


df_launches = spacex_df[['Lat', 'Long', 'class']]


# In[18]:


launches_list = df_launches.values.tolist() 
launches_list_size = len(launches_list)


# In[19]:


launches_list


# In[23]:


for index, record in spacex_df.iterrows():
    # TODO: Create and add a Marker cluster to the site map
    # marker = folium.Marker(...)
    marker = folium.Marker([record['Lat'], record['Long']], 
                  icon=folium.Icon(color='white', icon_color=record['marker_color']))
    marker_cluster.add_child(marker)

site_map


# From the color-labeled markers in marker clusters, you should be able to easily identify which launch sites have relatively high success rates.
# 

# # TASK 3: Calculate the distances between a launch site to its proximities
# 

# Next, we need to explore and analyze the proximities of launch sites.
# 

# Let's first add a `MousePosition` on the map to get coordinate for a mouse over a point on the map. As such, while you are exploring the map, you can easily find the coordinates of any points of interests (such as railway)
# 

# In[50]:


# Add Mouse Position to get the coordinate (Lat, Long) for a mouse over on the map
formatter = "function(num) {return L.Util.formatNum(num, 5);};"
mouse_position = MousePosition(
    position='topright',
    separator=' Long: ',
    empty_string='NaN',
    lng_first=False,
    num_digits=20,
    prefix='Lat:',
    lat_formatter=formatter,
    lng_formatter=formatter,
)
site_map.add_child(mouse_position)
site_map


# Now zoom in to a launch site and explore its proximity to see if you can easily find any railway, highway, coastline, etc. Move your mouse to these points and mark down their coordinates (shown on the top-left) in order to the distance to the launch site.
# 

# You can calculate the distance between two points on the map based on their `Lat` and `Long` values using the following method:
# 

# In[44]:


from math import sin, cos, sqrt, atan2, radians

def calculate_distance(lat1, lon1, lat2, lon2):
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


# In[45]:


distance_coastline = calculate_distance(28.59281,28.59281, 28.58423, -80.51519)
distance_coastline


# *TODO:* Mark down a point on the closest coastline using MousePosition and calculate the distance between the coastline point and the launch site.
# 

# In[46]:


# find coordinate of the closet coastline
# e.g.,: Lat: 28.56367  Lon: -80.57163

distance_coastline
marker_railway = folium.map.Marker(
    [28.59281, -80.59076],
    # Create an icon as a text label
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % "{:10.2f} KM".format(distance_coastline)
    )
)

site_map.add_child(mouse_position)
site_map


# *TODO:* After obtained its coordinate, create a `folium.Marker` to show the distance
# 

# In[47]:


# Create and add a folium.Marker on your selected closest coastline point on the map
# Display the distance between coastline point and launch site using the icon property 
# for example
coordinate = [28.59281, -80.59076]
distance_coastline = folium.Marker(
    coordinate,
    icon=folium.DivIcon(
       icon_size=(20,20),
       icon_anchor=(0,0),
        html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % "{:10.2f} KM".format(distance_coastline),
       )
 )

site_map.add_child(distance_coastline)
site_map
#icon=folium.DivIcon


# *TODO:* Draw a `PolyLine` between a launch site to the selected coastline point
# 

# In[53]:


# Create a `folium.PolyLine` object using the coastline coordinates and launch site coordinate
# lines=folium.PolyLine(locations=coordinates, weight=1)
coordinates = [
    [28.56342, -80.57674],
    [28.56342, -80.56756]]

lines=folium.PolyLine(locations=coordinates, weight=1)
site_map.add_child(lines)
distance = calculate_distance(coordinates[0][0], coordinates[0][1], coordinates[1][0], coordinates[1][1])
lines=folium.PolyLine(locations=coordinates, weight=1)
site_map.add_child(lines)
#need to add circle to the above code 


# Your updated map with distance line should look like the following screenshot:
# 

# <center>
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_3/images/launch_site_marker_distance.png" />
# </center>
# 

# *TODO:* Similarly, you can draw a line betwee a launch site to its closest city, railway, highway, etc. You need to use `MousePosition` to find the their coordinates on the map first
# 

# A railway map symbol may look like this:
# 

# <center>
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_3/images/railway.png" />
# </center>
# 

# A highway map symbol may look like this:
# 

# <center>
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_3/images/highway.png" />
# </center>
# 

# A city map symbol may look like this:
# 

# <center>
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_3/images/city.png" />
# </center>
# 

# In[ ]:


# Create a marker with distance to a closest city, railway, highway, etc.
# Draw a line between the marker to the launch site


# In[54]:


coordinates = [
    [28.56342, -80.57674],
    [28.5383, -81.3792]]

lines=folium.PolyLine(locations=coordinates, weight=1)
site_map.add_child(lines)
distance = calculate_distance(coordinates[0][0], coordinates[0][1], coordinates[1][0], coordinates[1][1])
distance_circle = folium.Marker(
    [28.5383, -81.3792],
    icon=DivIcon(
        icon_size=(20,20),
        icon_anchor=(0,0),
        html='<div style="font-size: 12; color:#252526;"><b>%s</b></div>' % "{:10.2f} KM".format(distance),
        )
    )
site_map.add_child(distance_circle)
site_map


# In[ ]:





# After you plot distance lines to the proximities, you can answer the following questions easily:
# 
# *   Are launch sites in close proximity to railways?
# *   Are launch sites in close proximity to highways?
# *   Are launch sites in close proximity to coastline?
# *   Do launch sites keep certain distance away from cities?
# 
# Also please try to explain your findings.
# 

# # Next Steps:
# 
# Now you have discovered many interesting insights related to the launch sites' location using folium, in a very interactive way. Next, you will need to build a dashboard using Ploty Dash on detailed launch records.
# 

# ## Authors
# 

# [Yan Luo](https://www.linkedin.com/in/yan-luo-96288783/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2021-01-01)
# 

# ### Other Contributors
# 

# Joseph Santarcangelo
# 

# ## Change Log
# 

# | Date (YYYY-MM-DD) | Version | Changed By | Change Description          |
# | ----------------- | ------- | ---------- | --------------------------- |
# | 2021-05-26        | 1.0     | Yan        | Created the initial version |
# 

# Copyright © 2021 IBM Corporation. All rights reserved.
# 
