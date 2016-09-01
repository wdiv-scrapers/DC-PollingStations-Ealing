from geojson_scraper import scrape


stations_url = "http://inspire.misoportal.com/geoserver/london_borough_of_ealing_polling_station_location_point/ows?service=WFS&version=1.1.1&request=GetFeature&typeNames=london_borough_of_ealing_polling_station_location_point&outputFormat=json&srsName=EPSG%3A4326"
districts_url = "http://inspire.misoportal.com/geoserver/london_borough_of_ealing_polling_district_polygon/ows?service=WFS&version=1.1.1&request=GetFeature&typeNames=london_borough_of_ealing_polling_district_polygon&outputFormat=json&srsName=EPSG%3A4326"
council_id = 'E09000009'


scrape(stations_url, council_id, 'utf-8', 'stations')
scrape(districts_url, council_id, 'utf-8', 'districts')
