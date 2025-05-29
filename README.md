
# 🏠 Byggekostnadsprediksjon – FastAPI + React

Et komplett fullstack-prosjekt som predikerer byggekostnadsindeks i Norge.  
Bygger på data fra [SSB](https://data.ssb.no/api/v0/dataset/1056?lang=en), og tilbyr et REST API med FastAPI + en responsiv frontend bygget i React.

---

## 📁 Prosjektstruktur

```
.
├── app.py                   # FastAPI-backend
├── requirements.txt        # Python-avhengigheter
├── Dockerfile              # For containerisering
├── src/                    # React-app (JS + CSS)
│   ├── App.js
│   ├── styles.css
│   └── ...
├── public/                 # HTML for React
│   └── index.html
├── package.json            # React dependencies
└── README.md
```

---

## 🚀 Teknologistack

| Komponent   | Teknologi             |
|------------|------------------------|
| Backend    | FastAPI (Python)       |
| Modell     | scikit-learn           |
| Frontend   | React (JS)             |
| Hosting API| Render.com             |
| Frontend Dev| CodeSandbox / Vercel  |
| Data       | SSB (Statistisk sentralbyrå) |

---

## 🎬 Live demo

- 🔗 React UI (CodeSandbox):  
  👉 [https://9qndjl.csb.app](https://9qndjl.csb.app)

- 🔗 Swagger UI (API – kan være blokkert i firma):  
  👉 https://boligprediksjon-fastapi.onrender.com/docs

---

## 📦 Hvordan kjøre lokalt

### 🐍 Backend (FastAPI):

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

📍 Åpne Swagger-dokumentasjon:  
[http://localhost:8000/docs](http://localhost:8000/docs)

---

### 🌐 Frontend (React):

```bash
npm install
npm start
```

📍 Appen kjører på:  
[http://localhost:3000](http://localhost:3000)

---

## 🔮 Hva gjør appen?

Brukeren velger:
- År (`year`)
- Måned (`month_num`)
- Type arbeid (`type_of_employment`)

Appen sender en POST til API-et som svarer med:

```json
{ "predicted_index": 127.9 }
```

---

## ℹ️ Hva betyr indeksen?

> Indeksen viser hvor mye byggekostnadene har økt siden 2015, der 2015 = 100.  
> En indeks på 130 betyr 30 % økning i kostnad.

---

## 📬 Kontakt

Laget av [Sushant Srivastava](https://github.com/SushantSriv)  
Bidrag og tilbakemeldinger er velkomne!
