from google.appengine.ext import ndb


class Sporocilo(ndb.Model):
    besedilo = ndb.StringProperty()
    poslano = ndb.DateTimeProperty(auto_now_add=True)
    izbrisano = ndb.BooleanProperty(default=False)

