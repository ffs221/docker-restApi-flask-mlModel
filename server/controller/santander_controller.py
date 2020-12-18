from flask import Blueprint
from flask import Flask, json,jsonify, g, request
from flask_cors import CORS
from ..services.santander_recom_service import (
    getProducts, getAge, getRent, getCustSeniority)
from ..models.user import (
    CreateUserSchema,
    UpdateUserSchema
)
from marshmallow import Schema, fields
# app = Flask(__name__)
# CORS(app)

santander = Blueprint('santander', __name__, url_prefix='/api/santander')
CORS(santander, max_age=30 * 86400)


@santander.route('/', methods=['POST'])
def post_recom():
    """
    .. http":post":": /api/santander

    Function that given the dish data it creates it.

    Example":":
    minimal body = {
        "age"":"23",
        "seniority"":"3",
        "segmentType"": "individual",
        "sex"": "F",
        "customerType"": "1",
        "rent"":"50000",
        "isNational"":"N",
        "isCustomer"":"1",
        "countryResidency"": "BG"
    }
        body = {
        "empStatus"": "A",
        "sex"": "F",
        "isNewCustomer"": "1",
        "isPrimCustomer"": "1",
        "customerType"": "1",
        "customerRelation"": "A",
        "isResidence"": "Y",
        "isNational"":"N",
        "isSpouse"":"Y",
        "isDeceased"":"N",
        "addressType"": "1",
        "isCustomer"":"1",
        "segmentType"": "individual",
        "countryResidency"": "BG",
        "channelType"": "013",
        "age"":"23",
        "seniority"":"3",
        "rent"":"50000"
    }

    ":param body": the data of the user sent in the body of the request.
    ":type body": dict

    """
    data = request.get_json()
    schema = UpdateUserSchema()
    errors = schema.validate(data) 
    if False in errors:
        return jsonify(errors), 400
        
    return getProducts(data)
