from flask import Flask, make_response, jsonify
from utils.config import db
from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask_cors import CORS
from routes.event_route import EventResource, EventListResource  # Corrected import
from routes.user_route import UserListResource,UserResource
from routes.ticket_route import TicketResource,TicketListResource
from routes.professional_route import ProfessionalListResource,ProfessionalResource
from routes.song_request_route import SongRequestResource,SongRequestListResource
# Configure the Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Add database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Recommended setting

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)
CORS(app)

class Homepage(Resource):
    def get(self):
        return make_response(jsonify({"message": "Welcome to music app backend"}))

# Register API resources
api.add_resource(Homepage, '/')
api.add_resource(EventListResource, '/events')  # Removed trailing slash
api.add_resource(EventResource, '/event/<int:event_id>')
api.add_resource(UserListResource,'/users')
api.add_resource(UserResource,'/user/<int:user_id>')
api.add_resource(TicketListResource,'/tickets')
api.add_resource(TicketResource,'/ticket/<int:ticket_id>')
api.add_resource(ProfessionalListResource,'/professionals')
api.add_resource(ProfessionalResource,'/professional/<int:professional_id>')
api.add_resource(SongRequestListResource,'/song_requests')
api.add_resource(SongRequestResource,'/song_request/<int:song_request_id>')





###if __name__ == '__main__':
###    app.run(port=5000, debug=True)
