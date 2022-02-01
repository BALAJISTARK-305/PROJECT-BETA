import csv
from flask import request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="Every item needs a store_id."
                        )

    # @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        data = Item.parser.parse_args()

        if ItemModel.find_by_name(data['name']):
            return {'message': "An item with name '{}' already exists.".format(data['name'])}, 400

        if data['price'] < 0.0:
            return {'message': "price should be postive value"}, 400

        item = ItemModel(**data)

        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted.'}
        return {'message': 'Item not found.'}, 404

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(data['name'])

        if data['price'] < 0.0:
            return {'message': "price should be postive value"}, 400

        if item:
            item.price = data['price']
        else:
            item = ItemModel(**data)

        item.save_to_db()

        return item.json()


class ItemList(Resource):
    def get(self):
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}


class Multiple_items(Resource):
    def post(self):
        list_of_items = request.get_json()

        for data in list_of_items:

            if ItemModel.find_by_name(data['name']):
                return {'message': "An item with name '{}' already exists.".format(data['name'])}, 400
            if data['price'] < 0.0:
                return {'message': "price should be postive value"}, 400

            item = ItemModel(**data)

            try:
                item.save_to_db()
            except:
                return {"message": "An error occurred inserting the item."}, 500

        return list_of_items, 201

# sample csv file to test is located in static folder


class UploadCSV(Resource):

    def post(self):
        # Create variable for uploaded file
        f = request.files['file']

        # store the file contents as a string
        fstring = f.read()
        csvfile = fstring.decode('utf-8')

        # create list of dictionaries keyed by header row
        csv_dicts = [{k: v for k, v in row.items()} for row in csv.DictReader(
            csvfile.splitlines(), skipinitialspace=True)]
        for data in csv_dicts:

            if ItemModel.find_by_name(data['name']):
                return {'message': "An item with name '{}' already exists.".format(data['name'])}, 400
            data['price'] = float(data['price'])
            if data['price'] < 0.0:
                return {'message': "price should be postive value"}, 400

            item = ItemModel(data['name'], data['price'], data['store_id'])

            try:
                item.save_to_db()
            except:
                return {"message": "An error occurred inserting the item."}, 500

            # do something list of dictionaries
        return "success"
