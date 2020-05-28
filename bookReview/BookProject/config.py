import json
file = open('C:\\Users\\Le Nhat\\VSC project\\bookReview\\BookProject\\config.json', "r")
dic = json.load(file)
class Config:
    SQLALCHEMY_DATABASE_URI= dic.get("SQLALCHEMY_DATABASE_URI")
    SECRET_KEY= dic.get("SECRET_KEY")
