import csv
import requests

# URL of the Flask API
url = 'http://192.168.1.6:5000/predict'

# Path to your CSV file
csv_file_path = r'E:\SpaceRocket\Live Trainings and Courses\AI Workplace\AISE\Work\ASSIGN\8_8_2024 flight_price\test_data.csv'

# Read the CSV file
try:
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        
        # Iterate through each row in the CSV file
        for row in csv_reader:
            # Prepare the data dictionary
            data = {
                'airline': int(row['airline']),  # Convert string to int if necessary
                'source_city': int(row['source_city']),
                'departure_time': int(row['departure_time']),
                'stops': int(row['stops']),
                'arrival_time': int(row['arrival_time']),
                'destination_city': int(row['destination_city']),
                'class': int(row['class']),
                'duration': float(row['duration']),
                'days_left': int(row['days_left'])
            }
            
            # Send the POST request to the Flask API with a timeout of 10 seconds
            try:
                response = requests.get(url, json=data, timeout=10)
                response.raise_for_status()  # Raise an exception for HTTP errors

                # Print the prediction result
                print(f"Prediction for row {row}: {response.json()}")
            
            except requests.exceptions.RequestException as e:
                print(f"Request failed for row {row}: {e}")
except FileNotFoundError:
    print(f"CSV file not found: {csv_file_path}")
except Exception as e:
    print(f"An error occurred while processing the CSV file: {e}")
