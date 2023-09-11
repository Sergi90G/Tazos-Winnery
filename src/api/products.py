from flask_restful import Resource, reqparse
from src.models import Product


class ProductApi(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("name",
                        type=str,
                        required=True,
                        help="Name is required and should be a string")
    parser.add_argument("category",
                        type=str,
                        required=True,
                        help="category is required and should be a string")
    parser.add_argument("description",
                        type=str,
                        required=True,
                        help="description is required and should be a string")
    parser.add_argument("yearofbottling",
                        type=int,
                        required=True,
                        help="yearofbottling is required and should be a integer")
    parser.add_argument("price ",
                        type=int,
                        required=True,
                        help="Price is required and should be a integer")
    parser.add_argument("photo ",
                        type=str,
                        required=True,
                        help="Photo is  required")

    def get(self):
        products = Product.query.all()
        product_list = []

        for product in products:
          product_info = {
            "id": product.id,
            "name": product.name,
            "category": product.category,
            "description": product.description,
            "yearofbottling": product.yearofbottling,
            "price": product.price,
            "photo": product.photo,
        }
        product_list.append(product_info)

        return product_list, 200

    def post(self):
        post_parser = self.parser.parse_args()
        try:
            existing_product = Product.query.filter_by(name=post_parser["name"]).first()
            if existing_product:
                return "product name is exists"

            new_product = Product(name=post_parser["name"], category=post_parser["category"],
                              description=post_parser["description"],
                              yearofbottling=post_parser["yearfbottling"], price=post_parser["price"],
                              photo=post_parser["photo"])
            new_product.create()
            return new_product.id, 200
        except:
            return "failure", 501


    def put(self, id):
        existing_product = Product.query.get(id)
        parser = self.parser.parse_args()
        if not existing_product:
            return "Product not found", 404

        existing_product.name = parser["name"]
        existing_product.category = parser["category"]
        existing_product.description = parser["description"]
        existing_product.yearofbottling = parser["yearofbottling"]
        existing_product.price = parser["price"]
        existing_product.photo = parser["photo"]

        existing_product.save()

        return "Success", 200


    def delete(self, id):
        product = Product.query.get(id)
        if product:
            product.delete()
            return "Success", 200
        else:
            return "Product not found", 404

