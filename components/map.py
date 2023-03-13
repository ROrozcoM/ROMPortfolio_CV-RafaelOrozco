import geopandas as gpd
import pandas as pd
import dash_leaflet as dl
import dash_mantine_components as dmc



'''gdf2 = gpd.read_file('./assets/useyourshapefile.shp')
geojson2 = gdf2.__geo_interface__'''

map = dl.Map([dl.LayersControl([
    dl.BaseLayer(dl.TileLayer(), name='Base', checked=True),
    #dl.Overlay(dl.GeoJSON(data=geojson2, id='places', format='geojson', ), name="work_places", checked=True),
    ]),
    ],
    #center=gdf2.unary_union.centroid.coords[0][::-1],
        style={"width": "100%", "height": "800px", "position": "relative", 'margin': "auto", }, zoom=7,
        maxZoom=25,
        id='mapa_trabajos')




map_card = dmc.Card(
    children = [map],
    withBorder=True,
    shadow="sm",
    radius="md",
)

