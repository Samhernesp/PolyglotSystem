from mongoengine import Document, EmbeddedDocument, fields

class Children(EmbeddedDocument):
    name = fields.StringField(required=True)
    born_date = fields.DateTimeField()
    genre = fields.StringField()
    study = fields.BooleanField()
    play_videogames = fields.BooleanField()
    videogames_platforms = fields.ListField(fields.StringField())

class ClientPlace(EmbeddedDocument):
    city = fields.StringField()
    state = fields.StringField()
    country = fields.StringField()
    postal_code = fields.StringField()

class Client(Document):
    client_id = fields.StringField(required=True)
    children = fields.EmbeddedDocumentListField(Children)
    born_place = fields.EmbeddedDocumentField(ClientPlace)
    place_residence = fields.EmbeddedDocumentField(ClientPlace)
    hobbies = fields.ListField(fields.StringField())
    sports = fields.ListField(fields.StringField())
    civil_status = fields.StringField()
    civil_status_date = fields.DateTimeField()
    couple = fields.ReferenceField('self')
    categories_of_interest = fields.ListField()