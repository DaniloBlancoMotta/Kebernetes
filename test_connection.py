import requests
import time

def test_server():
    url = 'http://localhost:8787/predict'
    
    customer = {
        "gender": "female",
        "seniorcitizen": 0,
        "partner": "yes",
        "dependents": "no",
        "phoneservice": "no",
        "multiplelines": "no_phone_service",
        "internetservice": "dsl",
        "onlinesecurity": "no",
        "onlinebackup": "yes",
        "deviceprotection": "no",
        "techsupport": "no",
        "streamingtv": "no",
        "streamingmovies": "no",
        "contract": "month-to-month",
        "paperlessbilling": "yes",
        "paymentmethod": "electronic_check",
        "tenure": 1,
        "monthlycharges": 29.85,
        "totalcharges": 29.85
    }
    
    try:
        response = requests.post(url, json=customer, timeout=5)
        if response.status_code == 200:
            result = response.json()
            print("Success! Server is running.")
            print(f"Response: {result}")
            return True
        else:
            print(f"Server responded with status code: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("Error: Cannot connect to server. Make sure Flask server is running.")
        print("Run 'python predict.py' in another terminal first.")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    test_server()