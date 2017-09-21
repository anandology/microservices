import web
import db
import json

urls = (
    "/trains", "trains",
    "/trains/(\d+)", "train"
)
app = web.application(urls, globals())


class trains:
    def GET(self):
        trains = db.get_trains().list()
        return json.dumps(trains)

class train:
    def GET(self, id):
        t = db.get_train(id)
        if not t:
            raise web.NotFound('{"error": "Not Found"}')
        return json.dumps(t)

if __name__ == "__main__":
    app.run()
