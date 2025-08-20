# 🧮 FastAPI Math Service

## 📌 Descriere
Acest proiect implementează un **microserviciu FastAPI** care expune o API REST pentru operații matematice de bază:

- Putere (`a^b`)
- Factorial (`n!`)
- Fibonacci (seria sau elementul `n`)

Toate cererile sunt logate într-o bază de date **Oracle**, utilizând utilizatorul `userpy` și tablespace-ul `tema_Py`.  
Proiectul respectă arhitectura **MVC/MVCS**, utilizează **Pydantic** pentru validare și este compatibil cu `flake8`.

---

## ⚙️ Funcționalități
- ✅ Operații matematice (Power, Factorial, Fibonacci)  
- ✅ Persistență în DB (logare cereri + rezultate)  
- ✅ Structură modulară (MVC/MVCS)  
- ✅ Validare input/output cu **Pydantic**  
- ✅ Standardizare cod cu **flake8**  
- ⚡ Opțional: execuție asincronă și workers  

---

## 🛠️ Tehnologii folosite
- [Python 3.10+](https://www.python.org/)  
- [FastAPI](https://fastapi.tiangolo.com/)  
- [Pydantic](https://docs.pydantic.dev/)  
- [cx_Oracle](https://oracle.github.io/python-cx_Oracle/)  
- [SQLAlchemy](https://www.sqlalchemy.org/) (opțional pentru ORM)  
- [Uvicorn](https://www.uvicorn.org/)  
- [Flake8](https://flake8.pycqa.org/)  

---

## 📂 Structura proiectului

---

## ⚙️ Funcționalități

- ✅ `POST /math/power` — calculează `a^b`
- ✅ `POST /math/factorial` — calculează `n!`
- ✅ `POST /math/fibonacci` — serie sau elementul `n`
- ✅ Logare cereri în Oracle (operație, parametri, rezultat, timestamp)
- ✅ Pydantic pentru validare I/O
- ✅ Conform PEP8 (flake8)

---

## 🛠️ Cerințe

- Python **3.10+**
- Oracle DB local (ex. `XE`)
- Oracle Instant Client (necesar pentru `cx_Oracle`)

---

## 🚀 Instalare și rulare

1) **Clonează repo**
```bash
git clone https://github.com/popmircea27/mathAPI.git
cd fastapi-math
