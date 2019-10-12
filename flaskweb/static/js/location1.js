var locations = [];
// The first step is obtain all the latitude and longitude from the HTML
// The below is a simple jQuery selector
$(".coordinates").each(function () {
    var longitude = $(".longitude", this).text().trim();
    // console.log(longitude)
    var latitude = $(".latitude", this).text().trim();
    var description = $(".description", this).text().trim();
    var service_name = $(".type",this).text().trim()
    var id_ = $(".id_",this).text().trim()
    // Create a point data structure to hold the values.
    var point = {
        "latitude": latitude,
        "longitude": longitude,
        "description": description,
        "service_name": service_name,
        "id_": id_
    };
    // Push them all into an array.
    locations.push(point);
});

console.log(locations)

var data = [];
for (i = 0; i < locations.length; i++) {
    var feature = {
        "type": "Feature",
        "properties": {
            "description": locations[i].description,
            "service_name": locations[i].service_name,
            "id_": locations[i].id_,
            "icon": "circle-15"
        },
        "geometry": {
            "type": "Point",
            "coordinates": [locations[i].longitude, locations[i].latitude]
        }
    };
    data.push(feature)
    console.log(feature)

}
// console.log(data)

mapboxgl.accessToken = 'pk.eyJ1IjoieHVlamluaHVhbmciLCJhIjoiY2psdDA1dDV5MDJzeTN2bGRxcGNodHY5YSJ9.Hx5ukpvIPwuE4kDn2JQW4Q';

var map1 = new mapboxgl.Map({
    container: 'map1',
    style: 'mapbox://styles/mapbox/streets-v10',
    zoom: 11,
    center: [locations[0].longitude, locations[0].latitude]
});


map1.on('load', function () {
    // Add a layer showing the places.
    map1.addLayer({
        "id": "places",
        "type": "symbol",
        "source": {
            "type": "geojson",
            "data": {
                "type": "FeatureCollection",
                "features": data
            }
        },
        "layout": {
            "icon-image": "{icon}",
            "icon-allow-overlap": true
        }
    });

    // map1.addControl(new MapboxGeocoder({
    //     accessToken: mapboxgl.accessToken,
    //     marker: false,
    // }));;

    map1.addControl(new mapboxgl.NavigationControl());
    map1.addControl(new mapboxgl.GeolocateControl({
        positionOptions: {
            enableHighAccuracy: true
        },
        trackUserLocation: true
    }));

    // When a click event occurs on a feature in the places layer, open a popup at the
    // location of the feature, with description HTML from its properties.
    map1.on('click', 'places', function (e) {
        var coordinates = e.features[0].geometry.coordinates.slice();
        var description = e.features[0].properties.description;
        var service_name = e.features[0].properties.service_name;
        var id_ = e.features[0].properties.id_;
        var url = '/detailedInfo/' + service_name + '/' + id_
        // Ensure that if the map is zoomed out such that multiple
        // copies of the feature are visible, the popup appears
        // over the copy being pointed to.
        while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
            coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
        }

        new mapboxgl.Popup()
            .setLngLat(coordinates)
            .setHTML('<a href="' + url + '">' + description + '</a>')
            // .setHTML("<a href={{ url_for('detailedInfo'" + ", service_id= " + id_ + ", service_name=" + service_name + ") }}>" + description + "</a>")
            .addTo(map1);
    });
    // Change the cursor to a pointer when the mouse is over the places layer.
    map1.on('mouseenter', 'places', function () {
        map1.getCanvas().style.cursor = 'pointer';
    });
    // Change it back to a pointer when it leaves.
    map1.on('mouseleave', 'places', function () {
        map1.getCanvas().style.cursor = '';
    });
});


// for the search map
