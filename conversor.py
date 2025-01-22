import geopandas as gpd

geojson_path = "pontos_rede.geojson"
data = gpd.read_file(geojson_path)

print("Sistema original:", data.crs)

# Transformar para WGS 84 (EPSG:4326)
data_wgs84 = data.to_crs(epsg=4326)

print(data_wgs84.head())

data_wgs84.to_file("pontos_rede_wgs84.geojson", driver="GeoJSON")
