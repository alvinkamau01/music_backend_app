from flask import request,make_response,jsonify
from utils.config import db
from models.professional import Professional
from flask_restful import Resource

class ProfessionalResource(Resource):
    def get(self,professional_id):
        professional=Professional.query.get(professional_id)
        if not professional:
            return make_response(jsonify({"error":"professional not found"}),500)
        return make_response(jsonify(professional.serialize()),200)

    def delete(self,professional_id):
        professional=Professional.query.get(professional_id)
        if not professional:
            return make_response(jsonify({"message":"professional to be deleted not found"}),500)
        db.session.delete(professional)
        db.session.commit()

        return make_response(jsonify({"message":"professional deleted successfully"}),200)


    def put(self,professional_id):
        professional=Professional.query.get(professional_id)
        if not professional:
            return make_response(jsonify({"error":"professional to be updated not found"}),500)
        
        data=request.get_json()
        professional.song_path=data.get("song_path",professional.song_path)
        professional.about=data.get("about",professional.about)
        professional.socials=data.get("socials",professional.socials)
        professional.banner_image=data.get("banner_image", professional.banner_image)

        db.session.commit()
        return make_response(jsonify({"message":"Professional updated succesfully"}),200)

   

class ProfessionalListResource(Resource):
    def get(self):
        professionals=Professional.query.all()
        if not professionals:
            return make_response(jsonify("error","data query unsuccessful"),400)
        return make_response(jsonify([professional.serialize() for professional in professionals]),200)

    def post(self):
        data=request.get_json()
        required_fields=["song_path","about","socials","banner_image"]
        for field in required_fields:
            if not field:
                return make_response(jsonify({"error":f"${field} required"}),400)

        new_professional=Professional(
            song_path=data["song_path"],
            about=data["about"],
            socials=data["socials"],
            banner_image=data['banner_image'],
        )
        db.session.add(new_professional)
        db.session.commit()

        return make_response(jsonify({"message":"professional added successfully"}),200)


    