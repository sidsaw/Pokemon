from flask import Flask, request
app = Flask(__name__)

print("Starting up the Pokémon Server")

# Listen for post requests
@app.route('/', methods=['GET', 'POST'])
def result():
	print("Received packets")
	return 'Received!'


# Get file list

# Check database for missing files


if __name__ == "__main__":
    app.run(host='0.0.0.0')