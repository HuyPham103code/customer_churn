import joblib

try:
    model_path = r'D:\nam_3\data_analysis\customer_churn\grid_search_results.pkl'
    loaded_model = joblib.load(model_path)
    print("Model loaded successfully!")
except Exception as e:
    print("Error loading model:", str(e))