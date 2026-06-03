// ── Constants ─────────────────────────────────────────────────────────────────
const STATE_COLOR = { red: '#f85149', yellow: '#d29922', green: '#3fb950' };
const STATE_DIM   = { red: '#2d0d0d', yellow: '#2d1f00', green: '#0d2e0d' };
const STATES      = ['red', 'yellow', 'green'];
const LIGHT_CY    = [75, 150, 225];


// ── Traffic light (D3 SVG) ────────────────────────────────────────────────────
const tlSvg = d3.select('#traffic-light-svg');

// Housing
tlSvg.append('rect')
    .attr('x', 20).attr('y', 10)
    .attr('width', 120).attr('height', 270)
    .attr('rx', 20)
    .attr('fill', '#0d1117')
    .attr('stroke', '#30363d')
    .attr('stroke-width', 2);

// Glow filters (one per state color)
const defs = tlSvg.append('defs');
STATES.forEach(s => {
    const f = defs.append('filter')
        .attr('id', `glow-${s}`)
        .attr('x', '-60%').attr('y', '-60%')
        .attr('width', '220%').attr('height', '220%');
    f.append('feGaussianBlur').attr('stdDeviation', 10).attr('result', 'blur');
    const merge = f.append('feMerge');
    merge.append('feMergeNode').attr('in', 'blur');
    merge.append('feMergeNode').attr('in', 'SourceGraphic');
});

const circles = tlSvg.selectAll('circle.light')
    .data(STATES)
    .join('circle')
    .attr('class', 'light')
    .attr('cx', 80)
    .attr('cy', (_, i) => LIGHT_CY[i])
    .attr('r', 38)
    .attr('fill', d => STATE_DIM[d]);

let currentState = null;

function setLight(state) {
    if (state === currentState) return;
    currentState = state;

    circles
        .transition().duration(300)
        .attr('fill',   d => d === state ? STATE_COLOR[d] : STATE_DIM[d])
        .attr('filter', d => d === state ? `url(#glow-${d})` : null);

    const nameEl = document.getElementById('state-name');
    nameEl.textContent = state ? state.toUpperCase() : '--';
    nameEl.style.color = STATE_COLOR[state] || '#e6edf3';
    document.getElementById('state-ts').textContent =
        `Updated: ${new Date().toLocaleTimeString()}`;
}


// ── Tooltip ───────────────────────────────────────────────────────────────────
const tip = document.getElementById('tooltip');

function showTip(evt, html) {
    tip.innerHTML = html;
    tip.style.opacity = 1;
    tip.style.left = (evt.clientX + 14) + 'px';
    tip.style.top  = (evt.clientY - 10) + 'px';
}

function hideTip() { tip.style.opacity = 0; }


// ── Timeline chart ────────────────────────────────────────────────────────────
let historyData = [];

function renderTimeline() {
    const wrap = document.getElementById('timeline-wrap');
    wrap.innerHTML = '';

    if (historyData.length < 2) {
        wrap.innerHTML = '<p style="color:#8b949e;padding:1rem;font-style:italic">Not enough data yet</p>';
        return;
    }

    // Show only the last 3 minutes relative to the latest record so that short
    // states like yellow (6 s) remain wide enough to see clearly.
    const WINDOW_MS  = 3 * 60 * 1000;
    const lastTs     = new Date(historyData.at(-1).timestamp);
    const windowStart = new Date(+lastTs - WINDOW_MS);

    // Include the record just before the window so the first bar fills to the left edge.
    let startIdx = 0;
    for (let i = historyData.length - 1; i > 0; i--) {
        if (new Date(historyData[i].timestamp) < windowStart) {
            startIdx = i;
            break;
        }
    }
    const visible = historyData.slice(startIdx);

    if (visible.length < 2) {
        wrap.innerHTML = '<p style="color:#8b949e;padding:1rem;font-style:italic">Not enough data yet</p>';
        return;
    }

    const intervals = visible.slice(0, -1).map((r, i) => ({
        state: r.state,
        start: new Date(r.timestamp),
        end:   new Date(visible[i + 1].timestamp),
    }));

    const m = { top: 20, right: 16, bottom: 40, left: 16 };
    const W = wrap.clientWidth || 600;
    const w = W - m.left - m.right;
    const BAR_H = 48;
    const H = BAR_H + 20;

    const x = d3.scaleTime()
        .domain([intervals[0].start, intervals.at(-1).end])
        .range([0, w]);

    const svg = d3.select(wrap).append('svg')
        .attr('width', W)
        .attr('height', H + m.top + m.bottom);

    const g = svg.append('g').attr('transform', `translate(${m.left},${m.top})`);

    g.selectAll('rect.seg')
        .data(intervals)
        .join('rect')
        .attr('class', 'seg')
        .attr('x',      d => x(d.start))
        .attr('y',      (H - BAR_H) / 2)
        .attr('width',  d => Math.max(1, x(d.end) - x(d.start)))
        .attr('height', BAR_H)
        .attr('fill',   d => STATE_COLOR[d.state] || '#666')
        .attr('rx', 3)
        .on('mousemove', (evt, d) => {
            const secs = Math.round((d.end - d.start) / 1000);
            showTip(evt, `<strong>${d.state.toUpperCase()}</strong><br>${secs}s`);
        })
        .on('mouseleave', hideTip);

    g.append('g')
        .attr('class', 'axis')
        .attr('transform', `translate(0,${(H + BAR_H) / 2 + 6})`)
        .call(d3.axisBottom(x).ticks(6).tickFormat(d3.timeFormat('%H:%M:%S')));
}


