import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import geopy.distance as gp_dist



bci_agents=pd.read_csv('<link of exprted excel sheet>')
bci_hubs=pd.read_csv('<link of exprted excel sheet>')


bci_agents.head()


active_agents=bci_agents[(bci_agents['Active Status']=='Active') & (bci_agents['GPS Location'].notna())]
active_agents.reset_index(inplace=True)


colors=['blue','green','red','orange']
tof=bci_hubs['Type of facility'].unique()
color_dict = dict(zip(tof,colors))


bs_m= folium.Map(location=[25.473034,81.878357], zoom_start=6)

for i in range(len(active_agents)):
    folium.CircleMarker(
    location=str(active_agents.loc[i]['GPS Location']).split(','),
    radius=5,
    tooltip=f"{active_agents.loc[i]['Name of Agent']}, {active_agents.loc[i]['City/Village/Block/Taluka']}<br>\
        Has {active_agents.loc[i]['Vehicle Type']}",
    color='green',
    fill=True,
    fill_color='#3186cc'
).add_to(bs_m)

for i, row in bci_hubs.iterrows():
    folium.Marker(
    location=row['GPS Location'].split(','),
    tooltip=f"{row['Hub Name']}<br>{row['Aid Type (comma separated)']}<br>\
        Inventory as of {row['Inventory updated as of']}: {row['Inventory']}<br>\
        Open: {row['Operating Hours']}",
    icon=folium.Icon(color=color_dict[row['Type of facility']], icon="medkit", prefix='fa')
).add_to(bs_m)
    
for i in range(len(bci_hubs)):
    folium.Circle(bci_hubs.loc[i]['GPS Location'].split(','),radius=int(bci_hubs.loc[i]['Hub Radius (km)']*1000)).add_to(bs_m)

# bs_m.save('bci.html')


sasha_hubs=pd.read_csv('<link of exprted excel sheet>')


sasha_hubs.head()


colors=['blue','green']
tof=sasha_hubs['Hub Type'].unique()
color_dict = dict(zip(tof,colors))
color_dict

for i, row in sasha_hubs[sasha_hubs['GPS Location'].notna()].iterrows():
    folium.Marker(
    location=row['GPS Location'].split(','),
    tooltip=f"{row['Hub name']}<br>{row['Contact Person']}<br>\
        {round(row['Artisans'])} artisans, {row['Products']}",
    icon=folium.Icon(color=color_dict[row['Hub Type']], icon="cart-plus", prefix='fa')
    ).add_to(bs_m)

for i in range(len(sasha_hubs)):
   folium.Circle(sasha_hubs.loc[i]['GPS Location'].split(','),radius=int(sasha_hubs.loc[i]['Radius (km)']*1000)).add_to(bs_m)

jaipur = pd.read_csv('Barefoot College - Casc-Aid (SAMNI) - Service agent (1).csv',error_bad_lines=False)
jaipur.head()
colors=['blue','green']
# tof=jaipur['Hub Type'].unique()
color_dict = dict(zip(tof,colors))

active_agents=jaipur[(jaipur['Active Status']=='Active') & (jaipur['GPS Location'].notna())]
active_agents.reset_index(inplace=True)

for i in range(len(active_agents)):
    folium.CircleMarker(
    location=str(active_agents.loc[i]['GPS Location']).split(','),
    radius=5,
    tooltip=f"{active_agents.loc[i]['Name of Agent']}, {active_agents.loc[i]['City/Village/Block/Taluka']}<br>\
        Has {active_agents.loc[i]['Vehicle Type']}",
    color='green',
    fill=True,
    fill_color='#3186cc'
).add_to(bs_m)

bs_m.save('bci_sasha.html')
