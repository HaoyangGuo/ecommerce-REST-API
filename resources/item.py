from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price", type=float, required=True)
    parser.add_argument("store_id", type=int, required=True)

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        else:
            return {"Message": "Item doesn't exist"}, 404

    @jwt_required()
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"message": "Item {} already exist".format(name)}, 400

        data = Item.parser.parse_args()
        item = ItemModel(name, data["price"], data["store_id"])
        
        try:
            item.save_to_db()
        except:
            return {"Message": "An error occured."}, 500

        return item.json(), 201

    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            ItemModel.delete_from_db(item)
            return {'message': 'Item deleted'}
        else:
            return {'Message': "An error occured"}, 500

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item:
            try:
                item.price = data["price"]
                ItemModel.save_to_db(item)
            except:
                return {"Message": "An error occured."}, 500
        else:
            item = ItemModel(name, data["price"], data["store_id"])
            ItemModel.save_to_db(item)
            
        return item.json()


class ItemsList(Resource):
    def get(self):
        items = [item.json() for item in ItemModel.query.all()]
        if items:
            return {"items": items}
        else:
            return {"Message": "No item exists at the moment"}
