from flask_restful import Resource, reqparse
from models.store import StoreModel


class Store(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument("name", type=float, required=True)

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        else:
            return {"message": "Store not found"}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"message": "Item {} already exist".format(name)}, 400
        store = StoreModel(name)

        try:
            store.save_to_db()
        except:
            return {"Message": "An error occured."}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            StoreModel.delete_from_db(store)
            return {'message': 'Store deleted'}
        else:
            return {'Message': "An error occured"}, 500


class StoreList(Resource):
    def get(self):
        stores = [store.json() for store in StoreModel.query.all()]
        if stores:
            return {"stores": stores}
        else:
            return {"Message": "No store exists at the moment"}
