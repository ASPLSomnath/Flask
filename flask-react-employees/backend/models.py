from app import db


class Employee(db.Model):
    ## id, name , role, description,gender ,img_url

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    gender = db.Column(db.String(6), nullable=False)
    img_url = db.Column(db.String(250), nullable=True)


    def to_json(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "role" : self.role,
            "description" : self.description,
            "gender" : self.gender,
            "imgUrl" : self.img_url,
        }