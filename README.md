# Deploying this project with Streamlit

Quick steps to run locally:

1. Create and activate a Python environment (recommended).
2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the app locally:

```
streamlit run app.py
```

Deployment to Streamlit Cloud:

- Create a new repository containing these files and your `Airbnb_Open_Data.csv`.
- On https://streamlit.io, choose "New app" and connect your repo, selecting `app.py` as the entrypoint.

Notes:

- If the CSV is large, consider sampling or uploading a smaller version for the cloud.
- Edit `app.py` to surface the specific charts or KPIs from your notebook as needed.
