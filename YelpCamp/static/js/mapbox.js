console.log(mapboxToken);
mapboxgl.accessToken = mapboxToken;
const map = new mapboxgl.Map({
  container: "map", // container ID
  style: "mapbox://styles/mapbox/outdoors-v12", // style URL
  center: geometry.coordinates, // starting position [lng, lat]
  zoom: 9, // starting zoom
});
const popup = new mapboxgl.Popup({ offset: 25 }).setText("Construction on the Washington Monument began in 1848.");

new mapboxgl.Marker({ color: "red" })
  .setLngLat(geometry.coordinates)
  .setPopup(new mapboxgl.Popup({ offset: 30 }).setText(place))
  .addTo(map);
