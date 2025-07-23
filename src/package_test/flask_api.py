from flask import Flask, jsonify, request
from db_orm_test.campaign import db, Campaign

# Inizializziamo l'app Flask
app = Flask(__name__)

db_schema = "mssql+pyodbc"
user = "kt"
password="kairostech1!"
db_host="10.0.0.49:1433"
db_name = "HarmonyMerge"
driver = "ODBC+Driver+13+for+SQL+Server"

# Configurazione del database
app.config["SQLALCHEMY_DATABASE_URI"] = f"{db_schema}://{user}:{password}@{db_host}/{db_name}?driver={driver}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False



# Inizializziamo SQLAlchemy con l'app Flask
db.init_app(app)

# Creiamo il database e la tabella users (una tantum)
with app.app_context():
    db.reflect()

# Rotte API


@app.route("/campaigns", methods=["GET"])
def get_campaigns():
    campaigns = Campaign.query.all()
    return jsonify([{"id": campaign.id, "name": campaign.name, "state": campaign.state} for campaign in campaigns])


@app.route("/campaigns/<int:id>", methods=["GET"])
def get_user(id):
    user = Campaign.query.get_or_404(id)
    return jsonify({"id": user.id, "name": user.name})


@app.route("/campaigns", methods=["POST"])
def create_user():
    data = request.get_json()
    new_user = Campaign(name=data["name"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"id": new_user.id, "name": new_user.name}), 201


@app.route("/campaigns/<int:id>", methods=["PUT"])
def update_user(id):
    user = Campaign.query.get_or_404(id)
    data = request.get_json()
    user.name = data["name"]
    db.session.commit()
    return jsonify({"id": user.id, "name": user.name})


@app.route("/campaigns/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = Campaign.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True)
