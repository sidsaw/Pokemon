from flask import Flask, request, jsonify
import json
app = Flask(__name__)

print("Starting Pokemon Server!")

# Listen for post requests
@app.route('/', methods=['GET', 'POST'])
def server():
	if request.method == 'POST':
		# if fileids is in data
		if request.args.get('fileids') != None:
			fileids = request.args.get('fileids')
			data = {'message': 'Received post request and fileids'}
			return jsonify(data)

		else:
			data = {'message': 'Received post request but did not find fileids'}
			return jsonify(data)

	data = {'message': 'Did not receive post request'}
	return jsonify(data)


# Get file list

# Check database for missing files


if __name__ == "__main__":
    app.run(host='0.0.0.0')
