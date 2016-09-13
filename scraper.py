from dc_base_scrapers.xml_scraper import Wfs2Scraper


stations_url = "http://inspire.misoportal.com/geoserver/london_borough_of_ealing_polling_station_location_point/ows?service=WFS&version=1.1.1&request=GetFeature&typeNames=london_borough_of_ealing_polling_station_location_point&srsName=EPSG%3A4326"
stations_fields = {
    '{http://www.dottedeyes.com/london_borough_of_ealing_polling_station_location_point}polling_station': 'polling_station',
    '{http://www.dottedeyes.com/london_borough_of_ealing_polling_station_location_point}pollingdistrict': 'pollingdistrict',
    '{http://www.dottedeyes.com/london_borough_of_ealing_polling_station_location_point}mi_ss': 'mi_ss',
    '{http://www.dottedeyes.com/london_borough_of_ealing_polling_station_location_point}fill': 'fill',
    '{http://www.dottedeyes.com/london_borough_of_ealing_polling_station_location_point}stroke': 'stroke',
    '{http://www.dottedeyes.com/london_borough_of_ealing_polling_station_location_point}size': 'size',
}

districts_url = "http://inspire.misoportal.com/geoserver/london_borough_of_ealing_polling_district_polygon/ows?service=WFS&version=1.1.1&request=GetFeature&typeNames=london_borough_of_ealing_polling_district_polygon&srsName=EPSG%3A4326"
districts_fields = {
    '{http://www.dottedeyes.com/london_borough_of_ealing_polling_district_polygon}distcode': 'distcode',
    '{http://www.dottedeyes.com/london_borough_of_ealing_polling_district_polygon}wardname': 'wardname',
    '{http://www.dottedeyes.com/london_borough_of_ealing_polling_district_polygon}mi_bp': 'mi_bp',
    '{http://www.dottedeyes.com/london_borough_of_ealing_polling_district_polygon}stroke': 'stroke',
    '{http://www.dottedeyes.com/london_borough_of_ealing_polling_district_polygon}strokewid': 'strokewid',
    '{http://www.dottedeyes.com/london_borough_of_ealing_polling_district_polygon}stroke2': 'stroke2',
}

council_id = 'E09000009'


stations_scraper = Wfs2Scraper(stations_url, council_id, 'stations', stations_fields, ['polling_station', 'pollingdistrict'])
stations_scraper.scrape()
districts_scraper = Wfs2Scraper(districts_url, council_id, 'districts', districts_fields, 'distcode')
districts_scraper.scrape()
