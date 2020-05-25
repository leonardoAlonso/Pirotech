from api.models import db, bc
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import MarketSchema
from .controllers import *

markets_schema = MarketSchema(many=True)
market_schema = MarketSchema()

parcer = reqparse.RequestParser()
parcer.add_argument('name', type=str, required=True,
                    help="the market name is a required parameter")
parcer.add_argument('latitude', type=float, required=False)
parcer.add_argument('longitude', type=float, required=False)

class MarketsView(Resource):
    """
        Markets View
        GET many, POST
    """
    @classmethod
    def get(cls):
        pass

    @classmethod
    def post(cls):
        """
        Add new market
        """
        args = parcer.parse_args()
        if uniqueMarket(args['latitude'], args['longitude']) is not None:
            return {'status': 'error', 'data': 'A market with this latitude and longitude exist'}, 400
        market = createMarket(**args)
        response = market_schema.dump(market).data
        return {
            'status': 'success',
            'data': {
                'market': response,
            }
        }, 201

        

class MarketView(Resource):
    pass
