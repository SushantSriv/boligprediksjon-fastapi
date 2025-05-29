import React, { useState } from "react";
import "./styles.css";

export default function App() {
  const [year, setYear] = useState(2024);
  const [month, setMonth] = useState(5);
  const [type, setType] = useState("12 Carpentry, total");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const predict = async () => {
    setLoading(true);
    setResult(null);

    const response = await fetch(
      "https://boligprediksjon-fastapi.onrender.com/predict",
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          year: parseInt(year),
          month_num: parseInt(month),
          type_of_employment: type,
        }),
      }
    );

    const data = await response.json();
    setResult(data.predicted_index);
    setLoading(false);
  };

  return (
    <div className="App">
      <h1>🔧 Byggekostnadsprediksjon</h1>

      <div className="info">
        <p>
          Denne applikasjonen forutsier byggekostnadsindeksen for en valgt type
          arbeid i boligbygging i Norge. Dataene er hentet fra Statistisk
          sentralbyrå (SSB), og modellen er trent på historiske data.
        </p>
        <p>
          <strong>Indeksen</strong> viser relative kostnader sammenlignet med
          nivået i 2015 (2015 = 100). En indeks på f.eks. 135 betyr at kostnaden
          har økt med 35 % siden 2015.
        </p>
      </div>

      <label>År:</label>
      <input value={year} onChange={(e) => setYear(e.target.value)} />

      <label>Måned:</label>
      <input value={month} onChange={(e) => setMonth(e.target.value)} />

      <label>Arbeidstype:</label>
      <select value={type} onChange={(e) => setType(e.target.value)}>
        <option>12 Carpentry, total</option>
        <option>13 Carpentry, materials</option>
        <option>16 Plumbing, total</option>
        <option>17 Plumbing, materials</option>
        <option>18 Electrical installation work, total</option>
        <option>19 Electrical installation work, materials</option>
      </select>

      <button onClick={predict} disabled={loading}>
        {loading ? "Forutsier..." : "Forutsi indeks"}
      </button>

      {result && (
        <p className="result">
          🔮 <strong>Predikert byggekostnadsindeks:</strong> {result}
        </p>
      )}
    </div>
  );
}
