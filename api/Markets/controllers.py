from .models import Market

def uniqueMarket(latitude, longitude):
    market = None
    if latitude is not None and longitude is not None:
        market = Market.query.filter_by(latitude=latitude, longitude=longitude).first()
    return market

def createMarket(**data):
    """
        Create new Market

        Return:
            [market, object]
    """
    market = Market(**data)
    market.save()
    return market
