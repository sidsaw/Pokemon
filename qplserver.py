from flask import Flask, request, jsonify
import json
app = Flask(__name__)

print("Starting Pokemon Server!")

# Listen for post requests
@app.route('/', methods=['GET', 'POST'])
def server():
	if request.method == 'POST':
		requestdata = request.get_json()
		# if fileids is in data
		if requestdata.get('fileids') != None:
			fileids = requestdata.get('fileids')
			print('fileids')
			print(fileids)
			data = {
				'message': 'Received post request and fileids',
				'idsneeded': fileids
			}
			return jsonify(data)

		else:
			# TODO change to sending back a status code as well
			data = {
				'message': 'Received post request but did not find fileids'
			}
			return jsonify(data)

	# TODO change to sending back a status code as well
	data = {
		'message': 'Did not receive post request'
	}
	return jsonify(data)


# Get file list

# Check database for missing files


if __name__ == "__main__":
    app.run(host='0.0.0.0')
