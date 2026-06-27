path = r"C:\Users\Hermes Botanica\Documents\bass-report\index.html"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Corrected centroids from USGS/Wikipedia/known data (lat, lon)
# Format: old string -> new string (just the lat/lon part)
fixes = [
    # White Rock Lake — centroid is roughly correct but let's be precise
    ('{ name:"White Rock Lake",         lat:32.83,  lon:-96.71,', '{ name:"White Rock Lake",         lat:32.8371, lon:-96.7168,'),
    ('{ name:"Lake Ray Roberts",        lat:33.37,  lon:-97.05,', '{ name:"Lake Ray Roberts",        lat:33.3920, lon:-97.0268,'),
    ('{ name:"Benbrook Lake",           lat:32.64,  lon:-97.47,', '{ name:"Benbrook Lake",           lat:32.6281, lon:-97.4638,'),
    ('{ name:"Lake Grapevine",          lat:32.97,  lon:-97.07,', '{ name:"Lake Grapevine",          lat:32.9898, lon:-97.0696,'),
    ('{ name:"Joe Pool Lake",           lat:32.66,  lon:-97.02,', '{ name:"Joe Pool Lake",           lat:32.6267, lon:-97.0197,'),
    ('{ name:"Lake Lewisville",         lat:33.04,  lon:-96.87,', '{ name:"Lake Lewisville",         lat:33.0912, lon:-96.9602,'),
    ('{ name:"Lake Texoma",             lat:33.80,  lon:-96.60,', '{ name:"Lake Texoma",             lat:33.8283, lon:-96.6128,'),
    ('{ name:"Lake Fork",               lat:32.89,  lon:-95.57,', '{ name:"Lake Fork",               lat:32.8936, lon:-95.6109,'),
    ('{ name:"Sam Rayburn Reservoir",   lat:31.07,  lon:-94.11,', '{ name:"Sam Rayburn Reservoir",   lat:31.0744, lon:-94.1095,'),
    ('{ name:"Toledo Bend Reservoir",   lat:31.18,  lon:-93.57,', '{ name:"Toledo Bend Reservoir",   lat:31.2120, lon:-93.5678,'),
    ('{ name:"Caddo Lake",              lat:32.69,  lon:-94.18,', '{ name:"Caddo Lake",              lat:32.6985, lon:-94.1782,'),
    ('{ name:"Lake Tawakoni",           lat:32.85,  lon:-95.95,', '{ name:"Lake Tawakoni",           lat:32.8581, lon:-95.9208,'),
    ('{ name:"Lake Palestine",          lat:31.93,  lon:-95.62,', '{ name:"Lake Palestine",          lat:31.9483, lon:-95.6342,'),
    ('{ name:"Lake Conroe",             lat:30.33,  lon:-95.42,', '{ name:"Lake Conroe",             lat:30.3800, lon:-95.5600,'),
    ('{ name:"Lake Houston",            lat:29.91,  lon:-95.17,', '{ name:"Lake Houston",            lat:29.9842, lon:-95.1438,'),
    ('{ name:"Lake Livingston",         lat:30.62,  lon:-94.94,', '{ name:"Lake Livingston",         lat:30.6500, lon:-94.9200,'),
    ('{ name:"Lake Travis",             lat:30.38,  lon:-98.00,', '{ name:"Lake Travis",             lat:30.4016, lon:-97.9247,'),
    ('{ name:"Lady Bird Lake",          lat:30.25,  lon:-97.81,', '{ name:"Lady Bird Lake",          lat:30.2588, lon:-97.7355,'),
    ('{ name:"Lake Georgetown",         lat:30.67,  lon:-97.77,', '{ name:"Lake Georgetown",         lat:30.6654, lon:-97.7935,'),
    ('{ name:"Canyon Lake",             lat:29.88,  lon:-98.20,', '{ name:"Canyon Lake",             lat:29.8820, lon:-98.2004,'),
    ('{ name:"Stillhouse Hollow Lake",  lat:30.98,  lon:-97.52,', '{ name:"Stillhouse Hollow Lake",  lat:30.9825, lon:-97.5193,'),
    ('{ name:"Belton Lake",             lat:31.12,  lon:-97.52,', '{ name:"Belton Lake",             lat:31.1447, lon:-97.5007,'),
    ('{ name:"Choke Canyon Reservoir",  lat:28.47,  lon:-98.25,', '{ name:"Choke Canyon Reservoir",  lat:28.4755, lon:-98.3369,'),
    ('{ name:"Falcon Reservoir",        lat:26.57,  lon:-99.15,', '{ name:"Falcon Reservoir",        lat:26.5617, lon:-99.1298,'),
    ('{ name:"Amistad Reservoir",       lat:29.45,  lon:-101.07,', '{ name:"Amistad Reservoir",       lat:29.5156, lon:-101.0701,'),
    ('{ name:"Lake Granbury",           lat:32.41,  lon:-97.77,', '{ name:"Lake Granbury",           lat:32.4053, lon:-97.7917,'),
    ('{ name:"Possum Kingdom Lake",     lat:32.87,  lon:-98.52,', '{ name:"Possum Kingdom Lake",     lat:32.8706, lon:-98.5019,'),
    ('{ name:"Lake Whitney",            lat:31.86,  lon:-97.36,', '{ name:"Lake Whitney",            lat:31.8582, lon:-97.3731,'),
    ('{ name:"Waco Lake",               lat:31.61,  lon:-97.26,', '{ name:"Waco Lake",               lat:31.6147, lon:-97.2568,'),
    ('{ name:"O.H. Ivie Reservoir",     lat:31.47,  lon:-100.22,', '{ name:"O.H. Ivie Reservoir",     lat:31.5128, lon:-99.9883,'),
    ('{ name:"Lake Meredith",           lat:35.43,  lon:-101.72,', '{ name:"Lake Meredith",           lat:35.6086, lon:-101.6948,'),
    ('{ name:"Lavon Lake",              lat:33.02,  lon:-96.42,', '{ name:"Lavon Lake",              lat:33.0345, lon:-96.4782,'),
    ('{ name:"Lake Ray Hubbard",        lat:32.84,  lon:-96.54,', '{ name:"Lake Ray Hubbard",        lat:32.8553, lon:-96.5380,'),
    ('{ name:"Lake Arlington",          lat:32.69,  lon:-97.23,', '{ name:"Lake Arlington",          lat:32.6937, lon:-97.2186,'),
    ('{ name:"Eagle Mountain Lake",     lat:32.92,  lon:-97.46,', '{ name:"Eagle Mountain Lake",     lat:32.9190, lon:-97.4584,'),
    ('{ name:"Lake Worth",              lat:32.83,  lon:-97.44,', '{ name:"Lake Worth",              lat:32.8265, lon:-97.4405,'),
    ('{ name:"Lake Brownwood",          lat:31.87,  lon:-99.01,', '{ name:"Lake Brownwood",          lat:31.8765, lon:-99.0074,'),
    ('{ name:"Lake Nasworthy",          lat:31.41,  lon:-100.50,', '{ name:"Lake Nasworthy",          lat:31.4046, lon:-100.4889,'),
    ('{ name:"Lake Corpus Christi",     lat:27.89,  lon:-97.87,', '{ name:"Lake Corpus Christi",     lat:27.8910, lon:-97.8704,'),
    ('{ name:"Calaveras Lake",          lat:29.33,  lon:-98.26,', '{ name:"Calaveras Lake",          lat:29.3416, lon:-98.2591,'),
    ('{ name:"Braunig Lake",            lat:29.27,  lon:-98.30,', '{ name:"Braunig Lake",            lat:29.2736, lon:-98.3046,'),
    ('{ name:"Lake Bastrop",            lat:30.116, lon:-97.267,', '{ name:"Lake Bastrop",            lat:30.1160, lon:-97.2840,'),
]

replaced = 0
for old, new in fixes:
    if old in content:
        content = content.replace(old, new, 1)
        replaced += 1
    else:
        print(f"NOT FOUND: {old[:60]}")

print(f"Replaced {replaced}/{len(fixes)} coordinate entries")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("DONE")
