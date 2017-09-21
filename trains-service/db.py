import web

db = web.database(dbn="sqlite", db="trains.db")

def get_trains():
    return db.select("train")

def get_train(id):
    return db.where("train", id=id).first()




