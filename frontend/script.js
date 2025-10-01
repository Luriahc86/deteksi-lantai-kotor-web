function showPage(page) {
  document.querySelectorAll(".page").forEach(p => p.style.display = "none");
  document.getElementById(page).style.display = "";
  document.querySelectorAll(".sidebar a").forEach(a => a.classList.remove("active"));
  let index = ["dashboard", "history", "live", "notif"].indexOf(page);
  if (index !== -1) document.querySelectorAll(".sidebar a")[index].classList.add("active");
}

function previewImage(event) {
  const output = document.getElementById("preview");
  output.innerHTML = "";
  if (event.target.files.length) {
    const img = document.createElement("img");
    img.src = URL.createObjectURL(event.target.files[0]);
    output.appendChild(img);
  }
}

function dummyDetect() {
  const preview = document.getElementById("preview");
  if (!preview.querySelector("img")) {
    alert("⚠️ Pilih gambar dulu!");
    return;
  }
  alert("✅ Deteksi selesai! Status: Kotor (dummy)");
  addHistory("Kotor", preview.querySelector("img").src);
}

function addHistory(status, imgSrc) {
  let history = JSON.parse(localStorage.getItem("histori") || "[]");
  history.unshift({ time: new Date().toLocaleString(), status, img: imgSrc });
  localStorage.setItem("histori", JSON.stringify(history));
  renderHistory();
}

function renderHistory() {
  const tbody = document.getElementById("historyTable");
  tbody.innerHTML = "";
  let history = JSON.parse(localStorage.getItem("histori") || "[]");
  history.forEach(h => {
    let tr = document.createElement("tr");
    tr.innerHTML = `<td>${h.time}</td><td>${h.status}</td><td><img src="${h.img}" width="80"></td>`;
    tbody.appendChild(tr);
  });
}

function showCCTV() {
  const link = document.getElementById("cctvLink").value;
  const video = document.getElementById("cctvVideo");
  if (link) {
    video.src = link;
    video.style.display = "";
  } else {
    video.src = "";
    video.style.display = "none";
  }
}

function tambahKontak() {
  let nama = document.getElementById("namaKontak").value.trim();
  let kontak = document.getElementById("kontak").value.trim();
  if (!nama || !kontak) return;
  let daftar = JSON.parse(localStorage.getItem("kontakNotif") || "[]");
  daftar.push({ nama, kontak });
  localStorage.setItem("kontakNotif", JSON.stringify(daftar));
  document.getElementById("namaKontak").value = "";
  document.getElementById("kontak").value = "";
  renderKontak();
}

function renderKontak() {
  let daftar = JSON.parse(localStorage.getItem("kontakNotif") || "[]");
  let ul = document.getElementById("daftarKontak");
  ul.innerHTML = "";
  daftar.forEach((k, i) => {
    let li = document.createElement("li");
    li.innerHTML = `<span><b>${k.nama}</b>: ${k.kontak}</span> <button onclick="hapusKontak(${i})">Hapus</button>`;
    ul.appendChild(li);
  });
}
function hapusKontak(i) {
  let daftar = JSON.parse(localStorage.getItem("kontakNotif") || "[]");
  daftar.splice(i, 1);
  localStorage.setItem("kontakNotif", JSON.stringify(daftar));
  renderKontak();
}

function toggleMode() {
  document.body.classList.toggle("dark");
}

window.onload = function() {
  renderHistory();
  renderKontak();
  showPage('dashboard');
};
// ... (fungsi sebelumnya tetap) ...

function toggleSidebar() {
  document.getElementById("sidebar").classList.toggle("active");
}

function toggleMode() {
  document.body.classList.toggle("dark");
}

window.onload = function() {
  renderHistory();
  renderKontak();
  showPage('dashboard');
};
function toggleSidebar() {
  document.getElementById("sidebar").classList.toggle("active");
}

function toggleMode() {
  document.body.classList.toggle("dark");
}

// fungsi lainnya tetap sama...
window.onload = function() {
  renderHistory();
  renderKontak();
  showPage('dashboard');
};
