from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import requests
import googlemaps 
from datetime import datetime


gmaps = googlemaps.Client(key='AIzaSyBhZ8mFk-0nHXMcO0dg4enWHgNnmnsoQEo')


app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/getdistance', methods=['GET', 'POST'])
@cross_origin()
def getDistance():
    if request.method == 'GET':
        mode=request.args['mode']
        startLocation=request.args['startlocation']
        endLocation=request.args['endlocation']
        paramList=["driving","walking","bicycling","transit"]
        data=None
        statusCode=None
        status=None
        for i in paramList:

            if mode not in paramList:
                statusCode="400"
                status="Fail"
                data="Invalid mode. please, use one of the following mode "+paramList[0]+" ,"+paramList[1]+" ,"+paramList[2]+" ,"+paramList[3]
                break
        print(mode,startLocation,endLocation,data)
        try:
            directions_result = gmaps.directions(startLocation,
                                        endLocation,
                                        mode=mode,
                                        )
            data=(directions_result[0])['legs'][0]['distance']['text']
            statusCode="200"
            status="Success"
        except:
            pass                            
        
        response={"status":status,"statuscode":statusCode,"data":data}
        return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80,debug=True)
