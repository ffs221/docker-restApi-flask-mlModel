from marshmallow import validate, Schema, fields,EXCLUDE,pre_load,ValidationError
from incoming import datatypes, PayloadValidator

class CreateUserSchema(PayloadValidator):
    empStatus = datatypes.String() 
    sex = datatypes.String() 
    isNewCustomer = datatypes.String() 
    isPrimCustomer = datatypes.String() 
    customerType = datatypes.String() 
    customerRelation = datatypes.String() 
    isResidence = datatypes.String() 
    isNational = datatypes.String() 
    isSpouse = datatypes.String() 
    isDeceased = datatypes.String() 
    addressType = datatypes.String() 
    isCustomer = datatypes.String() 
    segmentType = datatypes.String() 
    countryResidency = datatypes.String() 
    channelType  = datatypes.String() 
    age  = datatypes.String() 
    seniority = datatypes.String() 
    rent = datatypes.String() 

# @dataclass_json
# @dataclass
class UpdateUserSchema(PayloadValidator):
    age  = datatypes.String() 
    seniority = datatypes.String() 
    segmentType  = datatypes.String() 
    sex = datatypes.String() 
    customerType = datatypes.String() 
    rent  = datatypes.String() 
    isNational = datatypes.String() 
    isCustomer = datatypes.String() 
    countryResidency = datatypes.String() 
 
