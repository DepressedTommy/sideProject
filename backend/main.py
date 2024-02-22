from flask import Flask, jsonify
from weather_utils import get_pt_data

app = Flask(__name__)

# Define a route for handling GET requests to /weather/pt
@app.route('/weather/pt', methods=['GET'])
def weather_pt():
    try:
        # Call the get_pt_data function to fetch weather data for Portugal
        weather_data_pt = get_pt_data()
        
        if weather_data_pt:
            # Return a JSON response containing the weather data
            return jsonify(weather_data_pt), 200
        else:
            # Return an error response if weather data could not be fetched
            return jsonify({'error': 'Failed to fetch weather data for Portugal'}), 500
    except ConnectionError:
        # Handle connection errors
        return jsonify({'error': 'Failed to connect to the weather API'}), 500
    except TimeoutError:
        # Handle timeout errors
        return jsonify({'error': 'Request to weather API timed out'}), 500
    except Exception as e:
        # Return a generic error response if an unexpected exception occurs
        return jsonify({'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True)