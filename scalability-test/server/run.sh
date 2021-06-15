#!/bin/bash

# Download relevant OSM data
echo Downloading OSM data...
wget -qO source.osm.pbf ${OSM_DATA}
# Filter OSM road network
echo Filtering OSM road network...
osmium tags-filter source.osm.pbf w/highway w/public_transport=platform w/railway=platform w/park_ride=yes r/type=restriction r/type=route -o filtered.osm.pbf -f pbf,add_metadata=false
# Delete raw OSM file
rm source.osm.pbf
# Download GTFS data source
echo Downloading GTFS data source...
wget -qO source.gtfs.zip ${GTFS_DATA}
# Start OTP
java -Xmx8G -jar otp-2.1.0-SNAPSHOT-shaded.jar --build --serve .