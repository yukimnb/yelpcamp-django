mapboxgl.accessToken = mapboxToken;
const map = new mapboxgl.Map({
  container: "map", // container ID
  style: "mapbox://styles/mapbox/outdoors-v12", // style URL
  center: geometry.coordinates, // starting position [lng, lat]
  zoom: 9, // starting zoom
});

new mapboxgl.Marker({ color: "red" })
  .setLngLat(geometry.coordinates)
  .setPopup(new mapboxgl.Popup({ offset: 30 }).setText(place))
  .addTo(map);
