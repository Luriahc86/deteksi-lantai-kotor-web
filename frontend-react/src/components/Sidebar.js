import React from "react";

export default function Sidebar({ current, onMenu }) {
  const menu = [
    { key: "dashboard", label: "Dashboard" },
    { key: "history", label: "Histori Deteksi" },
    { key: "live", label: "Live CCTV" },
    { key: "notif", label: "Notifikasi" },
  ];
  return (
    <div style={{ width: 180, background: "#f2f2f2", padding: 16, minHeight: "100vh" }}>
      <h3 style={{ fontSize: 18 }}>Menu</h3>
      <ul style={{ listStyle: "none", padding: 0 }}>
        {menu.map((m) => (
          <li key={m.key}>
            <button
              style={{
                width: "100%",
                padding: "8px 0",
                margin: "6px 0",
                background: current === m.key ? "#cde" : "#fff",
                border: "1px solid #ccc",
                cursor: "pointer",
              }}
              onClick={() => onMenu(m.key)}
            >
              {m.label}
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}