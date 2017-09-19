from app import db


class User(db.Model):

    keyindex = db.Column(db.Integer, primary_key=True)
    summoner1id = db.Column(db.Integer, index=True)
    summoner2id = db.Column(db.Integer, index=True)
    matchid = db.Column(db.Integer, index=True)
    season = db.Column(db.Integer, index=True)
    regioncode = db.Column(db.String(10), index=True)
    winorlose = db.Column(db.Integer, index=True) #(0=lose 1=win 2=remake)
    soloduo = db.Column(db.Integer, index=True) #(0=duo 1=p1solo 2=p2solo)
    c1id = db.Column(db.Integer, index=True)
    c2id = db.Column(db.Integer, index=True)
    c1k = db.Column(db.Integer, index=True)
    c2k = db.Column(db.Integer, index=True)
    c1d = db.Column(db.Integer, index=True)
    c2d = db.Column(db.Integer, index=True)
    c1a = db.Column(db.Integer, index=True)
    c2a = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<User %r>' % (self.nickname)


    def __repr__(self):
        return '<Post %r>' % (self.body)
