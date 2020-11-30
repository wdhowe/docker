# Import Flask module
from flask import Flask

# Import flask restful modules
from flask_restful import Api, Resource, reqparse

# Create Flask app and restful api
app = Flask(__name__)
api = Api(app)

# Data (instead of database)
systems = [
  {
    "hostname": "server01",
    "os": "CentOS 7"
  },
  {
    "hostname": "server02",
    "os": "Ubuntu"
  }
]

#-- API Endpoints (Systems) --#
class Systems(Resource):

  # get - retrieve existing
  def get(self, hostname):
    for system in systems:
      if hostname == system["hostname"]:
        return system, 200
    return "System not found", 404

  # post - add new
  def post(self, hostname):
    parser = reqparse.RequestParser()
    parser.add_argument("os")
    args = parser.parse_args()

    for system in systems:
      if hostname == system["hostname"]:
        return "System with name {} already exists".format(hostname), 400

    system = {
      "hostname": hostname,
      "os": args["os"]
    }
    systems.append(system)
    return system, 201

  # put - modify existing
  def put(self, hostname):
    parser = reqparse.RequestParser()
    parser.add_argument("os")
    args = parser.parse_args()

    for system in systems:
      if hostname == system["hostname"]:
        # Modify existing system if it exists
        system["os"] = args["os"]
        return system, 200

    # Add new system if it does not exist already
    system = {
      "hostname": hostname,
      "os": args["os"],
    }
    systems.append(system)
    return system, 201

  # delete - remove existing
  def delete(self, hostname):
    global systems
    systems = [ system for system in systems if system["hostname"] != hostname ]
    return "{} is deleted.".format(hostname), 200

#-- End of API Endpoint (Systems) --##

# Add Systems resource to API and specify endpoint (/systems/)
api.add_resource(Systems, "/systems/<string:hostname>")

# Run the app
app.run(debug=False, host='0.0.0.0')

