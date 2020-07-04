from flask import Flask, request, jsonify
import json
app = Flask(__name__)

print("Starting Pokemon Server!")

# Listen for post requests
@app.route('/', methods=['GET', 'POST'])
def server():
	if request.method == 'POST':
		print("detected post request")
		requestdata = request.get_json()
		# if fileids is in data
		if requestdata.get('fileids') != None:
			print("detected fileids in form data")
			fileids = requestdata.get('fileids')
			# TODO query database and find which file ids needed
			data = {
				'log': 'Received post request and fileids',
				'idsneeded': fileids
			}
			return jsonify(data)

		# if files and neededids are in data
		elif (requestdata.get('files') != None and
				requestdata.get('idsneeded') != None):
			print("detected files and idsneeded in form data")
			files = requestdata.get('files')
			idsneeded = requestdata.get('idsneeded')
			# TODO Parse files for replayid
			# TODO check if replay was already parsed
			droppedids = []
			# TODO change statement below
			parsedids = idsneeded
			# TODO Update database with stats for new files
			print("Printing files")
			for file in files:
				print(files)
			logstring = 'Updated replays with fileids: ' + parsedids + ' ignored replayed with fileids: ' + droppedids
			data = {
				'log': logstring
			}
			return jsonify(data)

		else:
			print("did not detect fileids, files, idsneeded in form data")
			# TODO change to sending back a status code as well
			data = {
				'log': 'Received post request but did not find fileids or (files and idsneeded)'
			}
			return jsonify(data)

	# TODO change to sending back a status code as well
	print("did not detect post request")
	data = {
		'log': 'Did not receive post request'
	}
	return jsonify(data)


# Get file list

# Check database for missing files


if __name__ == "__main__":
    app.run(host='0.0.0.0')
