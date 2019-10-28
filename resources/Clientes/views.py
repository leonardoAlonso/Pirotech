from flask_restful import Resource


class Cliente(Resource):
    def get(self):
        return {"message": "Hello, World!"}
    
    def post(self):
        return {"message": "Hello, World!"}