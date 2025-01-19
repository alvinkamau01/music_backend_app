## work on last and research on how to query an online api and research on JWT
from flask_restful import Resource
from flask import request,jsonify, make_response
from models.song_request import SongRequest
from utils.config import db

class SongRequestResource(Resource):
    def get(self,song_request_id):
        song_request=SongRequest.query.get(song_request_id)
        if not song_request:
            return make_response(jsonify({"error":"song requested not found"}),500)
        return make_response(jsonify({"title":song_request.title,"id":song_request.id}))

    
    def delete (self,song_request_id):
        song_request=SongRequest.query.get(song_request_id)
        db.session.delete(song_request)
        db.session.commit()

        return make_response(jsonify({"message":"song deleted successfully"}),200)




class SongRequestListResource(Resource):
    def get(self):
     song_requests = SongRequest.query.all()  # Fetch all song requests
     # Create a list of dictionaries containing 'title' and 'id' for each song request
     response_data = [{"title": song.title, "id": song.id} for song in song_requests]
     return make_response(jsonify(response_data), 200)

    
    def post(self):
        data=request.get_json()
        new_song_request=SongRequest(
            title=data['title']
        )
        db.session.add(new_song_request)
        db.session.commit()

    