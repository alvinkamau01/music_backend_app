from utils.config import db
from models.user import User
from flask_restful import Resource
from flask import request,jsonify,make_response

class UserListResource(Resource):
    def get(self):
        users=User.query.all()
        return make_response(jsonify([user.serialize() for user in users]),200)
    
    def post(self):
        data=request.get_json()
        required_fields=["image","username","email","password","confirm_password"]
        for field in required_fields:
            if field not in data:
                return make_response(jsonify({"error": f"Missing field ${field} required"}),400)

        new_user=User(
           image=data["image"], 
           username=data["username"],
           email=data["email"],
           password=data["password"],
           confirm_password=data["confirm_password"],
           )

        db.session.add(new_user)
        db.session.commit()
        return make_response(jsonify({"message":"user created successfully"}))

class UserResource(Resource):
    def get(self,user_id):
        user=User.query.get(user_id)
        return make_response(jsonify(user.serialize()),200)
    
    def delete(self,user_id):
        user=User.query.get(user_id)
        if not user:
            return make_response(jsonify({"message":"event not found"}))
        db.session.delete(user)
        db.session.commit()

        return make_response(jsonify({"message": "User deleted successfully"}))
    
    def put(self,user_id):
        user=User.query.get(user_id)
        if not user:
            return make_response(jsonify({"message","data requested not found"}),400)
        data=request.get_json()
        user.image=data.get("image", user.image)
        user.username=data.get("username",user.username)
        user.email=data.get("email",user.email)
        user.password=data.get("password",user.password)
        user.confirm_password=data.get("confirm_password", user.password)

        db.session.commit()

        return make_response(jsonify({"message":"update successful"}))
        



