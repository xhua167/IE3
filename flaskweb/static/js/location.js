// google: AIzaSyB4Iq90i4001HHq0C2wfLoxwy_oVP6wQbk


var longitude = $("#longitude").text().trim();
var latitude = $("#latitude").text().trim();
var description = $("#description").text().trim();
// console.log(description);

mapboxgl.accessToken = 'pk.eyJ1IjoieHVlamluaHVhbmciLCJhIjoiY2psdDA1dDV5MDJzeTN2bGRxcGNodHY5YSJ9.Hx5ukpvIPwuE4kDn2JQW4Q';
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    zoom: 13,
    center: [longitude, latitude]
});

// create the popup
var popup = new mapboxgl.Popup({ offset: 25 })
.setText(description);

new mapboxgl.Marker()
.setLngLat([longitude, latitude])
.setPopup(popup) // sets a popup on this marker
.addTo(map);

var geocoder = new MapboxGeocoder({
    accessToken: mapboxgl.accessToken,
    marker: {
    color: 'orange'
    },
    mapboxgl: mapboxgl
});

map.addControl(geocoder);

map.on('load', function() {
  var directions = new MapboxDirections({
    accessToken: mapboxgl.accessToken
  });
  map.addControl(directions, 'top-left');
  // directions.setOrigin([longitude, latitude]);
  directions.setDestination([longitude, latitude]);
});



map.addControl(new mapboxgl.GeolocateControl({
    positionOptions: {
    enableHighAccuracy: true
    },
    trackUserLocation: true
}));

map.addControl(new mapboxgl.NavigationControl());










