
# 🏠 Byggekostnadsprediksjon – FastAPI + React + Docker

Dette prosjektet er et komplett fullstack-oppsett for maskinlæring og webutvikling, som predikerer byggekostnadsindeks i Norge basert på data fra Statistisk sentralbyrå (SSB). Det gir både et REST API (FastAPI) og en brukervennlig frontend (React), og alt kan kjøres lokalt eller containeriseres med Docker.

---

## 🎯 Prosjektmål

Dette prosjektet ble laget for å:
- Utforske hvordan man trener og bruker en ML-modell for prediksjon
- Lære å bygge og eksponere en ML-modell gjennom et REST API (FastAPI)
- Utvikle en interaktiv frontend med React
- Bruke Docker for enkel distribusjon og lokal kjøring
- Forstå hvordan backend og frontend jobber sammen
- Koble ML, API og UI i ett prosjekt – et komplett dataprodukt

---

## 🧱 Teknologistack

| Komponent       | Teknologi             |
|----------------|------------------------|
| ML-modell       | scikit-learn (RandomForest) |
| Modell-lagring  | joblib                 |
| Backend API     | FastAPI                |
| Frontend UI     | React                  |
| Data            | SSB (API)              |
| Deploy (API)    | Render.com             |
| Frontend (dev)  | CodeSandbox / Vercel   |
| Containerisering| Docker                 |

---

## 🧠 Hva gjør appen?

Brukeren kan:
- Velge et år, måned og type arbeid (f.eks. "12 Carpentry, total")
- Trykke "Forutsi indeks"
- Motta en byggekostnadsindeks som viser hvor mye kostnaden har endret seg relativt til 2015

🟢 En indeks på 140 betyr en 40 % økning i byggekostnader sammenlignet med 2015 (2015 = 100).

---

## 🗂️ Prosjektstruktur

```
.
├── app.py                   # FastAPI-backend
├── requirements.txt        # Python-avhengigheter
├── Dockerfile              # Lager et komplett backend-miljø
├── src/                    # React frontend
│   ├── App.js              # Hovedkomponenten
│   └── styles.css          # Brukergrensesnittstil
├── public/                 # HTML-inngangspunkt for React
│   └── index.html
├── package.json            # React-avhengigheter
└── README.md
```

---

## ⚙️ Hvordan kjøre lokalt

### 🐍 1. Kjør backend (FastAPI)

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

Åpne API-dokumentasjon: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### 🌐 2. Kjør frontend (React)

```bash
npm install
npm start
```

Frontend åpnes her: [http://localhost:3000](http://localhost:3000)

---

### 🐳 3. Kjør hele backend med Docker

Bygg og start backend via Docker:

```bash
docker build -t bolig-api .
docker run -p 8000:8000 bolig-api
```

Dette starter FastAPI og eksponerer `/predict`-endepunktet.

---

## 🔗 Live demo

- 🧪 API-dokumentasjon:  
  `https://boligprediksjon-fastapi.onrender.com/docs`

- 🌐 React UI (hostet via CodeSandbox):  
  [https://9qndjl.csb.app](https://9qndjl.csb.app)

---

## 📦 Eksempel på API-kall

```json
POST /predict
{
  "year": 2024,
  "month_num": 5,
  "type_of_employment": "12 Carpentry, total"
}
```

Respons:

```json
{
  "predicted_index": 129.83
}
```

---

## ✨ Hva jeg har lært

- Hvordan hente og bearbeide offentlig statistikk fra SSB
- Hvordan trene og bruke ML-modeller med scikit-learn
- Hvordan eksponere modeller gjennom FastAPI
- Hvordan bruke joblib for modell-lagring
- Hvordan utvikle og style et React-grensesnitt
- Hvordan bygge og kjøre backend i en Docker-container
- Hvordan koble frontend og backend med fetch() og CORS

---


