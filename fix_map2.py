path = r"C:\Users\Hermes Botanica\Documents\bass-report\index.html"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

old = "  detailMarker.bindPopup('<strong>' + name + '</strong>', { closeButton: false }).openPopup();\n\n  // ── Bank access point markers ──"
new = "  detailMarker.bindPopup('<strong>' + name + '</strong>', { closeButton: false }).openPopup();\n\n  // Snap the pin to the precise water centroid via Nominatim (async, silently)\n  if (!_preciseCoords[name]) _snapMarkerToWater(lat, lon, name);\n\n  // ── Bank access point markers ──"

if old in content:
    content = content.replace(old, new, 1)
    print("REPLACED OK")
else:
    print("NOT FOUND")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("DONE")
