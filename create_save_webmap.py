from arcgis.gis import GIS
import config

print("Create GIS Object")
gis = GIS("https://www.arcgis.com", config.username, config.password)

# Create map object
print("Create Map Object")
nl_map = gis.map('Netherlands', zoomlevel=7)  # you can specify the zoom level when creating a map

# Look for content created by esri_nl_content
print("Search for feature layers")
flayer_search_result = gis.content.search("hectometer owner:Esri_NL_Content","Feature Layer", outside_org=True)

# Adding the feature layers to the map object
print("Adding feature layers to the map")
for featureLayer in flayer_search_result:
    nl_map.add_layer(featureLayer)

# Set item properties
item_properties={'title':'Webmap DevDay 2018 via [application]',
                 'snippet': 'Python generated webmap saved as ArcGIS items',
                 'tags':['webmap', 'python generated', 'devday']}

# Save the map object as an ArcGIS item
print("Save the map")
nl_map.save(item_properties, folder="DevDay 2018")

print("Python Script completed")

