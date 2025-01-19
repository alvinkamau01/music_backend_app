from models.ticket import Ticket
from flask import request,jsonify,make_response
from flask_restful import Resource
from utils.config import db

class TicketResource(Resource):
    def get(self,ticket_id):
        ticket=Ticket.query.get(ticket_id)
        if not ticket:
            return make_response(jsonify({"error": "Ticket not found"}),404)
        return make_response(jsonify(ticket.serialize()),200)

    def put(self,ticket_id):
        ticket=Ticket.query.get(ticket_id)
        if not ticket:
            make_response(jsonify({"error":"data to be updated not found"}),500)
        
        data=request.get_json()
        ticket.name=data.get("name",ticket.name)
        ticket.ticket_class=data.get("ticket_class", ticket.ticket_class)
        ticket.seat=data.get("seat", ticket.seat)
        ticket.amount_paid=data.get("amount_paid",ticket.amount_paid)
        ticket.qr_code=data.get("qr_code", ticket.qr_code)

        db.session.commit()

        return make_response(jsonify({"message":"data updated successfully"}),200)
    def delete(self,ticket_id):
        ticket=Ticket.query.get(ticket_id)
        if not ticket:
            return make_response(jsonify({"error":"data to be deleted not found"}),500)
        db.session.delete(ticket)
        db.session.commit()

        return make_response(jsonify({"message":"ticket deleted successfully"}))

class TicketListResource(Resource):
    def get(self):
        tickets=Ticket.query.all()
        if not tickets:
            return make_response(jsonify({"error":"ticket not found"}),500)
        return make_response(jsonify([ticket.serialize()for ticket in tickets]),200)
    
        

    def post(self):
        data=request.get_json()
        new_ticket=Ticket(
            name=data["name"],
            ticket_class=data["ticket_class"],
            seat=data['seat'],
            amount_paid=data["amount_paid"],
            qr_code=data["qr_code"]
        )
        db.session.add(new_ticket)
        db.session.commit()

        return make_response(jsonify({"message":"data posted successfully"}),200)
