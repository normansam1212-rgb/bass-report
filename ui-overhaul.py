
import re

path = 'C:/Users/Jacob/Documents/bass-report/index.html'
with open(path, 'r') as f:
    c = f.read()

# Find and replace the entire <style> block
style_start = c.index('<style>') + len('<style>')
style_end = c.index('</style>', style_start)
old_style = c[style_start:style_end]

new_style = r""":root {
  --bg:       #1B2A3A;
  --bg2:      #172230;
  --card:     #243447;
  --card2:    #2A3D52;
  --card-hi:  #314A63;
  --border:   rgba(158,139,122,0.15);
  --border-hi:rgba(158,139,122,0.30);
  --accent:   #E8DDD0;
  --adim:     rgba(232,221,208,0.08);
  --text:     #E8DDD0;
  --mid:      #9E8B7A;
  --dim:      rgba(158,139,122,0.55);
  --good:     #C8B99A;
  --ok:       #9E8B7A;
  --bad:      #A07878;
  --hot:      #E8A87C;
  --radius:   16px;
  --tabh:     68px;
  --st:       env(safe-area-inset-top, 24px);
  --sb:       env(safe-area-inset-bottom, 24px);
  --shadow:   0 2px 12px rgba(0,0,0,0.20), 0 1px 3px rgba(0,0,0,0.10);
  --shadow-lg:0 8px 32px rgba(0,0,0,0.30);
}

* { margin:0; padding:0; box-sizing:border-box; -webkit-tap-highlight-color:transparent; }

body {
  font-family:-apple-system,'SF Pro Display','Helvetica Neue','Segoe UI',sans-serif;
  background:var(--bg);
  background-image:
    radial-gradient(ellipse 80% 50% at 50% 0%, rgba(232,221,208,0.03) 0%, transparent 100%),
    radial-gradient(ellipse 60% 40% at 80% 100%, rgba(74,107,133,0.10) 0%, transparent 100%);
  color:var(--text);
  min-height:100dvh;
  padding-top:calc(var(--st) + 4px);
  padding-bottom:calc(var(--tabh) + var(--sb) + 12px);
  overscroll-behavior:none;
  -webkit-font-smoothing:antialiased;
}

/* ═══ Header ═══ */
header {
  padding:12px 18px 14px;
  display:flex; align-items:center; gap:12px;
  background:rgba(23,34,48,0.80);
  backdrop-filter:blur(32px); -webkit-backdrop-filter:blur(32px);
  border-bottom:1px solid var(--border);
  position:sticky; top:0; z-index:300;
}
.hdr-title {
  font-size:21px; font-weight:800; letter-spacing:-.6px; flex:1;
  display:flex; align-items:center; gap:0;
}
.hdr-title span { color:var(--accent); }
.hdr-sub {
  font-size:10px; color:var(--dim); margin-top:2px;
  letter-spacing:.2px;
}
.geo-btn {
  width:40px; height:40px; border-radius:14px;
  border:1px solid var(--border-hi);
  background:rgba(49,74,99,0.6);
  color:var(--accent); font-size:17px; cursor:pointer; flex-shrink:0;
  display:flex; align-items:center; justify-content:center;
  transition:all .15s ease;
}
.geo-btn:active { opacity:.7; transform:scale(.93); }

/* ═══ Search ═══ */
.search-wrap { padding:12px 18px 2px; position:relative; }
.search-inner {
  display:flex; align-items:center; gap:10px;
  background:rgba(36,52,71,0.7);
  border:1px solid var(--border);
  border-radius:15px;
  padding:0 16px; height:48px;
  transition:all .2s ease;
}
.search-inner:focus-within {
  border-color:var(--border-hi);
  background:rgba(36,52,71,0.95);
  box-shadow:0 0 0 3px rgba(158,139,122,0.08), var(--shadow);
}
.search-icon { color:var(--dim); flex-shrink:0; font-size:16px; }
.search-inner input {
  flex:1; background:none; border:none; outline:none;
  color:var(--text); font-size:15px; font-weight:500;
}
.search-inner input::placeholder { color:var(--dim); }
.search-clear {
  background:rgba(158,139,122,0.12); border:none; color:var(--mid);
  font-size:15px; cursor:pointer; padding:4px 6px; border-radius:8px;
  line-height:1; display:none;
}
.search-clear.visible { display:block; }

/* Search dropdown */
.search-dropdown {
  position:absolute; top:calc(100% + 6px); left:16px; right:16px;
  background:var(--card); border:1px solid var(--border);
  border-radius:var(--radius); overflow:hidden; z-index:500;
  box-shadow:var(--shadow-lg); display:none;
}
.search-dropdown.open { display:block; }
.search-result {
  padding:14px 16px; cursor:pointer;
  border-bottom:1px solid var(--border);
  transition:background .15s;
}
.search-result:last-child { border-bottom:none; }
.search-result:active { background:var(--card2); }
.sr-name { font-size:14px; font-weight:600; }
.sr-sub  { font-size:11px; color:var(--dim); margin-top:3px; }
.search-loading, .search-none {
  padding:16px; text-align:center; color:var(--dim); font-size:13px;
}

/* ═══ Location pill ═══ */
.loc-pill {
  margin:8px 18px 0;
  display:none; align-items:center; gap:6px;
  background:rgba(232,221,208,0.05);
  border:1px solid var(--border);
  border-radius:22px; padding:6px 14px;
  font-size:12px; font-weight:600;
  color:var(--mid);
}
.loc-pill.visible { display:flex; }
.loc-dist { color:var(--dim); font-size:11px; margin-left:auto; }

/* ═══ Conditions Grid ═══ */
.cond-grid {
  margin:12px 18px 0;
  display:grid; grid-template-columns:repeat(4,1fr); gap:8px;
}
.cond-cell {
  background:rgba(36,52,71,0.6);
  border:1px solid var(--border);
  border-radius:14px;
  padding:12px 6px; text-align:center;
  transition:all .15s ease;
}
.c-lbl {
  font-size:8px; color:var(--dim); text-transform:uppercase;
  letter-spacing:1.2px; margin-bottom:6px; font-weight:700;
}
.c-val { font-size:16px; font-weight:800; line-height:1; margin-bottom:3px; }
.c-sub { font-size:9px; color:var(--dim); }

/* ═══ Hero Card ═══ */
.hero-card {
  margin:12px 18px 0;
  background:linear-gradient(145deg, rgba(232,221,208,0.06), rgba(158,139,122,0.04));
  border:1px solid var(--border-hi);
  border-radius:var(--radius);
  padding:20px 18px 18px;
  position:relative; overflow:hidden;
  box-shadow:var(--shadow);
}
.hero-card::after {
  content:''; position:absolute; top:-50px; right:-30px;
  width:180px; height:180px;
  background:radial-gradient(circle, rgba(232,221,208,0.06), transparent 70%);
  pointer-events:none;
}
.hero-lbl {
  font-size:9px; font-weight:800; letter-spacing:2px;
  color:var(--mid); text-transform:uppercase; margin-bottom:12px;
  display:flex; align-items:center; gap:6px;
}
.hero-body { display:flex; align-items:center; gap:14px; }
.hero-info { flex:1; min-width:0; }
.hero-name {
  font-size:22px; font-weight:800; letter-spacing:-.5px;
  line-height:1.1; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;
}
.hero-sub { font-size:12px; color:var(--dim); margin-top:5px; }
.hero-baits { display:flex; flex-wrap:wrap; gap:5px; margin-top:10px; }
.hero-chip {
  font-size:10px; font-weight:700; padding:4px 10px;
  border-radius:20px;
  background:rgba(200,185,154,0.10);
  color:var(--good);
  border:1px solid rgba(158,139,122,0.20);
}

/* ═══ Baits Strip ═══ */
.baits-strip {
  margin:10px 18px 0;
  background:rgba(36,52,71,0.6);
  border:1px solid var(--border);
  border-radius:var(--radius);
  padding:16px; display:none;
}
.baits-hdr {
  font-size:9px; font-weight:800; letter-spacing:1.5px;
  color:var(--dim); text-transform:uppercase; margin-bottom:10px;
}
.baits-row { display:flex; flex-wrap:wrap; gap:6px; }
.bait-chip {
  display:flex; align-items:baseline; gap:5px;
  padding:6px 12px; border-radius:20px;
  background:rgba(200,185,154,0.08);
  border:1px solid var(--border);
  font-size:12px; font-weight:700; color:var(--good);
}
.bait-why { font-size:10px; color:var(--dim); font-weight:500; }

/* ═══ Refresh ═══ */
.refresh-bar { padding:12px 18px 0; text-align:center; }
.refresh-btn {
  background:rgba(232,221,208,0.06);
  border:1px solid var(--border);
  color:var(--mid);
  font-size:13px; font-weight:700; cursor:pointer;
  padding:10px 24px; border-radius:22px;
  display:inline-flex; align-items:center; gap:8px;
  transition:all .15s ease;
}
.refresh-btn:active { transform:scale(.96); opacity:.7; }
.ri { display:inline-block; }
.refresh-btn.loading .ri { animation:spin .7s linear infinite; }

/* ═══ SVG icons ═══ */
svg { display:inline-block; vertical-align:middle; fill:none; stroke:currentColor; stroke-width:2; stroke-linecap:round; stroke-linejoin:round; width:18px; height:18px; }
svg[style*="width"] { width:auto; height:auto; }
.ri, .ti, .sr-icon svg { width:auto; height:auto; }
.ri { width:18px; height:18px; }
.ti { width:22px; height:22px; }
.sr-icon svg { width:20px; height:20px; }
.icon-accent { color:var(--accent); }
.icon-dim { color:var(--dim); }

/* ═══ Lake Cards ═══ */
.section-lbl {
  padding:14px 18px 8px;
  font-size:10px; font-weight:800; letter-spacing:1.5px;
  color:var(--dim); text-transform:uppercase; display:none;
}
.lakes-list { padding:0 18px 16px; display:flex; flex-direction:column; gap:10px; }

/* Filter bar */
.filter-bar {
  display:flex; gap:7px; padding:10px 18px; overflow-x:auto;
  -webkit-overflow-scrolling:touch; scrollbar-width:none;
}
.filter-bar::-webkit-scrollbar { display:none; }
.filter-chip {
  flex-shrink:0; padding:7px 15px; border-radius:22px;
  font-size:12px; font-weight:600; letter-spacing:.2px;
  background:rgba(36,52,71,0.5);
  border:1px solid var(--border);
  color:var(--dim); cursor:pointer;
  transition:all .2s ease;
  white-space:nowrap;
}
.filter-chip.active {
  background:var(--accent); border-color:var(--accent);
  color:var(--bg); font-weight:700;
  box-shadow:0 2px 12px rgba(232,221,208,0.15);
}
.filter-chip:active { transform:scale(.95); }
.filter-sort-row {
  display:flex; align-items:center; gap:8px; padding:4px 18px 2px;
}
.filter-sort-row select {
  background:var(--card); color:var(--mid);
  border:1px solid var(--border);
  border-radius:10px; padding:6px 12px; font-size:12px;
  -webkit-appearance:none; appearance:none;
}
.filter-count {
  font-size:11px; color:var(--dim); margin-left:auto; padding-right:4px;
}

/* Card */
.lake-card {
  background:linear-gradient(160deg, var(--card), var(--card2));
  border:1px solid var(--border);
  border-radius:var(--radius);
  display:flex; overflow:hidden;
  animation:fadeUp .35s ease both;
  box-shadow:var(--shadow);
  transition:all .15s ease;
}
.lake-card:active { opacity:.8; transform:scale(.985); }
.card-bar   { width:4px; flex-shrink:0; }
.card-body  { flex:1; padding:14px 14px 12px; min-width:0; }
.card-top   { display:flex; align-items:flex-start; gap:10px; margin-bottom:8px; }
.card-info  { flex:1; min-width:0; }
.card-name  { font-size:15px; font-weight:700; margin-bottom:3px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
.card-meta  { font-size:11px; color:var(--dim); }
.card-right { display:flex; flex-direction:column; align-items:center; gap:3px; flex-shrink:0; }
.card-trend { font-size:12px; font-weight:800; }
.score-tags { display:flex; flex-wrap:wrap; gap:4px; margin-bottom:8px; }
.stag { padding:3px 8px; border-radius:6px; font-size:10px; font-weight:700; }
.stag.pos { background:rgba(200,185,154,.10); color:var(--good); }
.stag.neg { background:rgba(160,120,120,.12);  color:var(--bad);  }
.stag.neu { background:rgba(158,139,122,.08);   color:var(--dim);  }
.card-baits { display:flex; flex-wrap:wrap; gap:4px; }
.mini-chip {
  font-size:10px; font-weight:600; padding:2px 8px; border-radius:10px;
  background:rgba(232,221,208,.05); color:var(--mid);
  border:1px solid var(--border);
}

/* ═══ No-nearby warning ═══ */
.no-nearby {
  margin:0 18px 10px; padding:14px 16px;
  background:rgba(158,139,122,0.06);
  border:1px solid var(--border);
  border-radius:14px; font-size:12px; color:var(--mid); line-height:1.5;
}

/* ═══ Map ═══ */
.map-view { display:none; flex-direction:column; padding:12px 18px; }
.map-view.active { display:flex; }
.map-hdr {
  margin-bottom:10px; font-size:11px; font-weight:800;
  color:var(--dim); text-transform:uppercase; letter-spacing:1px;
}
#map {
  flex:1; border-radius:var(--radius);
  border:1px solid var(--border);
  min-height:400px;
  height:calc(100dvh - var(--tabh) - var(--st) - var(--sb) - 72px);
}
.leaflet-popup-content-wrapper {
  background:rgba(27,42,58,0.97)!important;
  backdrop-filter:blur(12px);
  color:var(--text)!important;
  border-radius:16px!important;
  border:1px solid var(--border-hi)!important;
  box-shadow:var(--shadow-lg)!important;
}
.leaflet-popup-tip { background:rgba(27,42,58,0.97)!important; }
.leaflet-popup-close-button { color:var(--dim)!important; font-size:20px!important; top:8px!important; right:10px!important; }
.leaflet-popup-content { margin:14px!important; font-family:-apple-system,sans-serif!important; font-size:13px!important; line-height:1.5!important; }
.popup-name  { font-size:16px; font-weight:800; margin-bottom:4px; }
.popup-score { display:inline-block; padding:3px 12px; border-radius:20px; font-weight:800; font-size:13px; margin:3px 0 8px; }
.popup-meta  { color:var(--dim); font-size:11px; margin-bottom:8px; }
.popup-tags  { display:flex; flex-wrap:wrap; gap:4px; }
.ptag        { padding:2px 7px; border-radius:6px; font-size:10px; font-weight:700; }
.map-legend.leaflet-control {
  background:rgba(27,42,58,.96)!important;
  backdrop-filter:blur(12px);
  border-radius:14px!important;
  padding:12px 14px!important;
  border:1px solid var(--border)!important;
  box-shadow:var(--shadow)!important;
}
.map-legend h4 { font-size:9px; text-transform:uppercase; letter-spacing:1px; color:var(--dim); margin-bottom:8px; }
.leg-item  { display:flex; align-items:center; gap:7px; margin-bottom:5px; font-size:11px; color:var(--mid); }
.leg-item:last-child { margin-bottom:0; }
.leg-dot   { width:11px; height:11px; border-radius:50%; flex-shrink:0; }
.marker-label {
  background:transparent!important; border:none!important; box-shadow:none!important;
  color:var(--text)!important; font-size:10px!important; font-weight:900!important;
  padding:0!important; text-shadow:0 1px 4px rgba(0,0,0,.8);
}
.marker-label:before { display:none!important; }
.leaflet-control-zoom a {
  background:rgba(27,42,58,.95)!important;
  color:var(--text)!important;
  border:1px solid var(--border)!important;
  border-radius:10px!important;
}
.leaflet-control-zoom a:hover { background:rgba(36,52,71,.95)!important; }

/* ═══ Tab bar ═══ */
.tab-bar {
  position:fixed; bottom:0; left:0; right:0;
  height:calc(var(--tabh) + var(--sb)); padding-bottom:var(--sb);
  background:rgba(15,22,30,0.90);
  backdrop-filter:blur(32px); -webkit-backdrop-filter:blur(32px);
  border-top:1px solid var(--border);
  display:flex; z-index:300;
}
.tab-btn {
  flex:1; display:flex; flex-direction:column;
  align-items:center; justify-content:center; gap:4px;
  border:none; background:none; color:var(--dim); cursor:pointer;
  font-size:9px; font-weight:700; text-transform:uppercase; letter-spacing:.6px;
  transition:color .2s ease;
}
.tab-btn .ti { font-size:22px; line-height:1; transition:transform .2s ease; }
img[src^="icons/"] { mix-blend-mode:screen; opacity:0.85; }
.tab-btn.active { color:var(--accent); }
.tab-btn.active .ti { transform:scale(1.12); }
.tab-btn:active { opacity:.6; }

/* ═══ Nearby ═══ */
.nearby-view { display:none; flex-direction:column; padding:12px 18px; }
.nearby-view.active { display:flex; flex-direction:column; }
.nearby-hdr { display:flex; align-items:center; justify-content:space-between; margin-bottom:12px; }
.nearby-hdr h3 { font-size:14px; font-weight:800; color:var(--text); }
.nearby-hdr span { font-size:11px; color:var(--dim); }
.nearby-gps-btn {
  width:100%; padding:16px; border-radius:var(--radius);
  background:linear-gradient(135deg, rgba(232,221,208,0.10), rgba(158,139,122,0.06));
  border:1.5px solid var(--border-hi);
  color:var(--accent); font-size:15px; font-weight:700; cursor:pointer;
  display:flex; align-items:center; justify-content:center; gap:10px;
  margin-bottom:12px;
  box-shadow:var(--shadow);
  transition:all .2s ease;
}
.nearby-gps-btn:active { opacity:.7; transform:scale(.98); }
.nearby-gps-btn.locating { color:var(--mid); border-color:var(--border-hi); }
.nearby-radius-row { display:flex; gap:8px; margin-bottom:12px; }
.radius-chip {
  flex:1; padding:10px 4px; border-radius:12px; text-align:center;
  background:var(--card); border:1px solid var(--border);
  font-size:12px; font-weight:700; color:var(--dim); cursor:pointer;
  transition:all .15s ease;
}
.radius-chip.active {
  background:var(--accent); border-color:var(--accent);
  color:var(--bg); font-weight:800;
}
.radius-chip:active { opacity:.6; }
.nearby-list { display:flex; flex-direction:column; gap:10px; }
.nearby-card {
  background:linear-gradient(160deg, var(--card), var(--card2));
  border:1px solid var(--border);
  border-radius:var(--radius); display:flex; overflow:hidden;
  animation:fadeUp .35s ease both;
  box-shadow:var(--shadow);
}
.nearby-card:active { opacity:.8; transform:scale(.985); }
.nc-bar  { width:4px; flex-shrink:0; }
.nc-body { flex:1; padding:14px 14px 12px; min-width:0; }
.nc-top  { display:flex; align-items:flex-start; gap:10px; margin-bottom:8px; }
.nc-info { flex:1; min-width:0; }
.nc-name { font-size:15px; font-weight:700; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; margin-bottom:3px; }
.nc-meta { font-size:11px; color:var(--dim); }
.nc-right { display:flex; flex-direction:column; align-items:center; gap:3px; flex-shrink:0; }
.nc-dist { font-size:12px; font-weight:800; }
.nc-tags { display:flex; flex-wrap:wrap; gap:4px; margin-bottom:8px; }
.nc-baits { display:flex; flex-wrap:wrap; gap:4px; }
.nc-note {
  margin-top:10px; padding:12px 14px;
  background:rgba(158,139,122,0.06);
  border:1px solid var(--border);
  border-radius:12px; font-size:11px; color:var(--mid); line-height:1.5;
}
.nearby-empty {
  display:flex; flex-direction:column; align-items:center;
  justify-content:center; padding:56px 20px; gap:14px; text-align:center;
}
.nearby-empty .ne-icon { font-size:48px; }
.nearby-empty p { font-size:14px; color:var(--mid); line-height:1.6; }
.nearby-empty small { font-size:11px; color:var(--dim); }

/* ═══ Loading / Error ═══ */
.loading-screen {
  display:flex; flex-direction:column; align-items:center;
  justify-content:center; padding:60px 20px; gap:16px;
  color:var(--dim); font-size:14px;
}
.spinner { width:36px; height:36px; border:3px solid var(--border); border-top-color:var(--mid); border-radius:50%; animation:spin .8s linear infinite; }
.error-msg {
  margin:18px; padding:16px;
  background:rgba(160,120,120,0.08);
  border:1px solid rgba(160,120,120,0.20);
  border-radius:var(--radius); color:var(--bad); font-size:13px;
  text-align:center; line-height:1.6;
}
footer { padding:20px 18px 8px; text-align:center; font-size:10px; color:var(--dim); line-height:1.8; }

/* ═══ Detail Panel ═══ */
.detail-overlay {
  position:fixed; inset:0; z-index:900;
  background:var(--bg);
  overflow-y:auto; -webkit-overflow-scrolling:touch;
  display:none; flex-direction:column;
  animation:slideIn .22s ease;
}
.detail-overlay.open { display:flex; }
@keyframes slideIn { from { opacity:0; transform:translateY(20px); } to { opacity:1; transform:translateY(0); } }

.detail-sheet {
  display:flex; flex-direction:column;
  min-height:100%;
  padding-bottom:calc(var(--sb) + 28px);
}

/* Top info */
.detail-top {
  padding:calc(var(--st) + 16px) 18px 0;
  background:linear-gradient(180deg, rgba(23,34,48,.95) 60%, transparent);
  position:relative;
}
.detail-close {
  display:inline-flex; align-items:center; gap:5px;
  background:none; border:none;
  color:var(--mid); font-size:14px; font-weight:700;
  cursor:pointer; padding:8px 0 16px; letter-spacing:-.2px;
  transition:color .15s;
}
.detail-close:active { opacity:.5; }
.detail-badge {
  display:inline-flex; align-items:center; gap:6px;
  font-size:10px; font-weight:800; letter-spacing:2px;
  text-transform:uppercase; color:var(--mid); margin-bottom:10px;
}
.detail-name {
  font-size:28px; font-weight:900; letter-spacing:-.7px;
  line-height:1.05; margin-bottom:6px;
}
.detail-meta { font-size:13px; color:var(--dim); margin-bottom:16px; }
.detail-score-row { display:flex; align-items:center; gap:16px; margin-bottom:18px; }
.detail-ring { flex-shrink:0; }
.detail-score-info { flex:1; }
.detail-score-label {
  font-size:11px; font-weight:700; color:var(--dim);
  text-transform:uppercase; letter-spacing:1px; margin-bottom:5px;
}
.detail-score-tags { display:flex; flex-wrap:wrap; gap:5px; }

/* Map strip */
.detail-map-strip { width:100%; height:300px; flex-shrink:0; position:relative; }
#detailMap { width:100%; height:100%; }

/* Photos */
.detail-photos { display:grid; grid-template-columns:1fr 1fr; gap:8px; }
.detail-photos img {
  width:100%; height:140px; object-fit:cover;
  border-radius:12px; display:block;
  background:var(--card);
}
.detail-photo-placeholder {
  grid-column:1/-1;
  height:64px; display:flex; align-items:center; justify-content:center;
  color:var(--dim); font-size:12px; font-weight:600;
}
.detail-photo-credit {
  grid-column:1/-1;
  font-size:9px; color:var(--dim); text-align:right; padding-right:2px;
}

/* Bottom info */
.detail-bottom { background:var(--bg); padding:18px 18px 0; flex:1; }
.detail-section-title {
  font-size:10px; font-weight:800; letter-spacing:1.5px;
  text-transform:uppercase; color:var(--dim); margin-bottom:12px;
}

/* Strategy */
.strategy-block {
  background:rgba(36,52,71,0.5);
  border:1px solid var(--border);
  border-radius:var(--radius); padding:16px; margin-bottom:14px;
}
.strategy-row {
  display:flex; gap:12px; align-items:flex-start;
  padding:10px 0; border-bottom:1px solid var(--border);
}
.strategy-row:last-child { border-bottom:none; padding-bottom:0; }
.strategy-row:first-child { padding-top:0; }
.sr-icon { font-size:20px; flex-shrink:0; margin-top:1px; }
.sr-body { flex:1; min-width:0; }
.sr-label { font-size:11px; font-weight:800; color:var(--mid); text-transform:uppercase; letter-spacing:.8px; margin-bottom:3px; }
.sr-text  { font-size:13px; color:var(--text); line-height:1.5; }

/* Bait chips */
.detail-baits { display:flex; flex-wrap:wrap; gap:8px; margin-bottom:16px; }
.detail-bait-chip {
  display:flex; align-items:baseline; gap:6px;
  padding:8px 14px; border-radius:22px;
  background:rgba(200,185,154,0.08);
  border:1px solid var(--border);
  font-size:12px; font-weight:700; color:var(--good);
}
.dbc-why { font-size:10px; color:var(--dim); font-weight:500; }

/* Directions */
.directions-row { display:flex; gap:10px; margin-bottom:8px; }
.dir-btn {
  flex:1; padding:14px 10px;
  border-radius:var(--radius); border:none; cursor:pointer;
  font-size:14px; font-weight:800;
  display:flex; align-items:center; justify-content:center; gap:8px;
  transition:all .15s ease;
}
.dir-btn:active { opacity:.7; transform:scale(.97); }
.dir-apple {
  background:linear-gradient(135deg, var(--card-hi), var(--card2));
  border:1px solid var(--border-hi); color:var(--text);
}
.dir-google {
  background:linear-gradient(135deg, rgba(232,221,208,0.10), rgba(158,139,122,0.06));
  border:1px solid var(--border); color:var(--accent);
}

@keyframes spin  { to { transform:rotate(360deg); } }
@keyframes fadeUp { from { opacity:0; transform:translateY(14px) scale(.98); } to { opacity:1; transform:translateY(0) scale(1); } }
.lake-card:nth-child(1){animation-delay:0ms}
.lake-card:nth-child(2){animation-delay:30ms}
.lake-card:nth-child(3){animation-delay:60ms}
.lake-card:nth-child(4){animation-delay:90ms}
.lake-card:nth-child(5){animation-delay:120ms}
.lake-card:nth-child(n+6){animation-delay:150ms}"""

c = c[:style_start] + new_style + c[style_end:]

# Fix some HTML inline styles
c = c.replace(
    'style="width:28px;height:28px;vertical-align:middle;margin-right:6px;border-radius:6px;object-fit:contain;background:var(--card);padding:2px"',
    'style="width:30px;height:30px;vertical-align:middle;margin-right:8px;border-radius:8px;object-fit:contain;background:var(--card2);padding:3px"'
)

with open(path, 'w') as f:
    f.write(c)

print("UI overhaul CSS written successfully")
print(f"Total file size: {len(c)} bytes")