// ── Stats chart ───────────────────────────────────────────────────────────────
function renderStats(stats) {
    const wrap = document.getElementById('stats-wrap');
    wrap.innerHTML = '';

    if (!stats || stats.length === 0) {
        wrap.innerHTML = '<p style="color:#8b949e;padding:1rem;font-style:italic">No data yet</p>';
        return;
    }

    const m = { top: 10, right: 60, bottom: 10, left: 70 };
    const W = wrap.clientWidth || 600;
    const BAR_H = 38, GAP = 14;
    const H = stats.length * (BAR_H + GAP) - GAP;
    const w = W - m.left - m.right;

    const x = d3.scaleLinear()
        .domain([0, d3.max(stats, d => d.count)])
        .range([0, w]);

    const y = d3.scaleBand()
        .domain(stats.map(d => d.state))
        .range([0, H])
        .padding(GAP / (BAR_H + GAP));

    const svg = d3.select(wrap).append('svg')
        .attr('width', W)
        .attr('height', H + m.top + m.bottom);

    const g = svg.append('g').attr('transform', `translate(${m.left},${m.top})`);

    // Bars
    g.selectAll('rect.bar')
        .data(stats)
        .join('rect')
        .attr('class', 'bar')
        .attr('x', 0)
        .attr('y', d => y(d.state))
        .attr('width',  d => x(d.count))
        .attr('height', y.bandwidth())
        .attr('fill',   d => STATE_COLOR[d.state] || '#8b949e')
        .attr('rx', 4);

    // State name labels
    g.selectAll('text.lbl-state')
        .data(stats)
        .join('text')
        .attr('class', 'lbl-state')
        .attr('x', -8)
        .attr('y', d => y(d.state) + y.bandwidth() / 2 + 5)
        .attr('text-anchor', 'end')
        .attr('font-size', 13)
        .attr('font-weight', 700)
        .attr('fill', d => STATE_COLOR[d.state] || '#8b949e')
        .text(d => d.state.toUpperCase());

    // Count labels
    g.selectAll('text.lbl-count')
        .data(stats)
        .join('text')
        .attr('class', 'lbl-count')
        .attr('x', d => x(d.count) + 8)
        .attr('y', d => y(d.state) + y.bandwidth() / 2 + 5)
        .attr('font-size', 12)
        .text(d => d.count);
}


// ── REST API ──────────────────────────────────────────────────────────────────
async function loadHistory() {
    try {
        const res = await fetch('/api/history?limit=200');
        if (!res.ok) return;
        historyData = await res.json();
        if (historyData.length > 0) setLight(historyData.at(-1).state);
        renderTimeline();
    } catch (e) {
        console.error('Failed to load history:', e);
    }
}

async function loadStats() {
    try {
        const res = await fetch('/api/stats');
        if (!res.ok) return;
        renderStats(await res.json());
    } catch (e) {
        console.error('Failed to load stats:', e);
    }
}


// ── MQTT (WebSocket) ──────────────────────────────────────────────────────────
const badge = document.getElementById('mqtt-badge');

function setBadge(cls, text) {
    badge.className = `badge ${cls}`;
    badge.textContent = `MQTT: ${text}`;
}

// Connect to Mosquitto's WebSocket listener on port 9001.
// window.location.hostname resolves correctly whether running on
// localhost or on a remote host such as a Raspberry Pi.
const mqttClient = mqtt.connect(`ws://${window.location.hostname}:9001`, {
    clientId: `dashboard_${Math.random().toString(16).slice(2, 8)}`,
    reconnectPeriod: 3000,
    connectTimeout: 5000,
});

mqttClient.on('connect', () => {
    setBadge('badge-connected', 'Connected');
    mqttClient.subscribe('traffic_light/state');
});
mqttClient.on('reconnect', () => setBadge('badge-connecting', 'Reconnecting'));
mqttClient.on('error',     () => setBadge('badge-disconnected', 'Error'));
mqttClient.on('close',     () => setBadge('badge-connecting', 'Reconnecting'));

mqttClient.on('message', (topic, msg) => {
    try {
        const { state, timestamp } = JSON.parse(msg.toString());
        const record = { state, timestamp: timestamp || new Date().toISOString() };

        historyData.push(record);
        if (historyData.length > 200) historyData.shift();

        setLight(state);
        renderTimeline();
        loadStats();
    } catch (e) {
        console.error('MQTT message error:', e);
    }
});


// ── Initialise ────────────────────────────────────────────────────────────────
loadHistory();
loadStats();

// Refresh historical data every 30 seconds as a fallback
setInterval(() => { loadHistory(); loadStats(); }, 30_000);
