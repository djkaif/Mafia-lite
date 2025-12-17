const params = new URLSearchParams(location.search);
const code = params.get("code");
const API = "https://YOUR_BACKEND_URL";

async function load() {
  const res = await fetch(`${API}/state?code=${code}`);
  const data = await res.json();
  document.getElementById("status").innerText = "Phase: " + data.phase;
  document.getElementById("data").innerText = JSON.stringify(data, null, 2);
}

setInterval(load, 3000);
