path = r"C:\Users\Hermes Botanica\Documents\bass-report\index.html"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

old_sig = 'function initDetailMap(lat, lon, name, hex, score, bankAccess) {'

inject_before = '''// Cache of Nominatim-resolved precise centroids
var _preciseCoords = {};

function _snapMarkerToWater(lat, lon, name) {
  var delta = 0.5;
  var bb = (lat-delta)+","+(lon-delta)+","+(lat+delta)+","+(lon+delta);
  var url = "https://nominatim.openstreetmap.org/search?q=" +
    encodeURIComponent(name) +
    "&format=json&limit=5&countrycodes=us&bounded=1&viewbox=" + bb;
  fetch(url, { headers: { "Accept-Language": "en" } })
    .then(function(r){ return r.json(); })
    .then(function(results) {
      var waterClasses = ["natural","waterway","water","leisure"];
      var best = null;
      for (var i = 0; i < results.length; i++) {
        var r = results[i];
        var cls = (r["class"] || "").toLowerCase();
        if (waterClasses.indexOf(cls) >= 0) { best = r; break; }
      }
      if (!best && results.length) best = results[0];
      if (best) {
        var pLat = parseFloat(best.lat);
        var pLon = parseFloat(best.lon);
        var dLat = pLat - lat, dLon = pLon - lon;
        if (Math.sqrt(dLat*dLat + dLon*dLon) < 0.3) {
          _preciseCoords[name] = { lat: pLat, lon: pLon };
          if (detailMarker) detailMarker.setLatLng([pLat, pLon]);
          if (detailPulse)  detailPulse.setLatLng([pLat, pLon]);
          detailMap.panTo([pLat, pLon], { animate: true, duration: 0.5 });
        }
      }
    })
    .catch(function(){});
}

'''

new_fn_open = '''function initDetailMap(lat, lon, name, hex, score, bankAccess) {
  // Use cached precise coords if available from a previous lookup
  if (_preciseCoords[name]) {
    lat = _preciseCoords[name].lat;
    lon = _preciseCoords[name].lon;
  }
'''

if old_sig in content:
    content = content.replace(old_sig, inject_before + new_fn_open, 1)
    print("REPLACED OK")
else:
    print("NOT FOUND — checking...")
    idx = content.find('initDetailMap')
    print(repr(content[idx:idx+120]))

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("DONE")
